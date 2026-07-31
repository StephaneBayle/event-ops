---
name: event-inscriptions
description: >
  À utiliser pour tout ce qui concerne le public d'un événement : quand
  l'utilisateur parle d'"inscriptions", de "billetterie", d'"invitations", de
  "jauge", de "remplissage", de "no-show", de "relances", de "liste d'attente",
  d'"accréditations", de "badges", de "check-in" ou d'"émargement". Pilote
  l'entonnoir invités → inscrits → confirmés → présents, les hypothèses de
  no-show et les garanties à donner au traiteur.
version: 0.3.0
---

# Inscriptions, jauge & accueil

La jauge n'est pas un nombre, c'est un entonnoir qui se pilote dans le temps. Et
c'est un entonnoir qui coûte : le chiffre que tu garantis au traiteur est facturé,
qu'il vienne 200 personnes ou 120.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md` (segments de public, jauge cible) ; écris
`04-inscriptions.md`.

Si un dossier d'événement passé est accessible, **va chercher son taux de no-show
réel** dans la section « à réutiliser » de son débrief : une donnée observée sur un
public comparable vaut infiniment mieux qu'une fourchette générique.

## L'entonnoir

| Étape | Définition | À quoi ça sert |
|---|---|---|
| **Cible** | Jauge visée | Objectif du cadrage |
| **Touchés** | Invitations envoyées / audience de la com' | Mesure l'effort de recrutement |
| **Inscrits** | Ont rempli le formulaire | Indicateur avancé |
| **Confirmés** | Ont reconfirmé après relance | Base de la garantie traiteur |
| **Présents** | Ont émargé sur place | Le réel — à capitaliser |

Chaque étape a un taux de conversion. Les suivre dans le temps permet de **détecter
un sous-remplissage assez tôt pour réagir** — relancer, ouvrir à un autre public,
ou déclencher le no-go.

## Hypothèses de no-show

Le chiffre le plus structurant du dossier, et le plus mal estimé.

Ordres de grandeur — **à traiter comme point de départ, pas comme vérité** :

| Contexte | No-show typique |
|---|---|
| Gratuit, inscription en ligne, grand public | 30 à 50 % |
| Gratuit, public professionnel invité | 20 à 35 % |
| Payant | 5 à 10 % |
| Interne obligatoire / séminaire d'entreprise | 5 à 15 % |
| Soirée de gala avec placement nominatif | 3 à 8 % |

Facteurs aggravants à signaler : événement en soirée, météo défavorable annoncée,
grève de transports, lundi ou vendredi, période de vacances scolaires, inscription
ouverte très en amont (plus le délai est long, plus le no-show monte).

**Marque toujours l'hypothèse retenue comme hypothèse**, avec sa justification.
Et note-la de façon à pouvoir la confronter au réel dans le débrief — c'est ainsi
qu'on arrête de deviner au bout de trois éditions.

## Garanties et engagement financier

C'est le point où l'entonnoir devient de l'argent.

- Le traiteur demande un **nombre garanti**, généralement à J-3 ou J-7, facturé même
  si moins de monde vient. Repère cette date : c'est un jalon du rétroplanning.
- Garantir au niveau des **confirmés diminués du no-show attendu**, pas au niveau des
  inscrits. Et prévoir la marge de sécurité à la hausse que permet le contrat
  (beaucoup de traiteurs acceptent +5 à +10 % à J-1, jamais à la baisse).
- Le sur-remplissage a aussi un coût et un risque : au-delà de la jauge ERP autorisée,
  c'est un problème de sécurité, pas de confort. Fixe un plafond ferme et une liste
  d'attente.

Fais remonter le nombre garanti et sa date dans `02-budget.md` et le jalon dans
`01-retroplanning.md`.

## Dispositif d'inscription

- **Segments et tarifs** — qui s'inscrit comment (VIP sur invitation nominative,
  presse sur accréditation, public sur formulaire ouvert). Chaque segment a son
  circuit et son badge.
- **Données collectées** — le strict nécessaire. Chaque champ demandé fait chuter le
  taux de complétion. Attention **RGPD** : finalité, durée de conservation, base
  légale, mention d'information. Les régimes alimentaires et besoins d'accessibilité
  sont des données sensibles à traiter comme telles.
- **Accessibilité** — le formulaire doit permettre de signaler un besoin PMR, un
  accompagnateur, un besoin d'interprétation. Sans la question, l'information
  n'arrive jamais, et le jour J il est trop tard.
- **Séquence de relances** — confirmation immédiate, rappel à J-7, rappel à J-1 avec
  les informations pratiques (accès, horaire, plan). La relance J-1 est celle qui
  réduit le plus le no-show.
- **Liste d'attente** — à ouvrir dès que le taux d'inscription dépasse la jauge
  moins le no-show attendu.

## Jour J — check-in

- Dispositif d'émargement (nominatif, QR code, liste papier de secours — **toujours
  une liste papier de secours**, le réseau tombe).
- Nombre de postes d'accueil dimensionné sur le **pic d'arrivée**, pas sur le total :
  60 à 70 % du public arrive dans les 30 minutes précédant l'ouverture.
- Circuit séparé pour les VIP, la presse et les intervenants.
- Gestion des non-inscrits qui se présentent : politique décidée à l'avance, pas
  improvisée à la porte.
- Comptage en temps réel — c'est la donnée du débrief.

## Sortie

Tableau de l'entonnoir avec état à date et projection, hypothèse de no-show
justifiée, calendrier des relances, dispositif de check-in dimensionné, et le
nombre à garantir au traiteur avec sa date butoir.

Écris `04-inscriptions.md` et annonce la version.
