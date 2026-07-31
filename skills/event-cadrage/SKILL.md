---
name: event-cadrage
description: >
  Point d'entree d'un dossier evenementiel. A utiliser quand l'utilisateur veut
  "lancer un nouvel evenement", "cadrer un evenement", "definir les objectifs d'un
  evenement", "demarrer le dossier operationnel", ou fournit le nom/format d'un
  evenement sans cadre encore pose. Produit la FICHE D'IDENTITE : objectifs
  mesurables, KPIs, public cible, format, budget, gouvernance. C'est l'ancre dont
  toutes les autres briques dependent.
version: 0.1.0
---

# Cadrage d'evenement — Fiche d'identite

Tu produis l'invariant du dossier : le "pourquoi" et le cadre. Tout le reste
(retroplanning, conducteur, risques) devra pouvoir s'y rattacher.

## Methode

1. **Avant de rediger, nomme les hypotheses implicites** sur le type, l'echelle
   et l'intention de l'evenement, et signale ce qui manque.
2. Si des informations cles sont absentes, pose AU PLUS 3 questions ciblees
   (idealement via boutons / choix). Ne bloque pas : propose des valeurs par
   defaut explicitement marquees comme hypotheses.
3. Construis la fiche autour de ces rubriques :
   - **Objectif(s)** — formules de maniere mesurable (verbe + cible + echeance).
   - **KPIs** — 3 a 5 indicateurs, chacun rattache a un objectif, avec valeur cible.
   - **Public cible** — segments (ex. VIP, intervenants, presse, grand public),
     volume estime par segment.
   - **Format & cadre** — date(s), lieu, duree, jauge, format (conference, salon,
     soiree, tournoi...).
   - **Budget** — enveloppe globale + grands postes (lieu, technique, restauration,
     com'). Ordre de grandeur si non connu, marque comme estimation.
   - **Gouvernance** — qui decide quoi, instance d'arbitrage, sponsor.

## Test de qualite

La fiche est complete quand chaque objectif a au moins un KPI, et quand un tiers
pourrait dire "au service de quel objectif ?" pour n'importe quelle depense future.

## Sortie

Tableau de synthese clair + une phrase d'accroche resumant l'enjeu de l'evenement.
Propose ensuite d'enchainer sur le retroplanning (skill event-retroplanning).
