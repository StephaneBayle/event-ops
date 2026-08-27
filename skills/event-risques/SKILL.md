---
name: event-risques
description: >
  À utiliser pour analyser les risques d'un événement : quand l'utilisateur demande
  une "cartographie des risques", une "matrice des risques", un "pre-mortem", un
  "plan de traitement" ou de "coter les risques" d'un événement. Brique autonome
  (n'appelle aucune skill externe) calibrée pour l'événementiel : no-show
  intervenant, panne technique, météo, sûreté du public, dépassement budgétaire.
version: 0.5.0
---

# Cartographie des risques événementiels

Brique auto-suffisante. Tu évalues et traites les risques propres à un événement,
sans dépendre d'aucun outil installé ailleurs.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis tous les fichiers présents du dossier — le registre des risques se nourrit de
tout : engagements budgétaires, prestataires uniques, jauge, conducteur.
Écris `06-risques.md`.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : **tous ceux que tu as ouverts**, sans exception.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

## Méthode

1. **Pre-mortem** (Gary Klein) : « On est le lendemain, c'est un fiasco — qu'est-ce
   qui a foiré ? » Fais cet exercice **AVANT** la cotation ; il révèle les angles morts
   mieux qu'une revue classique, qui ne fait qu'ancrer sur les risques déjà listés.
2. **Identification** par familles typiques de l'événementiel : technique (son,
   vidéo, réseau, électricité), humain (no-show intervenant, sous-effectif
   bénévoles), logistique (livraison, transport, accès), sûreté & sécurité (foule,
   incident médical, évacuation), météo (si extérieur), réputationnel/com',
   financier (dépassement, défaut prestataire), juridique (assurance, droit à
   l'image, conformité, défaut d'accessibilité), fréquentation (sous-remplissage
   comme sur-affluence). Pour la famille juridique, parcours
   `${CLAUDE_PLUGIN_ROOT}/references/conformite.md` : un régime au statut « à vérifier »
   à quelques semaines du jour J est un risque coté, pas une tâche en retard — et son
   impact est souvent l'impossibilité d'ouvrir.
3. **Risques de dépendance** — repère les points uniques de défaillance : un
   prestataire sans doublure, un intervenant dont dépend tout le programme, une
   seule source d'alimentation. Ce sont eux qui transforment un incident en fiasco.
   Croise avec `03-prestataires.md` s'il existe.
4. **Cotation Probabilité × Impact** sur échelles 1-4 (ou 1-5), criticité =
   P × I. Classe en faible / moyen / élevé / critique.
5. **Traitement (4 T)** pour chaque risque significatif :
   **T**erminer (éviter / supprimer la cause), **T**raiter (réduire P ou I),
   **T**ransférer (assurance, prestataire), **T**olérer (accepter + surveiller).
   Associe un responsable et un déclencheur de plan d'action.
6. **Raccordement au go/no-go** — parmi les risques critiques, identifie ceux qui
   doivent alimenter le critère de décision d'annulation du rétroplanning. Un risque
   critique sans lien avec le go/no-go est soit mal coté, soit orphelin.

## Sortie

Registre des risques : id | description | famille | P | I | criticité | stratégie
4T | action | responsable | déclencheur. Plus une matrice P × I visuelle si le
format le permet. Termine par les 3 à 5 risques critiques à surveiller en priorité.

Écris `06-risques.md` et annonce sa version.
