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
├── 08-conformite.md         ← event-conformite    (transverse)
└── livrables/               ← event-dossier       (généré, jamais édité à la main)
    ├── dossier.html
    ├── conducteur-a4.html
    ├── checklists.html
    ├── budget.xlsx
    └── annuaire.html
```

L'index est un **numéro d'emplacement, pas une chronologie**. `08-conformite.md`
se remplit tôt — dès que le lieu et le format sont connus — et porte `08` parce que
les index `00` à `07` étaient pris : renuméroter casserait tous les dossiers déjà
produits.

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
lu:
  00-fiche-identite.md: 2
  03-prestataires.md: 4
---
```

- `evenement` / `jour_j` — recopiés depuis `00-fiche-identite.md`. S'ils divergent, la
  fiche d'identité fait foi ; signaler la divergence.
- `version` — entier, **incrémenté à chaque réécriture**. Critique pour le conducteur :
  l'équipe doit savoir quelle version elle tient en main le jour J.
- `maj` — date de dernière modification.

### `lu:` — versions des dépendances

Chaque brique consigne la version des fichiers dont elle dépend, **telle qu'elle les a
lus**. C'est ce qui rend la péremption détectable sans interprétation : si `02-budget.md` est
passé en v4 depuis, la brique qui déclare l'avoir lu en v3 est à repasser, et
`scripts/check_dossier.py` le dit. Sans ce champ, le contrôle se rabat sur la comparaison
des dates `maj`, qui rate tout ce qui se fait dans la même journée.

**Toute brique qui lit une autre brique le renseigne.** Deux exceptions, et deux
seulement : `event-cadrage`, qui est l'ancre et ne dépend de rien, et `event-dossier`,
dont les livrables ne portent pas de frontmatter — celui-ci fait figurer les versions
sources **sur le livrable lui-même**.

