#!/usr/bin/env python3
"""Vérification structurelle du plugin event-ops.

Ne juge PAS la qualité des livrables — c'est un jugement humain (test de
l'étranger compétent). Vérifie uniquement les invariants mécaniques, en
particulier ceux qui sont écrits à deux endroits et finiront par diverger.

Usage :  python3 scripts/check_plugin.py [--quiet]
Sortie :  0 si tout passe, 1 sinon.
"""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
SKILLS_DIR = ROOT / "skills"
CONVENTION = ROOT / "references" / "convention-dossier.md"
README = ROOT / "README.md"

# Nombres écrits en toutes lettres, pour les comptes annoncés en prose.
# Triés du plus long au plus court à l'usage : « dix-sept » avant « dix ».
MOTS = {
    "cinq": 5, "six": 6, "sept": 7, "huit": 8, "neuf": 9, "dix": 10,
    "onze": 11, "douze": 12, "treize": 13, "quatorze": 14, "quinze": 15,
    "seize": 16, "dix-sept": 17, "dix-huit": 18,
}

errors: list[str] = []
warnings: list[str] = []


def err(check: str, msg: str) -> None:
    errors.append(f"{check}: {msg}")


def warn(check: str, msg: str) -> None:
    warnings.append(f"{check}: {msg}")


def frontmatter(text: str) -> str | None:
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None


def field(fm: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+?)\s*$", fm, re.M)
    return m.group(1) if m else None


# --- 1. Manifeste ------------------------------------------------------------
# Le bug qui a réellement eu lieu : plugin.json jamais commité (cp -r a sauté
# le répertoire caché), rendant le plugin non installable.

manifest = None
if not MANIFEST.exists():
    err("manifeste", f"{MANIFEST.relative_to(ROOT)} absent — plugin non installable")
else:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err("manifeste", f"JSON invalide — {e}")
    else:
        for key in ("name", "version", "description"):
            if not manifest.get(key):
                err("manifeste", f"champ '{key}' manquant ou vide")
        home = manifest.get("homepage", "")
        if re.search(r"REMPLACER|REPLACE|TODO|XXX|example\.com", home, re.I):
            err("manifeste", f"homepage contient un placeholder — {home!r}")

        # Licence : le champ et le fichier se répondent, ou ni l'un ni l'autre.
        # Un dépôt public sans licence est « tous droits réservés » — ce qui
        # contredit le README, qui invite à installer le plugin depuis git.
        licence = manifest.get("license")
        fichier_licence = (ROOT / "LICENSE").exists()
        if licence and not fichier_licence:
            err("licence", f"le manifeste annonce '{licence}' mais LICENSE est absent")
        elif fichier_licence and not licence:
            err("licence", "LICENSE existe mais le manifeste ne déclare pas de 'license'")


# --- 1 bis. Marketplace ------------------------------------------------------
# Le dépôt est son propre marketplace (schéma à plugin unique : plugin.json et
# marketplace.json côte à côte, source "."). Version, description et keywords y
# sont donc écrits deux fois — invariant dupliqué, donc à épingler.

if not MARKETPLACE.exists():
    err("marketplace", f"{MARKETPLACE.relative_to(ROOT)} absent — plugin non installable depuis git")
else:
    try:
        mkt = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        err("marketplace", f"JSON invalide — {e}")
    else:
        entries = mkt.get("plugins")
        if not entries:
            err("marketplace", "aucune entrée dans 'plugins'")
        else:
            names = [e.get("name") for e in entries]
            if manifest and manifest.get("name") not in names:
                err(
                    "marketplace",
                    f"le plugin '{manifest.get('name')}' n'est pas listé (trouvé : {names})",
                )
            for e in entries:
                src = e.get("source")
                if not src:
                    err("marketplace", f"{e.get('name')} — champ 'source' manquant")
                elif not (ROOT / src).exists():
                    err("marketplace", f"{e.get('name')} — source '{src}' introuvable")
                elif not (ROOT / src / ".claude-plugin" / "plugin.json").exists():
                    err("marketplace", f"{e.get('name')} — source '{src}' sans plugin.json")

            if manifest:
                entry = next((e for e in entries if e.get("name") == manifest.get("name")), None)
                if entry:
                    if entry.get("version") != manifest.get("version"):
                        err(
                            "versions",
                            f"marketplace annonce {entry.get('version')} "
                            f"alors que le manifeste est en {manifest.get('version')}",
                        )
                    if entry.get("description") != manifest.get("description"):
                        err("marketplace", "description divergente entre marketplace.json et plugin.json")
                    if entry.get("keywords") and entry["keywords"] != manifest.get("keywords"):
                        warn("marketplace", "keywords divergents entre marketplace.json et plugin.json")

        meta = mkt.get("metadata", {})
        if manifest and meta.get("version") and meta["version"] != manifest.get("version"):
            err(
                "versions",
                f"marketplace.metadata en {meta['version']} "
                f"alors que le manifeste est en {manifest.get('version')}",
            )


