# Jeux d'essai — event-ops

**Branche orpheline. Elle ne contient pas le plugin, et le plugin ne la contient pas.**

## Pourquoi une branche séparée

Un plugin installé depuis git est **cloné intégralement** dans
`~/.claude/plugins/cache/` : tout ce qui se trouve sur la branche par défaut part chez
chaque membre de l'équipe. Ni `plugin.json` ni `marketplace.json` n'offrent de filtre de
fichiers.

Les jeux d'essai sont volumineux, ne servent qu'au développement du plugin, et n'ont rien
à faire dans une installation. Les isoler sur une branche orpheline les garde **dans le
même dépôt, versionnés, clonables**, sans jamais entrer dans le tree distribué.

## Contenu

| Répertoire | Cas | Sortie attendue |
|---|---|---|
| `jpo-800/` | Journée portes ouvertes, 800 personnes, site industriel ouvert au public | **exit 1** — un défaut délibérément conservé |
| `convention-250/` | Convention commerciale interne, 250 personnes, hybride | **exit 0** — dossier sain |

Les deux forment une **paire** : même piège de la garantie traiteur estimée par une brique
qui n'en est pas propriétaire, issue opposée. `jpo-800` montre le devis qui part en
signature avec le mauvais chiffre ; `convention-250` montre la chaîne qui tient. Les lire
côte à côte vaut mieux que lire l'un des deux.

`convention-250` porte aussi la propriété qu'aucun autre jeu d'essai ne peut porter :
**un dossier sain sort en exit 0**. Ça paraît trivial ; ça ne l'était pas — avant la
correction du cycle `02`↔`03`, aucun dossier réel ne pouvait être vert.

Chacun porte son `README.md`, qui dit ce qu'il démontre.

## Utilisation

```bash
git fetch origin jeu-essai
git worktree add ../event-ops-jeux-essai jeu-essai
```

Le worktree permet de lire un jeu d'essai **à côté** du plugin, sans changer de branche
dans le dépôt de travail.

## Règles

- **Aucune donnée réelle.** Prestataires anonymisés, contacts vides, montants en ordres de
  grandeur, points réglementaires formulés comme points à faire vérifier — jamais comme
  règles établies.
- **Ne pas fusionner cette branche dans `main`.** Elle n'a aucun ancêtre commun et n'a pas
  vocation à en avoir un.
- Chaque jeu d'essai porte un `README.md` qui dit **ce qu'il démontre** et, le cas échéant,
  **quels défauts y sont délibérément conservés**. Un jeu d'essai « nettoyé » sans lire son
  README perd son intérêt.
