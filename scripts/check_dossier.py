#!/usr/bin/env python3
"""Vérification de cohérence d'un dossier événement produit par event-ops.

Pendant de check_plugin.py, côté sortie : celui-ci vérifie le PLUGIN, celui-là
vérifie un DOSSIER réel. Il ne juge pas la qualité des livrables — c'est un
jugement humain (test de l'étranger compétent). Il attrape ce qu'une relecture
humaine ne voit pas : un en-tête divergent, une version qui n'a pas suivi, une
brique écrite avant la dernière mise à jour de ce dont elle dépend.

Le mapping index → brique et les dépendances sont lus dans la table lit/écrit de
references/convention-dossier.md : rien n'est redéclaré ici, sinon ce script
deviendrait à son tour un invariant dupliqué.

Usage :  python3 scripts/check_dossier.py [chemin-du-dossier] [--quiet] [--no-annotations]
Sortie :  0 si aucune erreur (des avertissements restent possibles), 1 sinon.

`--no-annotations` supprime les lignes `::error::` / `::warning::` destinées à GitHub
Actions. Nécessaire quand la CI vérifie une sortie ATTENDUE en erreur : sans lui la
course s'affiche en rouge alors qu'elle valide le comportement nominal. On ne peut pas
s'en passer en forçant GITHUB_ACTIONS=false — c'est une variable réservée, que le runner
réinjecte quoi qu'on écrive dans le `env:` de l'étape.
"""

from __future__ import annotations

import datetime as dt
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONVENTION = ROOT / "references" / "convention-dossier.md"
ANCRE = "00-fiche-identite.md"

errors: list[str] = []
warnings: list[str] = []
infos: list[str] = []


def err(check: str, msg: str) -> None:
    errors.append(f"{check}: {msg}")


def warn(check: str, msg: str) -> None:
    warnings.append(f"{check}: {msg}")


def info(msg: str) -> None:
    infos.append(msg)


def frontmatter(text: str) -> str | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def field(fm: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+?)\s*$", fm, re.M)
    return m.group(1) if m else None


def lu_block(fm: str) -> dict[str, int]:
    """Champ optionnel `lu:` — versions des dépendances au moment de l'écriture.

    lu:
      00-fiche-identite.md: 1
      02-budget.md: 3
    """
    m = re.search(r"^lu:\s*$\n((?:[ \t]+\S.*\n?)*)", fm, re.M)
    if not m:
        return {}
    out: dict[str, int] = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"\s+([0-9]{2}-[a-z-]+\.md)\s*:\s*(\d+)\s*$", line)
        if mm:
            out[mm.group(1)] = int(mm.group(2))
    return out


def iso(value: str | None) -> dt.date | None:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value.strip().strip("\"'"))
    except ValueError:
        return None


# --- 0. La convention, source du mapping et des dépendances ------------------

if not CONVENTION.exists():
    print(f"✗  convention: {CONVENTION} absent — impossible de vérifier quoi que ce soit.")
    sys.exit(1)

conv = CONVENTION.read_text(encoding="utf-8")
rows = re.findall(
    r"\|\s*`(event-[a-z]+)`\s*\|([^|]*)\|\s*`?([0-9]{2}-[a-z-]+\.md|livrables/\*)`?\s*\|",
    conv,
)
if not rows:
    print("✗  convention: table 'lit / écrit' introuvable ou format changé.")
    sys.exit(1)

TOUS = "*"  # marqueur : colonne « Lit » à « tous ceux présents »

# fichier -> (brique attendue, dépendances)
attendu: dict[str, tuple[str, list[str]]] = {}
index_de: dict[str, str] = {}  # "02" -> "02-budget.md"
for skill, lit_raw, ecrit in rows:
    if ecrit == "livrables/*":
        continue
    brique = skill[len("event-"):]
    deps = re.findall(r"`(\d{2})`", lit_raw)
    # « tous ceux présents » n'énumère rien mais veut dire quelque chose de précis :
    # toutes les briques d'index inférieur. Sans cette résolution, les deux briques
    # les plus dépendantes du dossier (risques, débrief) sortaient d'ici avec ZÉRO
    # dépendance, et le contrôle de fraîcheur ne s'appliquait jamais à elles.
    if not deps and re.search(r"\btous\b", lit_raw, re.I):
        deps = [TOUS]
    attendu[ecrit] = (brique, deps)
    index_de[ecrit[:2]] = ecrit


def deps_de(fichier: str) -> list[str]:
    """Fichiers dont `fichier` dépend, marqueur TOUS résolu."""
    brut = attendu[fichier][1]
    if brut == [TOUS]:
        return [f for f in sorted(attendu) if f[:2] < fichier[:2]]
    return [index_de[i] for i in brut if i in index_de]