# --- 2. Skills : frontmatter et cohérence de version -------------------------

skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()) if SKILLS_DIR.exists() else []
if not skill_dirs:
    err("skills", "aucune skill trouvée dans skills/")

skill_names: list[str] = []
for d in skill_dirs:
    rel = d.name
    sk = d / "SKILL.md"
    if not sk.exists():
        err("skills", f"{rel}/ n'a pas de SKILL.md")
        continue
    text = sk.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        err("skills", f"{rel} — frontmatter YAML absent ou malformé")
        continue

    name = field(fm, "name")
    version = field(fm, "version")
    desc = "description:" in fm

    if not name:
        err("skills", f"{rel} — champ 'name' absent")
    elif name != rel:
        # Un name désaligné du répertoire et la skill ne se déclenche jamais.
        err("skills", f"{rel} — name='{name}' ne correspond pas au répertoire")
    else:
        skill_names.append(name)

    if not desc:
        err("skills", f"{rel} — champ 'description' absent")
    if not version:
        err("skills", f"{rel} — champ 'version' absent")
    elif manifest and version != manifest.get("version"):
        err(
            "versions",
            f"{rel} en {version} alors que le manifeste est en {manifest['version']}",
        )


# --- 3. Références ${CLAUDE_PLUGIN_ROOT} -------------------------------------
# Échec silencieux : Claude ne trouve pas le fichier et improvise à partir de sa
# mémoire — ce que les skills lui interdisent explicitement.

for d in skill_dirs:
    sk = d / "SKILL.md"
    if not sk.exists():
        continue
    for ref in set(re.findall(r"\$\{CLAUDE_PLUGIN_ROOT\}/([A-Za-z0-9_./-]+)", sk.read_text(encoding="utf-8"))):
        if not (ROOT / ref).exists():
            err("références", f"{d.name} pointe vers {ref} — introuvable")


# --- 4. Mapping skill → fichier écrit ----------------------------------------
# Invariant dupliqué : la convention et chaque SKILL.md déclarent la même chose.

if not CONVENTION.exists():
    err("convention", "references/convention-dossier.md absent")
