#!/usr/bin/env python3
"""Passe le plugin event-ops à une nouvelle version, partout à la fois.

La version vit à TREIZE endroits : `.claude-plugin/plugin.json`, les deux champs
`version` de `.claude-plugin/marketplace.json`, et le frontmatter des dix
skills. `check_plugin.py` sait dire qu'ils divergent, mais rien n'évitait la
divergence — et un oubli sur un seul fichier ne se voit qu'après coup, en CI.

Le manifeste fait foi pour la version courante (voir CLAUDE.md). On ne remplace
que là où la valeur EST déjà la version courante : un fichier désaligné n'est
pas rattrapé en silence, il est signalé. Rattraper à la main est le bon
comportement — un fichier qui n'était pas à la bonne version pose une question
à laquelle ce script n'a pas la réponse.

Usage :  python3 scripts/bump_version.py 0.5.0
         python3 scripts/bump_version.py --minor        (--major | --minor | --patch)
         python3 scripts/bump_version.py --dry-run --minor
Sortie :  0 si tout a été mis à jour, 1 sinon.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = ROOT / "skills"

SEMVER = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


def sortir(msg: str) -> None:
    print(f"✗  {msg}")
    raise SystemExit(1)


# --- 1. Ce qu'on demande -----------------------------------------------------

args = sys.argv[1:]
dry = "--dry-run" in args
args = [a for a in args if a != "--dry-run"]

if len(args) != 1:
    sortir(
        "un seul argument attendu : une version (0.5.0) ou --major / --minor / --patch"
    )

if not MANIFEST.exists():
    sortir(f"{MANIFEST.relative_to(ROOT)} absent — le manifeste fait foi pour la version")

manifeste = MANIFEST.read_text(encoding="utf-8")
trouve = re.search(r'"version"\s*:\s*"([^"]+)"', manifeste)
if not trouve:
    sortir("aucun champ 'version' dans le manifeste")

courante = trouve.group(1)
pieces = SEMVER.match(courante)
if not pieces:
    sortir(f"version courante {courante!r} non conforme à MAJEUR.MINEUR.CORRECTIF")

cible = args[0]
if cible.startswith("--"):
    majeur, mineur, correctif = (int(x) for x in pieces.groups())
    niveau = cible[2:]
    if niveau == "major":
        majeur, mineur, correctif = majeur + 1, 0, 0
    elif niveau == "minor":
        mineur, correctif = mineur + 1, 0
    elif niveau == "patch":
        correctif += 1
    else:
        sortir(f"niveau inconnu : {cible} (attendu --major, --minor ou --patch)")
    cible = f"{majeur}.{mineur}.{correctif}"
elif not SEMVER.match(cible):
    sortir(f"{cible!r} n'est pas une version MAJEUR.MINEUR.CORRECTIF")

if cible == courante:
    sortir(f"le plugin est déjà en {courante}")


# --- 2. Où elle est écrite ---------------------------------------------------
# Motifs ciblés, jamais un remplacement de chaîne nu : « 0.4.0 » peut apparaître
# dans une prose (un montant, un exemple) qu'il ne faut surtout pas toucher.

echappee = re.escape(courante)
champ_json = re.compile(rf'("version"\s*:\s*)"{echappee}"')
champ_yaml = re.compile(rf"(^version:[ \t]*){echappee}[ \t]*$", re.M)

cibles: list[tuple[Path, re.Pattern[str], str]] = [
    (MANIFEST, champ_json, rf'\g<1>"{cible}"'),
]
if MARKETPLACE.exists():
    cibles.append((MARKETPLACE, champ_json, rf'\g<1>"{cible}"'))
else:
    print(f"⚠  {MARKETPLACE.relative_to(ROOT)} absent — non mis à jour")

for d in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.exists() else []:
    sk = d / "SKILL.md"
    if sk.exists():
        cibles.append((sk, champ_yaml, rf"\g<1>{cible}"))


# --- 3. Réécriture -----------------------------------------------------------

total = 0
desalignes: list[str] = []
for chemin, motif, remplacement in cibles:
    texte = chemin.read_text(encoding="utf-8")
    neuf, n = motif.subn(remplacement, texte)
    rel = chemin.relative_to(ROOT)
    if n == 0:
        desalignes.append(str(rel))
        continue
    if not dry:
        chemin.write_text(neuf, encoding="utf-8")
    total += n
    print(f"·  {rel} — {n} champ(s)")


# --- Rapport -----------------------------------------------------------------

prefixe = "essai à blanc — " if dry else ""

if desalignes:
    print(f"\n✗  {prefixe}{len(desalignes)} fichier(s) sans champ en {courante} :")
    for f in desalignes:
        print(f"     {f}")
    print("   Les aligner à la main, puis relancer — leur écart pose une question.")
    sys.exit(1)

print(f"\n✓  {prefixe}{courante} → {cible}, {total} champ(s) sur {len(cibles)} fichier(s).")
if not dry:
    print("   Vérifier : python3 scripts/check_plugin.py")
sys.exit(0)
