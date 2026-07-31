# Convention du dossier événement

Source de vérité unique du plugin `event-ops` pour la **persistance**. Toutes les skills
lisent et écrivent selon cette convention. Un dossier événementiel vit **3 à 6 mois** et
traverse des dizaines de sessions : l'état ne doit jamais vivre uniquement dans la
conversation.

---

## Règle d'or

> **Lire l'état du dossier AVANT de produire. Écrire le résultat APRÈS l'avoir produit.**

Une skill qui produit sans avoir lu invente un contexte qui existe peut-être déjà sur
disque, et contredit les autres briques. Une skill qui produit sans écrire perd son
travail à la fin de la session.

---

## Localiser le dossier

Dans l'ordre :

1. L'utilisateur a désigné un dossier explicitement → l'utiliser.
2. Un dossier contenant `00-fiche-identite.md` existe dans le répertoire courant ou juste
   en dessous → l'utiliser, et le signaler (« je reprends le dossier *X* »).
3. Sinon → proposer d'en créer un : `./<slug-evenement>/`, slug en minuscules sans accents
   (ex. `convention-annuelle-2026`). **Ne jamais créer sans le dire.**

Si plusieurs dossiers candidats existent, demander lequel plutôt que de deviner.

## Arborescence

```
<dossier-evenement>/
├── 00-fiche-identite.md     ← event-cadrage       (ancre)
├── 01-retroplanning.md      ← event-retroplanning (avant)
├── 02-budget.md             ← event-budget        (transverse)
├── 03-prestataires.md       ← event-prestataires  (avant/pendant)
├── 04-inscriptions.md       ← event-inscriptions  (avant/pendant)
├── 05-conducteur.md         ← event-conducteur    (pendant)
├── 06-risques.md            ← event-risques       (transverse)
├── 07-debrief.md            ← event-debrief       (après)
└── livrables/               ← event-dossier       (généré, jamais édité à la main)
    ├── dossier.html
    ├── conducteur-a4.html
    ├── budget.xlsx
    └── annuaire.html
```

Chaque fichier appartient à **une seule** skill. Une skill ne réécrit jamais le fichier
d'une autre : si elle a besoin d'y changer quelque chose, elle le signale à l'utilisateur.

`livrables/` est **généré**. Tout y est écrasable sans perte — la vérité est dans les `.md`.

## En-tête de fichier (frontmatter)

Tout fichier du dossier commence par :

```yaml
---
evenement: Convention annuelle 2026
jour_j: 2026-11-14
brique: conducteur
version: 3
maj: 2026-07-31
---
```

- `evenement` / `jour_j` — recopiés depuis `00-fiche-identite.md`. S'ils divergent, la
  fiche d'identité fait foi ; signaler la divergence.
- `version` — entier, **incrémenté à chaque réécriture**. Critique pour le conducteur :
  l'équipe doit savoir quelle version elle tient en main le jour J.
- `maj` — date de dernière modification.

## Lire l'état du dossier

Au démarrage, toute skill :

1. Liste les fichiers présents.
2. Lit **au minimum `00-fiche-identite.md`** (l'ancre) s'il existe.
3. Lit les fichiers dont elle dépend (voir tableau ci-dessous).
4. Annonce en une ligne ce qu'elle a trouvé et ce qui manque.
   *Ex. « Dossier trouvé : fiche d'identité (v2), rétroplanning (v1). Pas encore de budget
   ni de conducteur. »*

| Skill | Lit | Écrit |
|---|---|---|
| `event-cadrage` | — | `00-fiche-identite.md` |
| `event-retroplanning` | `00` | `01-retroplanning.md` |
| `event-budget` | `00`, `03` | `02-budget.md` |
| `event-prestataires` | `00`, `02` | `03-prestataires.md` |
| `event-inscriptions` | `00` | `04-inscriptions.md` |
| `event-conducteur` | `00`, `01`, `03`, `04` | `05-conducteur.md` |
| `event-risques` | tous ceux présents | `06-risques.md` |
| `event-debrief` | tous ceux présents | `07-debrief.md` |
| `event-dossier` | **tous** | `livrables/*` |

Une dépendance absente n'est **jamais bloquante** : produire quand même, en marquant
explicitement l'hypothèse retenue et en proposant la brique manquante.

## Écrire

- **Compléter, ne pas écraser.** Si le fichier existe, en reprendre le contenu, appliquer
  la modification demandée, et conserver le reste. Ne jamais repartir d'une page blanche
  sans le dire.
- **Incrémenter `version`** et mettre `maj` à la date du jour.
- **Ne jamais supprimer une donnée saisie par un humain** (un nom de contact, un montant
  négocié, une contrainte du lieu) sans confirmation explicite.
- En fin d'écriture, annoncer le fichier touché et sa nouvelle version.

## Journal des décisions

`00-fiche-identite.md` se termine par une section **Journal des décisions** :

| Date | Décision | Qui | Impact |
|---|---|---|---|

Y consigner les arbitrages structurants (changement de lieu, de date, de jauge, coupe
budgétaire, go/no-go). C'est ce qui permet, trois mois plus tard, de répondre à
« pourquoi on a fait ça déjà ? » — et c'est la matière première du débrief.

## Capitalisation entre événements

Un dossier clôturé devient un **modèle pour le suivant**. `event-debrief` écrit une
section « à réutiliser » dans `07-debrief.md` : prestataires à retenir ou à écarter,
hypothèses de no-show vérifiées, postes budgétaires sous-estimés, risques survenus.

Au démarrage d'un nouvel événement, `event-cadrage` propose de s'appuyer sur un dossier
passé s'il en repère un. C'est la seule manière de tenir la promesse de capitalisation :
sans persistance, chaque événement repart de zéro.