else:
    conv = CONVENTION.read_text(encoding="utf-8")
    declared = dict(
        re.findall(
            r"\|\s*`(event-[a-z]+)`\s*\|[^|]*\|\s*`?([0-9]{2}-[a-z-]+\.md|livrables/\*)`?\s*\|",
            conv,
        )
    )
    if not declared:
        err("convention", "table 'lit / écrit' introuvable ou format changé")

    for d in skill_dirs:
        sk = d / "SKILL.md"
        if not sk.exists():
            continue
        expected = declared.get(d.name)
        if expected is None:
            err("convention", f"{d.name} absent de la table lit/écrit")
            continue
        if expected == "livrables/*":
            continue  # event-dossier écrit un jeu de fichiers générés
        # Tolérant à la prose : « écris X », « Écris le tout dans X », retour
        # à la ligne entre le verbe et le fichier. On ne normalise pas la
        # rédaction des skills pour le confort du linter.
        written = re.findall(
            r"[eé]cris[^`]{0,30}`(\d{2}-[a-z-]+\.md)`",
            sk.read_text(encoding="utf-8"),
            re.I | re.S,
        )
        if not written:
            err("convention", f"{d.name} ne déclare écrire aucun fichier (attendu {expected})")
        elif expected not in written:
            err("convention", f"{d.name} écrit {written[0]} mais la convention dit {expected}")

    # --- 4 bis. Instruction `lu:` ---------------------------------------------
    # La convention attend que toute brique dépendant d'une autre consigne la
    # version qu'elle a lue. Ce contrôle vérifie que la skill le DIT — pas
    # qu'elle le fasse : c'est une déclaration, pas une mesure. Il attrape la
    # skill ajoutée plus tard sans l'instruction, pas la skill qui ment.
    lit_de = dict(
        re.findall(
            r"\|\s*`(event-[a-z]+)`\s*\|([^|]*)\|\s*`?(?:[0-9]{2}-[a-z-]+\.md|livrables/\*)`?\s*\|",
            conv,
        )
    )
    for d in skill_dirs:
        sk = d / "SKILL.md"
        if sk.exists() is False or d.name not in declared:
            continue
        text = sk.read_text(encoding="utf-8")
        mentionne = "`lu:`" in text
        nie = re.search(r"[Pp]as de champ\s+`lu:`", text) is not None

        # Deux exceptions, tirées de la convention et non redéclarées ici :
        # event-dossier n'écrit pas de frontmatter, event-cadrage est l'ancre.
        lit = lit_de.get(d.name, "")
        sans_dependance = not re.search(r"`\d{2}`|tous", lit)
        exception = declared[d.name] == "livrables/*" or sans_dependance

        if exception:
            if not nie:
                err(
                    "lu",
                    f"{d.name} n'a pas de dépendance à consigner : "
                    "il doit dire explicitement « pas de champ `lu:` »",
                )
        elif not mentionne:
            err("lu", f"{d.name} ne dit pas de renseigner `lu:` (la convention l'attend)")
        elif nie:
            err("lu", f"{d.name} nie le champ `lu:` alors qu'il dépend de {lit.strip()}")

    # --- 4 ter. Forme du champ `lu:` enseignée par les skills -----------------
    # `check_dossier.py` ne relit QUE la forme bloc. Une skill qui montre la forme
    # sur une seule ligne neutralise le contrôle de péremption sans un message : le
    # dossier sort vert alors que rien n'a été vérifié. C'est arrivé sur deux skills.
    for d in skill_dirs:
        sk = d / "SKILL.md"
        if not sk.exists():
            continue
        if re.search(r"lu:\s*\{", sk.read_text(encoding="utf-8")):
            err(
                "lu",
                f"{d.name} montre `lu:` sur une seule ligne — seule la forme bloc "
                "est relue par check_dossier.py",
            )

    # --- 4 quater. Dépendances : convention ↔ SKILL.md ------------------------
    # Troisième invariant dupliqué : la colonne « Lit » et les DEUX endroits où une
    # skill énumère ses dépendances — la phrase « Lis … » et l'instruction `lu:`.
    # Sans ce contrôle, `event-budget` demandait de consigner la lecture d'un
    # fichier qu'il n'avait jamais dit de lire.
    index_fichier = {f[:2]: f for f in declared.values() if f != "livrables/*"}

    def cites(bloc: str) -> set[str]:
        return set(re.findall(r"`(\d{2}-[a-z-]+\.md)`", bloc))

    for d in skill_dirs:
        sk = d / "SKILL.md"
        if not sk.exists() or d.name not in declared:
            continue
        lit = lit_de.get(d.name, "")
        if re.search(r"\btous\b", lit, re.I):
            continue  # « tous ceux présents » : il n'y a rien à énumérer
        attendues = {
            index_fichier[i] for i in re.findall(r"`(\d{2})`", lit) if i in index_fichier
        }
        paras = re.split(r"\n\s*\n", sk.read_text(encoding="utf-8"))

        para_lis = next((p for p in paras if re.search(r"\bLis\b", p)), None)
        if para_lis is None:
            if attendues:
                err(
                    "dépendances",
                    f"{d.name} — aucune phrase « Lis … » alors que la convention lui "
                    f"donne {sorted(attendues)}",
                )
        else:
            vues = cites(para_lis) - {declared[d.name]}
            if vues != attendues:
                err(
                    "dépendances",
                    f"{d.name} — la phrase « Lis … » cite {sorted(vues) or '(rien)'}, "
                    f"la convention dit {sorted(attendues) or '(rien)'}",
                )

        para_lu = next((p for p in paras if "`lu:`" in p), None)
        if para_lu and not re.search(r"[Pp]as de champ\s+`lu:`", para_lu):
            vues = cites(para_lu)
            if vues != attendues:
                err(
                    "dépendances",
                    f"{d.name} — l'instruction `lu:` cite {sorted(vues) or '(rien)'}, "
                    f"la convention dit {sorted(attendues) or '(rien)'}",
                )

    # Numérotation : pas de doublon d'index entre briques.
    seen: dict[str, str] = {}
    for skill, fname in declared.items():
        if fname == "livrables/*":
            continue
        idx = fname[:2]
        if idx in seen:
            err("convention", f"index {idx} utilisé par {seen[idx]} et {skill}")
        seen[idx] = skill