**La forme bloc ci-dessus est la seule lue.** `lu:` seul sur sa ligne, puis une ligne
indentée par dépendance. Une écriture sur une seule ligne (`lu:` suivi d'accolades) n'est
pas relue par `scripts/check_dossier.py` : le contrôle de péremption disparaît alors sans
message, ce qui est pire que de ne pas l'avoir.

Un dossier antérieur à cette règle et qui ne porte pas `lu:` reste valide — le contrôle
se rabat sur les dates `maj`, en moins précis.

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
| `event-retroplanning` | `00`, `08` | `01-retroplanning.md` |
| `event-budget` | `00`, `03`, `04` | `02-budget.md` |
| `event-prestataires` | `00`, `02` | `03-prestataires.md` |
| `event-inscriptions` | `00`, `02`, `03`, `05` | `04-inscriptions.md` |
| `event-conducteur` | `00`, `01`, `03`, `04` | `05-conducteur.md` |
| `event-risques` | tous ceux présents | `06-risques.md` |
| `event-debrief` | tous ceux présents | `07-debrief.md` |
| `event-conformite` | `00`, `03`, `04` | `08-conformite.md` |
| `event-dossier` | **tous** | `livrables/*` |

Une dépendance absente n'est **jamais bloquante** : produire quand même, en marquant
explicitement l'hypothèse retenue et en proposant la brique manquante.

### Le cycle `02` ↔ `03` : deux passes, pas une

`event-budget` lit `03-prestataires.md`, et `event-prestataires` lit `02-budget.md`.
**Ce n'est pas une dépendance, c'est un cycle** : quel que soit l'ordre, la première des
deux tourne sans sa dépendance. C'est normal et voulu — un budget se construit avant
d'avoir des devis, et on ne consulte pas des prestataires sans enveloppe.

**Conséquence : la seconde passe n'est pas optionnelle.**

| Passe | Brique | Ce qu'elle produit |
|---|---|---|
| 1 | `event-budget` | Budget d'estimation — toutes lignes en « Estimation », enveloppe du cadrage |
| 2 | `event-prestataires` | Cahiers des charges, devis comparés, **montants négociés** |
| 3 | `event-budget` **à nouveau** | Les montants négociés remplacent les estimations → **nouvelle version de `02`** |

Un budget qui reste en v1 alors que `03-prestataires.md` existe est un budget périmé : il
affiche des estimations dont on a les vrais prix. **Quand `event-prestataires` retient un
devis, elle annonce explicitement qu'il faut repasser `event-budget`** — et l'inverse vaut
aussi : un budget qui trouve `03` sur disque intègre ses montants au lieu de ré-estimer.

La révision doit dire **ce qui a bougé et pourquoi**, ligne à ligne. Un écart global proche
de zéro cache souvent deux erreurs de sens contraire qui s'annulent : c'est justement
l'information qu'on cherche.

**Ce qu'un cycle fait au champ `lu:`.** Sur une paire mutuelle, les deux briques ne peuvent
pas être à jour l'une de l'autre en même temps : celle qui n'a pas été écrite en dernier
porte forcément le `lu:` de la version précédente de l'autre. Ce retard d'**une** version
est le coût normal du cycle, et `scripts/check_dossier.py` ne le compte que comme
avertissement. Un retard de **deux versions ou plus** reste une erreur : cette fois la
brique a réellement manqué une passe. Les paires mutuelles se déduisent de la table
ci-dessus (`02` ↔ `03`, `02` ↔ `04`, `04` ↔ `05`) — elles n'ont pas à y être redéclarées.

Même logique, plus dangereuse, pour la **garantie traiteur** : `02` peut la poser en
hypothèse faute de `04-inscriptions.md`, `03` la reprend dans le cahier des charges, un
devis l'inscrit et un acompte la fige — sans que son propriétaire légitime l'ait jamais
validée. Une valeur estimée par une brique qui n'en est pas propriétaire doit être
**re-vérifiée dès que le propriétaire existe**, et jamais figée dans un contrat avant.

## Écrire

- **Compléter, ne pas écraser.** Si le fichier existe, en reprendre le contenu, appliquer
  la modification demandée, et conserver le reste. Ne jamais repartir d'une page blanche
  sans le dire.
- **Incrémenter `version`** et mettre `maj` à la date du jour.
- **Renseigner `lu:`** avec la version de chaque dépendance effectivement ouverte — pas
  celle que tu supposes, celle que tu as lue.
- **Ne jamais supprimer une donnée saisie par un humain** (un nom de contact, un montant
  négocié, une contrainte du lieu) sans confirmation explicite.
- En fin d'écriture, annoncer le fichier touché et sa nouvelle version.

## Données personnelles du dossier

Le dossier porte des données nominatives **par construction** : l'annuaire jour J de
`05-conducteur.md` (nom, rôle, téléphone), le dispositif d'émargement, et à l'inscription
les régimes alimentaires et les besoins d'accessibilité. `references/conformite.md`
classe ces deux dernières catégories en **données sensibles** et impose leur destruction
après l'événement.

> **Un dossier versionné en git ne peut pas honorer cette destruction.** L'historique
> conserve ce qu'un commit a écrit, même si le fichier est vidé ensuite ; l'effacer
> suppose de réécrire le dépôt entier, et chaque clone déjà distribué garde sa copie.
> Une purge promise sur un dossier commité est une purge qui n'aura pas lieu.

Trois règles, à appliquer avant le premier dossier réel et non après :

1. **Le lien nom ↔ besoin ne s'écrit jamais dans un fichier du dossier.** Régimes
   alimentaires, allergies, besoins d'accessibilité : le **décompte** suffit à toutes les
   briques qui en dépendent — le traiteur reçoit des nombres, pas des noms. Le lien
   nominatif reste dans l'outil d'inscription, sous son propre régime et sa propre durée.
2. **`04-inscriptions.md` reste agrégé.** C'est déjà sa nature — un entonnoir, des taux,
   des segments. Y coller une liste d'inscrits transforme une brique de pilotage en
   fichier de données personnelles, et lui fait franchir la ligne sans que rien ne le
   signale.
3. **L'annuaire jour J se réduit au strict opérationnel** : rôle, et le numéro par lequel
   on joint ce rôle. Préférer une ligne de service à un portable personnel quand elle
   existe. `livrables/` étant régénérable, il n'a aucune raison d'être versionné —
   l'annuaire diffusé sur téléphone encore moins.

`.gitignore` à poser à la racine d'un dossier événement destiné à git :

```gitignore
livrables/
*-nominatif.md
*.csv
```

`livrables/` est **généré** : l'exclure ne perd rien, la vérité restant dans les `.md`.
Les deux autres motifs couvrent ce qu'on exporte d'un outil de billetterie et qu'on dépose
« provisoirement » dans le dossier.

**Poser la durée de conservation dès le cadrage, et nommer qui purge.** Une date sans
titulaire ne se tient pas — c'est la même règle que partout ailleurs dans ce dossier.
`scripts/check_dossier.py` signale l'empreinte de données personnelles fichier par
fichier, et avertit si un dossier versionné n'ignore pas `livrables/`.

## Journal des décisions

`00-fiche-identite.md` se termine par une section **Journal des décisions** :

| Date | Décision | Qui | Impact |
|---|---|---|---|

**Seule `event-cadrage` y écrit** — `00-fiche-identite.md` est son fichier. Toute autre
brique qui assiste à un arbitrage structurant ne le consigne pas elle-même : elle propose
de repasser `event-cadrage` pour l'ajouter au journal.

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
