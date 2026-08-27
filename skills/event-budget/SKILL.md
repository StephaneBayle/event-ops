---
name: event-budget
description: >
  À utiliser pour construire et piloter le budget d'un événement : quand
  l'utilisateur demande un "budget", un "budget prévisionnel", un "suivi
  budgétaire", de "chiffrer un événement", parle d'"enveloppe", de "postes de
  dépense", de "HT ou TTC", de "reste à engager", de "dépassement" ou veut un
  "budget en Excel". Produit un budget structuré ligne à ligne avec suivi
  budgété / engagé / réalisé, gestion HT-TTC et provision pour aléas.
version: 0.4.0
---

# Budget événementiel

Un budget d'événement n'est pas une liste de grands postes : c'est un instrument de
pilotage à 40-80 lignes qu'on tient à jour de la première estimation au solde final.
La question n'est jamais « combien ça coûte » mais « combien on a déjà engagé, et
qu'est-ce qu'il me reste ».

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md` (enveloppe et objectifs), `03-prestataires.md` (montants
réellement négociés) et `04-inscriptions.md` (jauge et garantie traiteur) ; écris
`02-budget.md`.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : `00-fiche-identite.md`, `03-prestataires.md` et `04-inscriptions.md`.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

Si un poste dépasse son enveloppe, ne le lisse pas : nomme le dépassement, chiffre-le,
et propose des arbitrages.

## Règles non négociables

1. **HT ou TTC — jamais les deux sans le dire.** Chaque ligne porte son montant HT,
   son taux de TVA et son montant TTC. Le total est présenté dans les deux bases.
   Une confusion HT/TTC sur un budget à cinq chiffres est une faute lourde.
   - Taux courants en France : 20 % standard, 10 % restauration sur place et
     hébergement, 5,5 % alimentaire à emporter, 2,1 % / exonérations spécifiques.
     **Vérifie, ne présume pas** : le taux dépend de la prestation exacte.
   - Si l'organisation **récupère la TVA**, c'est le HT qui pilote. Sinon c'est le
     TTC. Pose la question au début — elle change toute la lecture du budget.
2. **Ne jamais inventer un montant.** Un prix inconnu est une estimation explicitement
   marquée comme telle, avec sa base (ratio, devis comparable, ordre de grandeur), ou
   une ligne vide « à chiffrer ». Un budget crédible faux est plus dangereux qu'un
   budget visiblement incomplet.
3. **Provision pour aléas obligatoire** : 5 à 10 % du total selon le niveau
   d'incertitude (10 % si le lieu ou le format n'est pas figé, 5 % si tout est
   contractualisé). Elle est une **ligne du budget**, pas un matelas caché dans les
   autres postes.

## Structure du budget

### Dépenses, par poste

Reprends les domaines de `${CLAUDE_PLUGIN_ROOT}/references/chantiers.md` comme
ossature — c'est ce qui garantit qu'aucune famille de dépense n'est oubliée.
Ordre de grandeur typique : lieu et technique dominent, la restauration surprend
toujours à la hausse, la signalétique et le staff sont systématiquement sous-estimés.

Colonnes :

| Poste | Ligne | Base de calcul | Qté | PU HT | **Total HT** | TVA | **Total TTC** | Budgété | **Engagé** | **Réalisé** | Reste à engager | Prestataire | Échéance de paiement | Statut |

- **Budgété** — l'estimation validée.
- **Engagé** — ce qui est contractuellement dû dès signature, même non payé. **C'est
  la colonne qui compte** : c'est elle qui dit ce qu'on perdrait en cas d'annulation.
- **Réalisé** — facturé et payé.
- **Base de calcul** — « 180 convives × 42 € », « forfait », « 3 jours × 2 techniciens ».
  Sans elle, personne ne peut refaire le calcul ni ajuster quand la jauge bouge.

### Recettes (si l'événement en a)

Billetterie, sponsors et partenariats, subventions, refacturation interne.
Distinguer **acquis / promis / espéré** — un sponsor « intéressé » n'est pas une recette.

### Synthèse

- Total dépenses HT / TTC.
- Total recettes.
- **Solde**, et si négatif : qui le couvre.
- Provision pour aléas et ce qu'il en reste.
- **Engagé cumulé à date** — le chiffre à mettre sous les yeux du décideur go/no-go.

## Liens avec les autres briques

- **Jauge** — la restauration, les badges, les cadeaux et parfois la sécurité sont
  proportionnels au nombre de présents. Utilise l'hypothèse de `04-inscriptions.md`,
  et surtout **la garantie traiteur, pas le nombre d'inscrits** : c'est le chiffre
  garanti qui est facturé.
- **Prestataires** — les montants négociés de `03-prestataires.md` remplacent les
  estimations. Signale les écarts estimation → devis, ils sont instructifs.
- **Go/no-go** — l'engagé cumulé et les acomptes non remboursables sont un critère
  de décision. Signale qu'il faut repasser `event-retroplanning` pour les intégrer
  au critère du jalon.
- **Risques** — un dépassement probable est un risque financier à coter dans
  `06-risques.md`.

## Sortie

Budget complet en tableau, synthèse par poste, et les 3 à 5 lignes à surveiller
(les plus incertaines ou les plus lourdes).

Écris `02-budget.md` et annonce la version.

**Sur demande — et propose-le systématiquement — génère `livrables/budget.xlsx`** :
un event manager travaille dans Excel, pas dans du markdown. Le fichier doit avoir
des **formules vivantes** (sous-totaux, TVA, écarts, reste à engager) et non des
valeurs figées, pour rester utilisable après ta sortie.