# Paires mutuelles : A lit B ET B lit A. Déduites de la table, jamais redéclarées.
# Sur un cycle, les deux briques ne peuvent pas être à jour l'une de l'autre en même
# temps : celle qui n'a pas été écrite en dernier porte forcément la version
# précédente de l'autre. Ce retard-là est structurel, pas une négligence.
mutuels: set[frozenset[str]] = {
    frozenset((f, autre))
    for f in attendu
    for autre in deps_de(f)
    if f in deps_de(autre)
}


# --- 1. Localiser le dossier -------------------------------------------------

args = [a for a in sys.argv[1:] if not a.startswith("--")]
if args:
    dossier = Path(args[0]).expanduser().resolve()
    if not dossier.is_dir():
        print(f"✗  dossier: {dossier} n'est pas un répertoire.")
        sys.exit(1)
else:
    cwd = Path.cwd()
    if (cwd / ANCRE).exists():
        dossier = cwd
    else:
        candidats = sorted(p for p in cwd.iterdir() if p.is_dir() and (p / ANCRE).exists())
        if len(candidats) == 1:
            dossier = candidats[0]
            print(f"→  dossier trouvé : {dossier.name}")
        elif not candidats:
            print(f"✗  dossier: aucun {ANCRE} dans {cwd} ni juste en dessous.")
            print("   Passe le chemin en argument : check_dossier.py <chemin>")
            sys.exit(1)
        else:
            # La convention l'impose : demander plutôt que deviner.
            print("✗  dossier: plusieurs dossiers candidats — précise lequel :")
            for c in candidats:
                print(f"     {c.name}")
            sys.exit(1)

presents = sorted(p.name for p in dossier.glob("[0-9][0-9]-*.md"))


# --- 2. Fichiers inattendus --------------------------------------------------

for name in presents:
    if name not in attendu:
        idx = name[:2]
        if idx in index_de:
            err("nommage", f"{name} — la convention attend {index_de[idx]} pour l'index {idx}")
        else:
            err("nommage", f"{name} — index {idx} inconnu de la convention")


# --- 3. Frontmatter de chaque brique -----------------------------------------

meta: dict[str, dict] = {}
for name in presents:
    if name not in attendu:
        continue
    brique_attendue, _ = attendu[name]
    fm = frontmatter((dossier / name).read_text(encoding="utf-8"))
    if fm is None:
        err("frontmatter", f"{name} — absent ou malformé")
        continue

    d = {
        "evenement": field(fm, "evenement"),
        "jour_j": field(fm, "jour_j"),
        "brique": field(fm, "brique"),
        "version": field(fm, "version"),
        "maj": field(fm, "maj"),
        "lu": lu_block(fm),
    }
    meta[name] = d

    for key in ("evenement", "jour_j", "brique", "version", "maj"):
        if not d[key]:
            err("frontmatter", f"{name} — champ '{key}' absent")

    if d["brique"] and d["brique"] != brique_attendue:
        err("frontmatter", f"{name} — brique='{d['brique']}', attendu '{brique_attendue}'")

    if d["version"]:
        if not re.fullmatch(r"\d+", d["version"]):
            err("version", f"{name} — version='{d['version']}' n'est pas un entier")
        elif int(d["version"]) < 1:
            err("version", f"{name} — version={d['version']}, doit démarrer à 1")

    if d["maj"] and iso(d["maj"]) is None:
        err("date", f"{name} — maj='{d['maj']}' n'est pas une date ISO (AAAA-MM-JJ)")
    if d["jour_j"] and iso(d["jour_j"]) is None:
        err("date", f"{name} — jour_j='{d['jour_j']}' n'est pas une date ISO (AAAA-MM-JJ)")


# --- 4. L'ancre fait foi -----------------------------------------------------
# « S'ils divergent, la fiche d'identité fait foi ; signaler la divergence. »

ancre = meta.get(ANCRE)
if ancre is None:
    if ANCRE in presents:
        pass  # déjà signalé plus haut
    else:
        warn("ancre", f"{ANCRE} absent — aucune référence pour vérifier evenement/jour_j")
else:
    for name, d in meta.items():
        if name == ANCRE:
            continue
        for key in ("evenement", "jour_j"):
            if d[key] and ancre[key] and d[key] != ancre[key]:
                err(
                    "ancre",
                    f"{name} — {key}='{d[key]}' diverge de la fiche d'identité "
                    f"('{ancre[key]}') ; la fiche fait foi",
                )


# --- 5. Fraîcheur : une brique écrite avant sa dépendance --------------------
# C'est le contrôle qui attrape le vrai défaut d'usage : la convention repose sur
# des sections « À faire remonter » que personne ne rejoue. Une brique dont une
# dépendance a bougé après elle est potentiellement périmée.

