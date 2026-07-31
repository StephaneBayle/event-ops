---
name: event-retroplanning
description: >
  À utiliser pour la phase AVANT d'un événement : quand l'utilisateur demande un
  "rétroplanning", un "planning à rebours", "qui fait quoi", une "matrice RACI",
  un "chemin critique", un "go/no-go", ou des "checklists J-30 / J-7 / J-1".
  Produit le plan de préparation : rétroplanning construit à rebours depuis le
  jour J, matrice RACI par chantier, jalon de décision go/no-go, et checklists
  jalonnées.
version: 0.3.0
---

# Retroplanning, RACI & checklists

Tu organises la preparation. Le piege a eviter : une liste de taches sans colonne
vertebrale decisionnelle. On le corrige avec le chemin critique + le RACI.

## Methode

1. **Rappelle l'ancre** : si une fiche d'identite (event-cadrage) existe, rattache
   le plan a ses objectifs. Sinon, signale l'hypothese de date/jour J retenue.
2. **Retroplanning a rebours** : pars du jour J et remonte. Identifie le **chemin
   critique** (la chaine de taches dont tout retard repousse l'evenement) et
   distingue-le des taches a flottement.
3. **Chantiers fonctionnels** — OUVRE et PARCOURS le fichier de reference
   `${CLAUDE_PLUGIN_ROOT}/references/chantiers.md`. Ne le resume pas de memoire :
   passe ses 13 domaines un par un, et pour chacun, soit tu l'adresses dans le
   plan, soit tu le marques explicitement "sans objet". Applique aussi sa grille
   temps x chantier (chaque domaine retenu doit exister en avant / pendant /
   apres). Tout chantier ou toute phase non traite = un trou ; signale-le
   explicitement en sortie.
4. **Matrice RACI** par chantier : Responsable (fait) / Approbateur (valide) /
   Consulte / Informe. Une seule lettre A par ligne. Elimine les "je croyais que
   c'etait toi".
5. **Checklists jalonnees** : J-30, J-7, J-1, avec cases a cocher et responsable.

## Sortie

- Tableau retroplanning (tache | echeance | responsable | depend de | critique ?).
- Matrice RACI (chantier x roles).
- Trois checklists jalonnees.

Marque toute date/responsable suppose comme hypothese. Propose d'enchainer sur le
conducteur (event-conducteur) et la cartographie des risques (event-risques).