# --- 5. README ↔ skills ------------------------------------------------------
# Le README a déjà menti une fois (« les six briques » pour neuf skills).

if not README.exists():
    err("readme", "README.md absent")
elif skill_names:
    readme = README.read_text(encoding="utf-8")
    for name in skill_names:
        if f"`{name}`" not in readme:
            err("readme", f"{name} n'est pas documentée dans le README")
    # Le nom du plugin lui-même apparaît légitimement (section Installation) et
    # n'est pas une skill.
    plugin_name = manifest.get("name") if manifest else None
    for cited in set(re.findall(r"`(event-[a-z]+)`", readme)):
        if cited == plugin_name:
            continue
        if cited not in skill_names:
            err("readme", f"{cited} est citée mais n'existe pas dans skills/")
    # Compte annoncé en toutes lettres.
    m = re.search(r"##\s+Les\s+([a-zé]+)\s+briques", readme, re.I)
    if m:
        annonce = MOTS.get(m.group(1).lower())
        if annonce is None:
            warn("readme", f"nombre de briques « {m.group(1)} » non reconnu")
        elif annonce != len(skill_names):
            err("readme", f"annonce « {m.group(1)} briques » mais il y en a {len(skill_names)}")


# --- 6. Fichiers de référence : comptes annoncés et skills nommées -----------
# Même classe de bug que « les six briques » du README, mais plus coûteuse : les
# skills doivent PARCOURIR ces fichiers entrée par entrée. Un compte faux et elles
# en sautent une, sans que rien ne le signale. Chaque compte est annoncé à
# plusieurs endroits du même fichier — invariant dupliqué, donc à épingler.
#
# Généralisé à tout fichier de référence : ajouter le sien à REFERENCES_COMPTEES
# suffit, il n'y a rien à recopier.

REFERENCES_COMPTEES = {
    "chantiers.md": ("lentilles", "domaines"),
    "conformite.md": ("familles", "régimes"),
}


def verifie_reference(fichier: str, noms: tuple[str, ...]) -> None:
    chemin = ROOT / "references" / fichier
    etiquette = fichier[:-3] if fichier.endswith(".md") else fichier
    if not chemin.exists():
        err(etiquette, f"references/{fichier} absent")
        return
    ch = chemin.read_text(encoding="utf-8")

    # Ce que le fichier contient réellement, section par section.
    reels: dict[str, int] = {}
    for sec in re.split(r"^## ", ch, flags=re.M):
        titre = sec.split("\n", 1)[0].lower()
        n = len(re.findall(r"^\d+\. \*\*", sec, re.M))
        for nom in noms:
            if nom in titre and n:
                reels[nom] = n

    mots_alt = "|".join(sorted(MOTS, key=len, reverse=True))
    for nom in noms:
        if nom not in reels:
            err(etiquette, f"aucune section ne numérote les {nom}")
            continue
        for m in re.finditer(rf"\b([0-9]+|{mots_alt})\s+{nom}\b", ch, re.I):
            mot = m.group(1)
            annonce = int(mot) if mot.isdigit() else MOTS[mot.lower()]
            if annonce != reels[nom]:
                err(
                    etiquette,
                    f"« {m.group(0)} » annoncé alors que le fichier en liste {reels[nom]}",
                )

    # Le fichier nomme les skills censées le parcourir. Si l'une d'elles cesse
    # d'y renvoyer, elle improvise de mémoire — ce que la skill s'interdit.
    entete = ch.split("---", 1)[0]
    for nom_skill in sorted(set(re.findall(r"`(event-[a-z]+)`", entete))):
        d = SKILLS_DIR / nom_skill
        if not (d / "SKILL.md").exists():
            err(etiquette, f"{nom_skill} est nommée mais n'existe pas dans skills/")
        elif f"references/{fichier}" not in (d / "SKILL.md").read_text(encoding="utf-8"):
            err(
                etiquette,
                f"{nom_skill} doit parcourir {fichier} mais ne le référence pas",
            )


