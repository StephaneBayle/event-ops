# Jeu d'essai — convention commerciale interne, 250 personnes, hybride

Dossier événement **produit en déroulant les skills du plugin de bout en bout** sur un cas
fictif de la cible corporate/conférence. Il est le **pendant sain** de `jpo-800/` : celui-ci
sort en **exit 0**, l'autre en exit 1.

**Ce n'est pas un événement réel.** Aucune société, aucun contact, aucun devis authentique.
Les prestataires sont désignés par lot (L1…L12), toutes les cases de prix sont vides et
marquées « à obtenir ».

## Pourquoi ce cas

`jpo-800` couvrait un salon grand public en site industriel. Celui-ci prend l'autre bout de
la cible et sollicite ce que le premier ne touche pas :

| Point | Où le voir |
|---|---|
| **Hybride assumé** (deux publics, un seul mange) | `00` § 4, `02` poste « Hybride », `04` § 1 |
| **Budget qui dépasse et ne se résorbe pas** | `02` § 5 — 13 070 € d'arbitrages pour 18 815 € d'écart |
| **Gouvernance manquante** | `00` § 7 — le pouvoir d'annuler n'a pas de titulaire |
| **Consultation non lancée** | `03` — CDC rédigés, grille comparative **vide** |
| **Incertitude TVA non levée** | `02` § 4 — elle double l'ampleur du dépassement |
| **Conformité d'un lieu qui porte son régime** | `08` — huit régimes écartés avec motif |

## Ordre de production

```
event-cadrage  →  event-budget  →  event-prestataires  →  event-inscriptions
    00 v1           02 v1              03 v1                  04 v1
                    02 v2 ←──────────────────────────────────────┘
```

**État final : `00` v1 · `02` v2 · `03` v1 · `04` v1.**

`01-retroplanning.md`, `05-conducteur.md`, `06-risques.md` et `07-debrief.md` sont
**volontairement absents** — à J-203 avec aucune consultation lancée, un dossier ressemble
à ça, et le trou dans la numérotation rend l'incomplétude lisible sur un simple `ls`.

## Ce que ce jeu d'essai démontre

### 1. Un dossier sain peut sortir vert

C'est sa raison d'être principale, et c'était **structurellement impossible** avant la
correction du cycle : `02` lit `03` et `03` lit `02`, donc celle des deux qui n'est pas
écrite en dernier porte forcément un `lu:` en retard d'une version. L'ancienne logique en
faisait une erreur dure — un dossier parfaitement tenu sortait rouge à chaque exécution, et
on apprenait à ignorer le vérificateur.

Ici les deux retards d'une version sortent en **avertissement**, et le dossier en exit 0.

### 2. La garantie traiteur n'a pas été détournée

C'est le pendant exact du défaut de `jpo-800`, avec l'issue inverse. Même enchaînement,
même piège, résultat opposé :

| Étape | `jpo-800` | `convention-250` |
|---|---|---|
| `02` pose une hypothèse faute de `04` | 450 couverts | 200 couverts, marqués **B1, sans propriétaire** |
| `03` la reprend au cahier des charges | **Inscrite dans un devis retenu** | **Fourchette 170–210, ferme au 11/03, aucun acompte** |
| `04` tranche | 380 — trop tard, le devis est parti | **170 — dans la fourchette, rien à renégocier** |
| `02` repassé | v3, signale « à notifier avant signature » | v2, reprend 170 sans le discuter |

Lire les deux côte à côte est le meilleur moyen de comprendre ce que la convention appelle
« une valeur estimée par une brique qui n'en est pas propriétaire ».

### 3. Le champ `lu:` est écrit en forme bloc

Les trois briques dépendantes le renseignent, et `check_dossier.py` les relit toutes. C'est
ce que la forme sur une seule ligne — enseignée un temps par deux skills — faisait
disparaître **sans message**.

### 4. La seconde passe du budget sait dire que rien n'a bougé

`02` v2 chiffre la révision ligne à ligne (−1 590 € sur la restauration) **et constate que
rien d'autre n'a changé**, parce que `03` ne porte encore aucun montant négocié. Un budget
repassé qui n'aurait rien à dire serait un budget qui n'a pas regardé.

### 5. Un registre de conformité peut être entièrement tranché

`08-conformite.md` est le pendant exact de celui de `jpo-800`, et l'opposition est le
plus utile de la paire :

| | `jpo-800` | `convention-250` |
|---|---|---|
| Lieu | Site industriel, non ERP en usage normal | Lieu de congrès, déjà ERP |
| Régime structurant | Utilisation exceptionnelle — instruction longue, bloquante | Aucun : le lieu porte son régime |
| Ce qui pèse | Faire autoriser l'ouverture | L'hybride — captation, replay, données |
| Indéterminés | 2 | **0** |
| Lignes sans vérificateur | 2 | **0** |

**Zéro indéterminé n'est pas un signe de complaisance** : c'est ce que permet un lieu
qui porte déjà son régime, et les huit régimes écartés le sont **avec leur motif**. Deux
d'entre eux sont explicitement signalés comme à rouvrir si le format bouge — une
convention qui deviendrait payante ferait changer de réponse la première condition du
régime « grands rassemblements ».

Le seul trou est ailleurs, et le registre le dit sans le corriger lui-même : `00` § 7 ne
désigne toujours pas qui a le pouvoir d'annuler. Le registre sait qui **vérifie**, pas
qui **décide** — et il propose de repasser `event-cadrage` plutôt que d'écrire dans le
fichier d'une autre brique.

## Ce qu'il ne faut pas y chercher

- **Des prix de marché.** Ordres de grandeur cohérents entre eux, pas une base tarifaire.
  Ne jamais les réutiliser comme référence de chiffrage.
- **Du droit.** Régime ERP, effectif autorisé, taux de TVA, droit à l'image, RGPD : tout
  est formulé en **point à faire vérifier**, jamais en règle établie. C'est le comportement
  attendu du plugin et il doit le rester.
- **Un dossier complet.** Quatre briques sur huit, douze lots non sourcés, aucun prix
  obtenu, et le décideur du go/no-go pas encore nommé.

## Vérification

```bash
python3 <chemin-du-plugin>/scripts/check_dossier.py convention-250
```

Attendu : **exit 0**, **aucune erreur**, et **deux avertissements de cycle**
(`02`↔`03` et `02`↔`04`) qui sont le coût structurel normal et **ne se corrigent pas**.

**Toute erreur est une régression.** Et si les deux avertissements disparaissaient, ce
serait le signe qu'on a cessé de détecter les cycles — à vérifier avant de s'en réjouir.

Le compteur « jour J dans N jours » varie avec la date du jour : c'est une information, pas
une assertion.
