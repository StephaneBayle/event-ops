---
name: event-debrief
description: >
  À utiliser pour la phase APRÈS un événement : quand l'utilisateur demande un
  "débrief", un "bilan", un "retour d'expérience", un "AAR", un "after-action
  review", un "bilan KPIs" ou la "clôture" d'un événement. Transforme l'événement
  en actif réutilisable : clôture logistique, bilan KPIs vs objectifs, et débrief
  structuré.
version: 0.4.1
---

# Débrief & capitalisation

Tu clos l'événement et tu en fais un actif pour les prochains. C'est cette phase
qui fait la différence entre « on a survécu » et « on s'améliore ».

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis tous les fichiers présents — le débrief confronte le réalisé au prévu, il lui
faut donc le prévu. Le **Journal des décisions** de `00-fiche-identite.md` est ta
matière première : il dit pourquoi les arbitrages ont été pris.
Écris `07-debrief.md`.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : **tous ceux que tu as ouverts**, sans exception.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

## Méthode

1. **Clôture opérationnelle** : démontage / logistique retour, restitution
   matériel, relances et remerciements (prestataires, intervenants, partenaires),
   soldes budgétaires, **factures encore en attente**.
2. **Bilan KPIs vs objectifs** : reprends la fiche d'identité et confronte chaque
   KPI à sa cible. Écart chiffré + lecture courte de la cause.
3. **Bilan budgétaire** : budgété vs engagé vs réalisé par poste, en cohérence avec
   `02-budget.md`. Identifie les postes systématiquement sous-estimés — ce sont eux
   qui fausseront le prochain budget si on ne les note pas.
4. **Bilan de fréquentation** : taux de no-show réel vs hypothèse retenue dans
   `04-inscriptions.md`. C'est **la** donnée la plus précieuse à capitaliser : elle
   conditionne les garanties traiteur et donc l'engagement financier du prochain
   événement.
5. **After-Action Review** (4 questions, format militaire) :
   - Qu'attendait-on ? (l'intention)
   - Qu'est-il réellement arrivé ?
   - Pourquoi l'écart ?
   - Que garde-t-on / change-t-on pour la prochaine fois ?
6. **Risques survenus vs anticipés** : croise avec `06-risques.md`. Trois cas à
   nommer distinctement — risques anticipés qui sont survenus (le traitement a-t-il
   fonctionné ?), risques anticipés non survenus (sur-cotés ?), et surtout **incidents
   non anticipés** (l'angle mort à intégrer au prochain pre-mortem).
7. **Capitalisation** — section explicite « à réutiliser », structurée pour être lue
   par le `event-cadrage` du prochain événement :
   - Prestataires à retenir / à écarter, avec le motif.
   - Hypothèses vérifiées (no-show, ratios de consommation, temps de montage).
   - Postes budgétaires à corriger.
   - Risques à remonter dans la cotation.
   - Modèles et documents à ajuster.

## Sortie

Tableau KPIs (cible | réalisé | écart | cause) + bilan budgétaire + bilan
fréquentation + compte rendu AAR structuré + section « à réutiliser / à corriger ».

Pas de langue de bois : nomme les écarts. Un débrief qui ne fâche personne n'apprend
rien à personne.

Écris `07-debrief.md` et annonce sa version.
