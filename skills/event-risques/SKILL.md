---
name: event-risques
description: >
  A utiliser pour analyser les risques d'un evenement : quand l'utilisateur demande
  une "cartographie des risques", une "matrice des risques", un "pre-mortem", un
  "plan de traitement" ou de "coter les risques" d'un evenement. Brique autonome
  (n'appelle aucune skill externe) calibree pour l'evenementiel : no-show
  intervenant, panne technique, meteo, surete du public, depassement budgetaire.
version: 0.1.0
---

# Cartographie des risques evenementiels

Brique auto-suffisante. Tu evalues et traites les risques propres a un evenement,
sans dependre d'aucun outil installe ailleurs.

## Methode

1. **Identification** par familles typiques de l'evenementiel : technique (son,
   video, reseau, electricite), humain (no-show intervenant, sous-effectif
   benevoles), logistique (livraison, transport, acces), surete & securite (foule,
   incident medical, evacuation), meteo (si exterieur), reputationnel/com',
   financier (depassement, defaut prestataire), juridique (assurance, droit a
   l'image, conformite).
2. **Pre-mortem** (Gary Klein) : "On est le lendemain, c'est un fiasco — qu'est-ce
   qui a foire ?" Fais cet exercice AVANT la cotation ; il revele les angles morts
   mieux qu'une revue classique.
3. **Cotation Probabilite x Impact** sur echelles 1-4 (ou 1-5), criticite =
   P x I. Classe en faible / moyen / eleve / critique.
4. **Traitement (4 T)** pour chaque risque significatif :
   **T**erminer (eviter / supprimer la cause), **T**raiter (reduire P ou I),
   **T**ransferer (assurance, prestataire), **T**olerer (accepter + surveiller).
   Associe un responsable et un declencheur de plan d'action.

## Sortie

Registre des risques : id | description | famille | P | I | criticite | strategie
4T | action | responsable | declencheur. Plus une matrice P x I visuelle si le
format le permet. Termine par les 3 a 5 risques critiques a surveiller en priorite.
