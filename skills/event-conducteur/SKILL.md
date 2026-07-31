---
name: event-conducteur
description: >
  À utiliser pour la phase PENDANT d'un événement : quand l'utilisateur demande un
  "conducteur", un "run of show", un "minutage du jour J", un "déroulé", un "plan
  de salle", un "annuaire jour J", des "tops régie" ou des "procédures d'escalade".
  Produit la pièce maîtresse de l'exécution : séquencement minuté, tops régie,
  ressources, responsables, et plans de repli.
version: 0.3.0
---

# Conducteur jour J (run of show)

Tu produis l'instrument que l'equipe tient en main sous tension. C'est la partie
que la plupart des dossiers negligent et qui fait toute la difference.

## Methode

1. **Conducteur minute** : sequence par sequence, avec pour chaque creneau :
   heure de debut | action | responsable | ressources (technique, RH, materiel) |
   signal de transition vers la sequence suivante.
2. **Plan de salle** : zones, flux, points de controle d'acces.
3. **Annuaire jour J** : contacts operationnels (nom, role, telephone), regroupes
   par fonction.
4. **Procedures d'escalade** : pour chaque incident plausible, qui decide et selon
   quel seuil. Format clair "Si X alors Y, decideur = Z".
5. **PACE planning** pour chaque fonction vitale (son, acces, intervenant cle,
   electricite) : **P**rimary / **A**lternate / **C**ontingency / **E**mergency —
   quatre niveaux de repli. (Origine militaire, pertinent pour des publics
   exigeants en continuite.)
6. **Test du parcours-participant** : suis mentalement chaque persona (VIP,
   intervenant, presse, public) de l'arrivee au depart. Tout point de contact non
   couvert par le conducteur = un trou ; signale-le.

## Sortie

Conducteur en tableau chronologique + plan de salle (description ou schema) +
annuaire + table d'escalade + grille PACE des fonctions vitales.
