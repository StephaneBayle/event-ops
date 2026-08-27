---
name: event-dossier
description: >
  Skill chapeau. À utiliser quand l'utilisateur veut "le dossier complet", "le
  dossier opérationnel complet", "tout assembler", "générer le document final" ou
  "produire le livrable" d'un événement. Assemble toutes les briques (cadrage,
  rétroplanning, budget, prestataires, inscriptions, conducteur, risques, débrief)
  et produit un jeu de livrables structuré et stylisé, prêt à partager avec une
  équipe.
version: 0.4.1
---

# Dossier opérationnel complet

Tu assembles l'ensemble en un jeu de livrables cohérent et soigné. Objectif : qu'un
tiers compétent puisse exécuter l'événement avec ces seuls documents (test de
l'étranger compétent).

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.

**Tu assembles depuis les fichiers, pas depuis la conversation.** Lis tous les
fichiers présents du dossier et construis les livrables à partir d'eux. Tu écris
uniquement dans `livrables/` — jamais dans les `.md` sources, qui appartiennent
aux autres briques.

**Pas de champ `lu:`** : les livrables ne portent pas de frontmatter. En revanche,
**fais figurer sur chaque livrable la version de chaque source utilisée**
(« généré depuis 00 v1, 02 v3, 05 v2 — le 12/09/2026 »). Une liasse imprimée qui ne dit
pas de quelles versions elle est tirée est inexploitable dès la première révision.

Pour toute brique dont le fichier manque, deux options : produire la section en
appliquant la méthode de la brique correspondante et **prévenir que la source
n'existe pas** (le résultat ne sera pas persisté par toi), ou proposer de lancer
la brique d'abord. Ne fabrique pas silencieusement du contenu qui aurait dû être
validé ailleurs.

## Méthode

1. **Ordre d'assemblage** :
   - Fiche d'identité — page d'ancrage.
   - AVANT : rétroplanning + go/no-go + RACI + checklists.
   - Moyens : budget, prestataires, inscriptions.
   - PENDANT : conducteur + plan de salle + escalade + PACE.
   - Transverse : cartographie des risques.
   - APRÈS : clôture + bilan KPIs + AAR.
2. **Tests de complétude** avant de finaliser. OUVRE et PARCOURS
   `${CLAUDE_PLUGIN_ROOT}/references/chantiers.md` plutôt que de te fier à ta
   mémoire ; applique **toutes** ses lentilles et son contrôle final. Signale tout
   manque restant plutôt que de le masquer.
3. **Contrôle mécanique d'abord** — lance
   `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/check_dossier.py <dossier>`. Il attrape en une
   seconde ce qu'une relecture ne voit pas : en-tête divergent, brique écrite sur une
   version périmée de ce dont elle dépend, livrable plus ancien que sa source. Reprends
   sa sortie telle quelle dans l'encadré final ; ne la paraphrase pas.
4. **Cohérence inter-fichiers** — ce que le script ne sait pas voir, parce que c'est du
   fond et non de la forme. Vérifie que les briques ne se contredisent pas :
   même jour J partout, jauge cohérente entre inscriptions / plan de salle /
   garanties traiteur, montants du budget cohérents avec les prestataires retenus,
   responsables du conducteur présents dans le RACI et dans l'annuaire. Toute
   divergence se signale, elle ne se lisse pas. **C'est le seul contrôle qui attrape une
   valeur devenue fausse sans que sa version ait bougé** — un cahier des charges qui porte
   encore l'ancien nombre de couverts, par exemple.

## Sortie — jeu de livrables

Un seul HTML monolithique ne couvre aucun usage terrain correctement. Produis dans
`livrables/` :

| Fichier | Usage | Format |
|---|---|---|
| `dossier.html` | Le dossier complet à diffuser | HTML autonome, imprimable, navigable par ancres, table des matières |
| `conducteur-a4.html` | **Pour la régie et l'équipe, en main le jour J** | A4 **paysage**, `@media print` propre, gros corps de texte, numéro de version en en-tête et en pied de chaque page |
| `annuaire.html` | Contacts d'urgence, consulté sur téléphone | Une colonne, lisible sur mobile, numéros cliquables (`tel:`) |
| `checklists.html` | À imprimer et cocher | Cases à cocher réelles, une page par jalon |
| `budget.xlsx` | **Non négociable** — l'event manager travaille dans Excel | Généré depuis `02-budget.md`, formules de sous-totaux vivantes |

Sur demande : version **.docx** du dossier complet.

Soigne la hiérarchie visuelle et la lisibilité ; évite le rendu « template générique ».
Les documents destinés au jour J priment sur l'esthétique du dossier : ils se lisent
sous tension, dans une salle mal éclairée, par quelqu'un qui cherche une information
en trois secondes.

Termine par un encadré **« Points à vérifier avant diffusion »** listant les hypothèses
restantes, les champs « à compléter » (contacts, montants) et les incohérences
inter-fichiers détectées.
