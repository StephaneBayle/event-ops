---
name: event-dossier
description: >
  Skill chapeau. À utiliser quand l'utilisateur veut "le dossier complet", "le
  dossier opérationnel complet", "tout assembler", "générer le document final" ou
  "produire le livrable" d'un événement. Assemble toutes les briques (cadrage,
  rétroplanning, budget, prestataires, inscriptions, conducteur, risques, débrief)
  et produit un jeu de livrables structuré et stylisé, prêt à partager avec une
  équipe.
version: 0.3.0
---

# Dossier operationnel complet

Tu assembles l'ensemble en un livrable coherent et soigne. Objectif : qu'un tiers
competent puisse executer l'evenement avec ce seul document (test de l'etranger
competent).

## Methode

1. **Sequence de production**, dans l'ordre :
   - Fiche d'identite (logique de event-cadrage).
   - AVANT : retroplanning + RACI + checklists (logique de event-retroplanning).
   - PENDANT : conducteur + plan de salle + escalade + PACE (event-conducteur).
   - Risques : cartographie + traitement 4T (event-risques).
   - APRES : cloture + bilan KPIs + AAR (event-debrief).
   Reutilise la methode de chaque brique ; ne redemande pas ce qui est deja connu.
2. **Tests de completude** avant de finaliser. Pour le test de taxonomie, OUVRE
   et PARCOURS `${CLAUDE_PLUGIN_ROOT}/references/chantiers.md` plutot que de te
   fier a ta memoire ; applique ses 6 lentilles et son controle final :
   - Taxonomie : les 13 domaines parcourus (adresses ou "sans objet" justifie) ?
   - Temps x chantier : chaque domaine retenu present en avant / pendant / apres ?
   - Flux : personnes, biens, energie, argent traces de bout en bout ?
   - Orphelins de RACI : aucune tache sans Responsable assigne ?
   - Parcours : chaque persona a-t-il un chemin sans trou ?
   - Etranger competent : ce document suffit-il a executer sans te poser de question ?
   Signale tout manque restant plutot que de le masquer.

## Sortie — livrable stylise

Genere un document final **production-ready**, pas un brouillon :
- Format par defaut : **fichier HTML autonome** (single-file, imprimable,
  navigable par ancres), sobre et soigne — table des matieres, sections
  numerotees AVANT / PENDANT / APRES, tableaux propres.
- Sur demande : version **.docx** equivalente.
- Soigne la hierarchie visuelle et la lisibilite ; evite le rendu "template
  generique". Place la fiche d'identite en tete comme page d'ancrage.

Termine par un encadre "Points a verifier avant diffusion" listant les hypotheses
restantes et les zones a confirmer par un humain.
