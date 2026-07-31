# Event-ops Plugin

Plugin Claude pour la gestion d'événements et la production de dossiers opérationnels.

## Structure

- `skills/` — Six skills Claude auto-suffisantes :
  - `event-cadrage/` — Cadrage et objectives
  - `event-retroplanning/` — Rétroplanning et RACI
  - `event-conducteur/` — Conducteur et plan de salle
  - `event-risques/` — Cartographie risques et pre-mortem
  - `event-debrief/` — After-Action Review et bilan
  - `event-dossier/` — Assemblage du dossier complet

- `.claude/` — Configuration Claude Code
- `references/` — Matériel de référence et chantiers

## Développement

Pour tester le plugin localement :

```bash
# En développement, le plugin s'installe via Claude Code UI
```

## Slash commands

```
/event-ops:event-cadrage      # Cadrage
/event-ops:event-retroplanning # Rétroplanning  
/event-ops:event-conducteur    # Conducteur
/event-ops:event-risques       # Risques
/event-ops:event-debrief       # Débrief
/event-ops:event-dossier       # Dossier complet
```

## Notes de cadre

Ce plugin produit des livrables pédagogiques et opérationnels. Tous les scénarios, cas et données sont fictifs. Aucune donnée classifiée, ordre de bataille réel, ou information sensible n'est embarquée.