for fichier, noms in REFERENCES_COMPTEES.items():
    verifie_reference(fichier, noms)


# --- 6 bis. Fraîcheur d'un fichier de référence réglementaire ----------------
# R-03 du registre des risques. Le linter sait vérifier la structure d'un fichier de
# référence et ses comptes ; il ne peut rien dire de l'actualité de son contenu. Un
# fichier qui cite des textes vieillit sans que rien ne le signale — mode d'échec
# habituel de toute référence sans propriétaire.
#
# Avertissement et jamais erreur : le dépôt a déjà tiré cette leçon sur les cycles. Une
# CI qui passe au rouge pour une chose qu'on ne peut pas corriger dans la minute
# s'apprend à s'ignorer, et emporte avec elle les alertes qui comptaient.

REFERENCES_DATEES = {"conformite.md": 12}  # fichier -> péremption en mois


def verifie_fraicheur(fichier: str, mois: int) -> None:
    chemin = ROOT / "references" / fichier
    if not chemin.exists():
        return
    ch = chemin.read_text(encoding="utf-8")
    etiquette = fichier[:-3] if fichier.endswith(".md") else fichier

    m = re.search(r"\*\*Dernière vérification du contenu\*\*\s*:\s*(\d{4}-\d{2}-\d{2})", ch)
    if not m:
        warn(etiquette, f"references/{fichier} ne porte pas de date de dernière vérification")
    else:
        try:
            vu = dt.date.fromisoformat(m.group(1))
        except ValueError:
            warn(etiquette, f"references/{fichier} — date de vérification '{m.group(1)}' illisible")
        else:
            age = (dt.date.today() - vu).days
            if age > mois * 30:
                warn(
                    etiquette,
                    f"references/{fichier} vérifié il y a {age // 30} mois "
                    f"(seuil {mois}) — les textes cités ont pu bouger",
                )

    m = re.search(r"\*\*Relu par\*\*\s*:\s*(.+)", ch)
    relecteur = re.sub(r"[*`]", "", m.group(1)).strip().lower() if m else ""
    if not m:
        warn(etiquette, f"references/{fichier} ne dit pas qui l'a relu")
    elif relecteur.startswith("personne"):
        warn(
            etiquette,
            f"references/{fichier} n'a jamais été relu par un humain qualifié — "
            "le contenu réglementaire est une rédaction initiale non vérifiée",
        )


for fichier, mois in REFERENCES_DATEES.items():
    verifie_fraicheur(fichier, mois)


# --- 7. Aucun fichier de référence mort --------------------------------------
# Tout ce qui vit dans le dépôt est cloné chez chaque membre de l'équipe : un
# fichier de référence que plus aucune skill n'ouvre est du poids mort livré à
# tout le monde. Ce contrôle attrape aussi le nom de fichier ACCENTUÉ — le charset
# de la référence ${CLAUDE_PLUGIN_ROOT} (§3) exclut les accents, donc un
# references/conformité.md échapperait en silence au contrôle d'existence.

referencees: set[str] = set()
for d in skill_dirs:
    sk = d / "SKILL.md"
    if sk.exists():
        referencees.update(
            re.findall(
                r"\$\{CLAUDE_PLUGIN_ROOT\}/(references/[A-Za-z0-9_./-]+)",
                sk.read_text(encoding="utf-8"),
            )
        )

for f in sorted((ROOT / "references").glob("*.md")):
    if f"references/{f.name}" not in referencees:
        err("références", f"references/{f.name} n'est ouvert par aucune skill")

# --- Rapport -----------------------------------------------------------------

quiet = "--quiet" in sys.argv
ci = os.environ.get("GITHUB_ACTIONS") == "true"

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
    n = len(skill_names)
    v = manifest.get("version", "?") if manifest else "?"
    print(f"✓  {n} skills cohérentes, manifeste v{v}, références et convention alignées.")
    if warnings:
        print(f"   ({len(warnings)} avertissement(s))")
sys.exit(0)
