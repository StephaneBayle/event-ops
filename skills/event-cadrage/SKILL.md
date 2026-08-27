---
name: event-cadrage
description: >
  Point d'entrée d'un dossier événementiel. À utiliser quand l'utilisateur veut
  "lancer un nouvel événement", "cadrer un événement", "définir les objectifs d'un
  événement", "démarrer le dossier opérationnel", ou fournit le nom/format d'un
  événement sans cadre encore posé. Produit la FICHE D'IDENTITÉ : objectifs
  mesurables, KPIs, public cible, format, budget, gouvernance. C'est l'ancre dont
  toutes les autres briques dépendent.
version: 0.4.1
---

# Cadrage d'evenement — Fiche d'identite

Tu produis l'invariant du dossier : le "pourquoi" et le cadre. Tout le reste
(retroplanning, conducteur, risques) devra pouvoir s'y rattacher.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.

Tu es l'**ancre** : c'est toi qui crées le dossier. Localise-le (ou propose de le créer),
puis écris `00-fiche-identite.md`. Si une fiche existe déjà, reprends-la et complète-la
plutôt que de repartir de zéro.

**Pas de champ `lu:`** dans la fiche d'identité : tu es l'ancre, tu ne dépends d'aucune
autre brique. C'est la seule qui n'en porte pas.

Si tu repères un dossier d'événement passé (un autre répertoire avec un `07-debrief.md`),
propose de t'appuyer sur sa section « à réutiliser » : prestataires retenus, hypothèses
de fréquentation vérifiées, postes budgétaires sous-estimés.

## Consigner un arbitrage

`00-fiche-identite.md` t'appartient : tu es la **seule** brique qui puisse écrire au
**Journal des décisions**. Quand un arbitrage structurant est pris (changement de lieu, de
date, de jauge, coupe budgétaire, go/no-go), n'attends pas une demande de re-cadrage
complet : relis la fiche, **ajoute une ligne au journal** (date, décision, qui, impact),
incrémente `version`, et ne touche à rien d'autre.

Sans cela le journal reste vide — et `event-debrief`, qui en fait sa matière première,
n'aura rien à lire trois mois plus tard.

## Méthode

1. **Avant de rédiger, nomme les hypothèses implicites** sur le type, l'échelle
   et l'intention de l'événement, et signale ce qui manque.
2. Si des informations clés sont absentes, pose AU PLUS 3 questions ciblées
   (idéalement via boutons / choix). Ne bloque pas : propose des valeurs par
   défaut explicitement marquées comme hypothèses.
3. Construis la fiche autour de ces rubriques :
   - **Objectif(s)** — formulés de manière mesurable (verbe + cible + échéance).
   - **KPIs** — 3 à 5 indicateurs, chacun rattaché à un objectif, avec valeur cible.
   - **Public cible** — segments (ex. VIP, intervenants, presse, grand public),
     volume estimé par segment.
   - **Format & cadre** — date(s), lieu, durée, jauge, format (conférence, salon,
     soirée, portes ouvertes...), et **présentiel / hybride / distanciel**. L'hybride
     n'est pas un détail technique : il double le public, le conducteur et la modération.
   - **Budget** — enveloppe globale + grands postes, **en précisant HT ou TTC**.
     Ordre de grandeur si non connu, marqué comme estimation. Le détail relève de
     `event-budget` ; ici on pose l'enveloppe et sa nature.
   - **Contraintes réglementaires** — le lieu est-il un ERP ? quelle catégorie ?
     **accessibilité PMR**, autorisations à demander (voie publique, débit de boissons,
     SACEM). Poser la question tôt : ces délais sont incompressibles et conditionnent
     le rétroplanning.
   - **Gouvernance** — qui décide quoi, instance d'arbitrage, sponsor, et surtout
     **qui a le pouvoir d'annuler ou de reporter**. C'est la décision la plus lourde
     du dossier ; elle doit avoir un titulaire dès le cadrage.

## Test de qualité

La fiche est complète quand chaque objectif a au moins un KPI, quand un tiers
pourrait dire « au service de quel objectif ? » pour n'importe quelle dépense future,
et quand le décideur du go/no-go est nommé.

## Sortie

Tableau de synthèse clair + une phrase d'accroche résumant l'enjeu de l'événement.
Termine par la liste explicite des hypothèses retenues et des zones à confirmer.

Écris le tout dans `00-fiche-identite.md` (frontmatter conforme à la convention), en
initialisant la section **Journal des décisions**. Annonce le fichier écrit et sa version.

Propose ensuite d'enchaîner sur le rétroplanning (`event-retroplanning`) ou le budget
(`event-budget`).
