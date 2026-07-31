# event-ops

Plugin Claude **auto-suffisant** pour produire et piloter un dossier opérationnel
d'événement, de bout en bout. Aucune dépendance à des skills externes : tout est
embarqué dans le plugin, donc il s'installe et fonctionne à l'identique chez chaque
membre de l'équipe.

Cible : événements **corporate/conférence**, **salon/portes ouvertes**,
**soirée/réception**.

## Installation

Ce dépôt est son propre marketplace : le plugin s'installe directement depuis git.

Dans **Claude Code** — pas dans un terminal — saisir :

```
/plugin marketplace add StephaneBayle/event-ops
```

puis installer `event-ops` depuis ce marketplace. Selon le client, la même opération
est disponible dans l'interface de gestion des plugins.

> `/plugin` est une commande Claude Code, pas une commande shell. Dans l'application
> de bureau, la saisir dans la zone de conversation ; en terminal, au prompt de
> `claude` (qui suppose le CLI installé).

Pour mettre à jour après un `git push` : actualiser le marketplace, puis réinstaller.

C'est ce qui rend le plugin partageable : chaque membre de l'équipe installe depuis
la même source, et obtient exactement la même version.

## Les neuf briques

Chaque brique est une *skill* : elle se déclenche automatiquement quand le contexte
de ta phrase correspond à sa description, et elle est invocable explicitement par son
nom (`event-cadrage`, `event-budget`, …).

| Brique | Phase | Produit |
|---|---|---|
| `event-cadrage` | Ancre | Fiche d'identité : objectifs, KPIs, public, budget, contraintes ERP, gouvernance |
| `event-retroplanning` | Avant | Rétroplanning (chemin critique) + jalon go/no-go + RACI + checklists J-30/J-7/J-1 |
| `event-budget` | Transverse | Budget ligne à ligne, budgété/engagé/réalisé, HT-TTC, provision aléa, export xlsx |
| `event-prestataires` | Avant/pendant | Cahier des charges, comparaison de devis, contractualisation, briefing, réception |
| `event-inscriptions` | Avant/pendant | Entonnoir invités→présents, no-show, garantie traiteur, check-in |
| `event-conducteur` | Pendant | Conducteur minuté avec tops régie + plan de salle + escalade + PACE |
| `event-risques` | Transverse | Cartographie P×I + pre-mortem + plan de traitement 4T |
| `event-debrief` | Après | Bilan KPIs vs objectifs + After-Action Review + capitalisation |
| `event-dossier` | Chapeau | Assemble tout en un jeu de livrables (HTML, conducteur A4, budget xlsx, annuaire) |

## Le dossier événement

Un événement vit **3 à 6 mois** et traverse des dizaines de sessions. Les briques ne
travaillent donc pas en mémoire : elles lisent et écrivent un **dossier de fichiers
sur disque**, versionnable en git et éditable à la main.

```
mon-evenement/
├── 00-fiche-identite.md     ← l'ancre
├── 01-retroplanning.md
├── 02-budget.md
├── 03-prestataires.md
├── 04-inscriptions.md
├── 05-conducteur.md
├── 06-risques.md
├── 07-debrief.md
└── livrables/               ← généré par event-dossier
```

Chaque brique lit ce qui existe avant de produire, et complète sans écraser. Une
brique manquante n'est jamais bloquante : l'hypothèse retenue est signalée.

Conséquence directe : un dossier clôturé devient le **modèle du suivant** — le débrief
écrit ce qui doit être repris (prestataires, taux de no-show réel, postes sous-estimés).

## Frameworks mobilisés

RACI · chemin critique / rétroplanning · go/no-go · PACE planning · pre-mortem (Klein) ·
parcours-participant (service design) · cotation Probabilité × Impact + 4 T ·
After-Action Review.

## Usage typique

1. Démarrer : `event-cadrage` (ou « cadre-moi le nouvel événement … »).
2. Enchaîner au fil du besoin : rétroplanning, budget, prestataires, inscriptions,
   conducteur, risques.
3. Finaliser : `event-dossier` pour le jeu de livrables à diffuser.
4. Après l'événement : `event-debrief`, qui alimente le prochain dossier.

Les briques sont indépendantes : on peut n'en appeler qu'une (« fais-moi juste le
conducteur ») sans passer par les autres.

## Principes

- **Les hypothèses sont marquées comme telles.** Aucun nom, contact, montant ou date
  n'est inventé silencieusement.
- **Les trous se signalent, ils ne se lissent pas.** Les lentilles de complétude
  servent à révéler les manques, pas à produire un document rassurant.
- **Outil opérationnel réel.** Les dossiers produits servent à monter de vrais
  événements — d'où la rigueur exigée sur le budget, la sécurité et l'accessibilité.
