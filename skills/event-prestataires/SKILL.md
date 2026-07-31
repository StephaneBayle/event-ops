---
name: event-prestataires
description: >
  À utiliser pour tout ce qui touche aux fournisseurs d'un événement : quand
  l'utilisateur demande un "cahier des charges", un "appel d'offres", de "comparer
  des devis", une "grille comparative", un "briefing prestataire", un "brief
  traiteur", de "choisir un prestataire", ou parle de traiteur, technicien son,
  sécurité, mobilier, signalétique, photographe, agence. Couvre la chaîne complète :
  sourcing, cahier des charges, comparaison de devis, contractualisation, briefing,
  réception de prestation.
version: 0.3.0
---

# Prestataires — du cahier des charges à la réception

C'est là que passe l'essentiel du temps d'un event manager, et l'essentiel du budget.
Un dossier qui traite les prestataires en une ligne (« traiteur : à trouver ») n'est
pas un dossier opérationnel.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md` et `02-budget.md` s'ils existent ; écris `03-prestataires.md`.

Les montants que tu inscris ici doivent rester cohérents avec le budget. Si tu retiens
un devis qui fait sortir un poste de son enveloppe, dis-le et propose de reprendre
`event-budget`.

## Méthode

Selon ce que demande l'utilisateur, tu interviens à une ou plusieurs étapes. Ne déroule
pas tout systématiquement — situe d'abord où on en est.

### 1. Cadrer le besoin (cahier des charges)

Pour chaque lot de prestation, produire un CDC court et attaquable :

- **Objet et périmètre** — ce qui est inclus, et surtout **ce qui ne l'est pas**
  (la source n°1 de litige).
- **Contraintes du lieu** — accès, horaires de livraison, monte-charge, puissance
  électrique disponible, nuisances sonores, contraintes ERP.
- **Volumétrie** — nombre de convives, de places, de mètres linéaires. Indiquer
  explicitement si le chiffre est ferme ou une fourchette, et à quelle date il
  deviendra ferme.
- **Créneaux** — montage, exploitation, démontage, avec les heures.
- **Exigences de service** — qualifications, effectif sur site, langue, tenue.
- **Livrables attendus** et critères de réception.
- **Format de réponse imposé** — c'est ce qui rend les devis comparables. Sans lui,
  chaque prestataire découpe son offre à sa façon et la comparaison est impossible.

### 2. Comparer les devis

Le livrable que la direction ou le client réclame. Grille systématique :

| Critère | Prestataire A | B | C |
|---|---|---|---|
| Prix **HT** | | | |
| TVA (taux) | | | |
| Prix **TTC** | | | |
| Périmètre couvert / écarts au CDC | | | |
| **Ce qui n'est pas inclus** | | | |
| Options chiffrées | | | |
| Conditions de paiement (acompte, solde) | | | |
| **Conditions et date limite d'annulation** | | | |
| Assurance / RC pro | | | |
| Références comparables | | | |
| Effectif et encadrement sur site | | | |
| Délai de réponse / réactivité constatée | | | |

Règles :

- **Ne compare jamais un HT avec un TTC.** Ramène tout à la même base et dis
  laquelle. Sur un budget événementiel, la confusion HT/TTC est une faute lourde.
- **Reconstitue le périmètre manquant.** Un devis moins cher qui exclut la livraison,
  le montage ou le personnel n'est pas moins cher : chiffre l'écart et compare à
  périmètre égal. C'est le cœur du travail de comparaison.
- **La date limite d'annulation sans frais** de chaque prestataire alimente le jalon
  go/no-go du rétroplanning. Remonte-la explicitement.
- N'invente aucun prix, aucun nom de société, aucune référence. Les cases inconnues
  restent vides et marquées « à obtenir ».

Termine par une **recommandation argumentée**, pas seulement un tableau : quel
prestataire, pourquoi, et quel est le risque résiduel du choix.

### 3. Contractualiser

Points à ne pas laisser au téléphone : périmètre annexé au contrat, montant et
échéancier (acompte / solde), pénalités de retard, conditions d'annulation des deux
côtés, assurance, sous-traitance autorisée ou non, droit à l'image si captation,
clause RGPD si données personnelles échangées.

Signale ce qui relève d'une validation juridique humaine — tu prépares, tu ne valides pas.

### 4. Briefer

La fiche de briefing est ce qu'on envoie au prestataire **avant** le jour J. Une par
prestataire, tenant sur une page :

- Rappel du périmètre commandé.
- Adresse précise, point de livraison, contact sur place avec téléphone.
- Créneaux horaires fermes (montage / service / démontage).
- Interlocuteur unique côté organisateur, et son suppléant.
- Extrait du conducteur qui le concerne — **uniquement ses séquences**, pas le
  conducteur entier.
- Consignes spécifiques : tenue, badges, parking, accès PMR, contraintes de bruit.
- Que faire en cas de problème : qui appeler, à quel seuil.

### 5. Réceptionner

Le jour J et après : conformité au CDC, écarts constatés, incidents, validation du
service fait avant paiement du solde, éléments à retenir pour le débrief (à faire
remonter dans la section « à réutiliser » de `07-debrief.md`).

## Points de vigilance

- **Prestataire unique sans doublure** = point de défaillance unique. Signale-le et
  fais-le remonter dans `06-risques.md`.
- **Acomptes versés** : ils transforment un no-go en perte sèche. Leur montant cumulé
  et leur date doivent être visibles dans le budget et peser dans le go/no-go.
- **Sous-traitance en cascade** : le prestataire que tu as choisi n'est pas toujours
  celui qui viendra. À clarifier avant signature.

## Sortie

Selon l'étape : cahier des charges, grille comparative + recommandation, points de
contractualisation, fiches de briefing, ou compte rendu de réception.

Écris `03-prestataires.md` — un tableau de suivi consolidé (lot | prestataire retenu |
montant HT/TTC | acompte versé | date limite d'annulation | statut) plus le détail par
lot. Annonce la version.