for name, d in meta.items():
    maj_self = iso(d["maj"])
    for dep in deps_de(name):
        if dep not in meta:
            continue
        if frozenset((name, dep)) in mutuels:
            continue  # un cycle a son propre message, plus bas
        maj_dep = iso(meta[dep]["maj"])
        if maj_self and maj_dep and maj_dep > maj_self:
            warn(
                "fraîcheur",
                f"{name} (maj {d['maj']}) est plus ancien que {dep} (maj {meta[dep]['maj']}) "
                f"dont il dépend — à repasser",
            )

    # Contrôle exact quand le champ optionnel `lu:` est renseigné.
    for dep, vue in d["lu"].items():
        if dep not in meta:
            warn("lu", f"{name} déclare avoir lu {dep}, absent du dossier")
            continue
        actuelle = meta[dep]["version"]
        if not (actuelle and re.fullmatch(r"\d+", actuelle)):
            continue
        retard = int(actuelle) - vue
        if retard <= 0:
            continue
        if retard == 1 and frozenset((name, dep)) in mutuels:
            # Coût structurel du cycle, pas un oubli. En faire une erreur, c'est
            # garantir un dossier rouge en permanence — et apprendre à l'utilisateur
            # à ignorer ce script.
            warn(
                f"cycle {min(name, dep)[:2]}↔{max(name, dep)[:2]}",
                f"{name} porte {dep} v{vue}, actuel v{actuelle} — retard d'une version, "
                f"coût normal du cycle",
            )
        else:
            err(
                "lu",
                f"{name} a été écrit sur la base de {dep} v{vue}, "
                f"or {dep} est en v{actuelle} — à repasser",
            )

# Les cycles déclarés méritent leur message : la convention impose une seconde passe.
for paire in sorted(mutuels, key=sorted):
    a, b = sorted(paire)
    if a not in meta or b not in meta:
        continue
    ma, mb = iso(meta[a]["maj"]), iso(meta[b]["maj"])
    if ma and mb and mb > ma:
        warn(
            f"cycle {a[:2]}↔{b[:2]}",
            f"{b} a bougé après {a} : `event-{attendu[a][0]}` n'a peut-être pas été "
            f"repassée (la convention impose une seconde passe sur un cycle)",
        )


# --- 6. Livrables générés ----------------------------------------------------

livrables = dossier / "livrables"
if livrables.is_dir():
    generes = [p for p in livrables.iterdir() if p.is_file()]
    if generes:
        plus_recent_source = max((dossier / n).stat().st_mtime for n in meta) if meta else 0
        plus_ancien_livrable = min(p.stat().st_mtime for p in generes)
        if plus_recent_source > plus_ancien_livrable:
            warn(
                "livrables",
                "au moins un livrable est plus ancien qu'une brique source — "
                "régénérer avec event-dossier",
            )


# --- 7. Complétude (information, jamais une erreur) --------------------------
# « Une dépendance absente n'est jamais bloquante. » On la signale, on ne la
# sanctionne pas.

manquantes = [f for f in sorted(attendu) if f not in presents]
if manquantes:
    info("briques absentes : " + ", ".join(f"{f[:2]} ({attendu[f][0]})" for f in manquantes))

if ancre:
    jj = iso(ancre["jour_j"])
    if jj:
        delta = (jj - dt.date.today()).days
        if delta > 0:
            info(f"jour J dans {delta} jours (J-{delta})")
        elif delta == 0:
            info("jour J : c'est aujourd'hui")
        else:
            info(f"jour J passé depuis {-delta} jours — dossier en phase APRÈS")

for name, d in meta.items():
    maj = iso(d["maj"])
    if maj and maj > dt.date.today():
        warn("date", f"{name} — maj={d['maj']} est dans le futur")


# --- Rapport -----------------------------------------------------------------

quiet = "--quiet" in sys.argv
ci = os.environ.get("GITHUB_ACTIONS") == "true" and "--no-annotations" not in sys.argv

for i in infos:
    if not quiet:
        print(f"·  {i}")

for w in warnings:
    print(f"⚠  {w}")
    if ci:
        print(f"::warning::{w}")

if errors:
    for e in errors:
        print(f"✗  {e}")
        if ci:
            print(f"::error::{e}")
    print(f"\n{len(errors)} erreur(s) — voir ci-dessus.")
    sys.exit(1)

if not quiet:
    nom = (ancre or {}).get("evenement") or dossier.name
    versions = ", ".join(f"{n[:2]} v{meta[n]['version']}" for n in sorted(meta))
    print(f"✓  « {nom} » — {len(meta)}/{len(attendu)} briques — {versions}")
    if warnings:
        print(f"   ({len(warnings)} avertissement(s))")
sys.exit(0)
