---
name: event-retroplanning
description: >
  À utiliser pour la phase AVANT d'un événement : quand l'utilisateur demande un
  "rétroplanning", un "planning à rebours", "qui fait quoi", une "matrice RACI",
  un "chemin critique", un "go/no-go", ou des "checklists J-30 / J-7 / J-1".
  Produit le plan de préparation : rétroplanning construit à rebours depuis le
  jour J, matrice RACI par chantier, jalon de décision go/no-go, et checklists
  jalonnées.
version: 0.4.0
---

# Rétroplanning, RACI & checklists

Tu organises la préparation. Le piège à éviter : une liste de tâches sans colonne
vertébrale décisionnelle. On le corrige avec le chemin critique + le RACI.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md` (l'ancre) avant de produire, écris `01-retroplanning.md` après.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : `00-fiche-identite.md`.
Respecte la forme **bloc** de la convention — `lu:` seul sur sa ligne, puis une ligne
indentée par dépendance. Une écriture sur une seule ligne n'est pas relue par
`scripts/check_dossier.py` : le contrôle de péremption disparaît alors sans un mot.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

## Méthode

1. **Rappelle l'ancre** : rattache le plan aux objectifs de la fiche d'identité.
   Si elle n'existe pas, signale l'hypothèse de date/jour J retenue et propose
   `event-cadrage`.
2. **Rétroplanning à rebours** : pars du jour J et remonte. Identifie le **chemin
   critique** (la chaîne de tâches dont tout retard repousse l'événement) et
   distingue-le des tâches à flottement.
3. **Jalon go / no-go** — place explicitement le ou les points de décision
   « on y va / on annule / on reporte ». Pour chacun :

   | Date butoir | Critère de décision | Décideur | Conséquence si no-go |
   |---|---|---|---|

   Fixe la date butoir sur la **dernière échéance d'annulation sans frais** des
   engagements lourds (lieu, traiteur, prestation technique) — c'est elle qui commande,
   pas le confort de l'équipe. Le décideur est celui nommé dans la gouvernance de la
   fiche d'identité ; s'il n'y en a pas, c'est un trou : signale-le.
4. **Chantiers fonctionnels** — OUVRE et PARCOURS le fichier de référence
   `${CLAUDE_PLUGIN_ROOT}/references/chantiers.md`. Ne le résume pas de mémoire :
   passe ses domaines un par un, et pour chacun, soit tu l'adresses dans le
   plan, soit tu le marques explicitement « sans objet ». Applique aussi sa grille
   temps × chantier (chaque domaine retenu doit exister en avant / pendant /
   après). Tout chantier ou toute phase non traité = un trou ; signale-le
   explicitement en sortie.
5. **Délais incompressibles** — repère les tâches dont le délai ne se comprime pas
   quel que soit l'effort : autorisations administratives, commissions de sécurité ERP,
   fabrication de signalétique, envoi des invitations (délai de réponse), visas
   d'intervenants étrangers. Elles doivent être sur le chemin critique.
6. **Matrice RACI** par chantier : Responsable (fait) / Approbateur (valide) /
   Consulté / Informé. Une seule lettre A par ligne. Élimine les « je croyais que
   c'était toi ».
7. **Checklists jalonnées** : J-30, J-7, J-1, avec cases à cocher et responsable.

## Sortie

- Tableau rétroplanning (tâche | échéance | responsable | dépend de | critique ?).
- Table des jalons go/no-go.
- Matrice RACI (chantier × rôles).
- Trois checklists jalonnées.

Marque toute date/responsable supposé comme hypothèse. Écris `01-retroplanning.md` et
annonce sa version.

Propose d'enchaîner sur le budget (`event-budget`), les prestataires
(`event-prestataires`) ou la cartographie des risques (`event-risques`).
