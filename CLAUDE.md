# Event-ops Plugin

Plugin Claude pour la gestion d'événements et la production de dossiers opérationnels.

## Structure

- `.claude-plugin/plugin.json` — **manifeste du plugin, source de vérité de la version.**
  Ne pas ajouter de `package.json` : le plugin ne contient aucun code JS.
- `.claude-plugin/marketplace.json` — le dépôt est son propre marketplace (schéma à
  plugin unique, `source: "."`), ce qui rend le plugin installable depuis git.
  **Il duplique version, description et keywords du manifeste** : les deux fichiers
  doivent être modifiés ensemble, le linter échoue sinon.
- `skills/` — les briques, chacune auto-suffisante (aucune dépendance à une skill externe).
- `references/` — fichiers de référence partagés, parcourus par les skills.
  - `chantiers.md` — taxonomie des domaines + lentilles de complétude.
  - `convention-dossier.md` — convention du dossier événement persistant.
- `scripts/check_plugin.py` — vérification structurelle (voir ci-dessous).
- `scripts/bump_version.py` — change la version aux douze endroits à la fois.

## Vérification

**Après toute modification du plugin, lancer :**

```bash
python3 scripts/check_plugin.py
```

Aucune dépendance (bibliothèque standard). Tourne aussi en CI sur push et PR
(`.github/workflows/check.yml`).

Le script vérifie les invariants **mécaniques** — il ne juge pas la qualité des
livrables, qui reste un jugement humain (test de l'étranger compétent) :

- Manifeste présent, JSON valide, sans placeholder dans `homepage`.
  *C'est le bug qui a réellement eu lieu : `plugin.json` non commité, plugin
  non installable.*
- Frontmatter de chaque skill : `name` identique au nom du répertoire — un
  désalignement et la skill ne se déclenche jamais.
- Versions des skills alignées sur celle du manifeste.
- Chaque `${CLAUDE_PLUGIN_ROOT}/…` pointe vers un fichier existant. **Échec
  silencieux sinon** : Claude ne trouve pas le fichier et improvise de mémoire,
  ce que les skills lui interdisent explicitement.
- Le fichier que chaque skill déclare écrire correspond à la table lit/écrit de
  `convention-dossier.md`, et les index `NN-` sont uniques.
- Les skills du `README` correspondent aux répertoires de `skills/`, nombre annoncé
  compris.
- Chaque skill **dit** ce qu'elle fait du champ `lu:` : l'instruction de le renseigner si
  elle dépend d'une autre brique, la mention explicite « pas de champ `lu:` » sinon.
  Le contrôle vérifie l'instruction, **pas le comportement** — `lu:` reste une
  déclaration, pas une mesure.
- Aucune skill ne montre `lu:` **sur une seule ligne**. `check_dossier.py` ne relit que la
  forme bloc ; la forme sur une ligne fait disparaître le contrôle de péremption **sans
  message**, ce qui est pire que de ne pas l'avoir. Deux skills l'ont enseignée.
- Les dépendances qu'une skill énumère — dans sa phrase « Lis … » **et** dans son
  instruction `lu:` — correspondent à la colonne « Lit » de la convention. Sans lui,
  `event-budget` demandait de consigner la lecture d'un fichier qu'il n'avait jamais dit
  de lire.
- Les comptes annoncés par `references/chantiers.md` — « 7 lentilles », « 16 domaines »,
  répétés à quatre endroits — correspondent à ce que le fichier liste vraiment, et les
  skills qu'il nomme le référencent effectivement. *Même classe de bug que « les six
  briques » du README, mais plus coûteuse : les skills doivent le parcourir entrée par
  entrée, et un compte faux leur en fait sauter une sans que rien ne le signale.*

Les quatre derniers contrôles sont les plus utiles sur la durée : ce sont des
**invariants dupliqués**, et tout invariant écrit à deux endroits finit par diverger.

### Vérifier un dossier produit

`check_plugin.py` vérifie le **plugin**. Son pendant vérifie un **dossier événement réel** :

```bash
python3 scripts/check_dossier.py <chemin-du-dossier>
```

Sans argument, il cherche un `00-fiche-identite.md` dans le répertoire courant ou juste
en dessous, et refuse de deviner si plusieurs dossiers sont candidats.

Il lit le mapping index → brique et les dépendances **dans la table lit/écrit de la
convention** — rien n'y est redéclaré, sinon le script deviendrait à son tour un invariant
dupliqué. Il contrôle :

- frontmatter complet, `brique` cohérente avec l'index, `version` entière, dates ISO ;
- `evenement` et `jour_j` identiques partout, **la fiche d'identité faisant foi** ;
- fichiers hors convention (mauvais index, mauvais nom) ;
- **fraîcheur** — une brique plus ancienne que ce dont elle dépend est signalée, avec un
  message dédié pour le cycle `02` ↔ `03` ;
- **péremption exacte** via le champ `lu:`, que chaque brique renseigne avec la version
  de ses dépendances au moment où elle écrit (voir la convention) ;
- **les cycles**, déduits de la table (`02`↔`03`, `02`↔`04`, `04`↔`05`) et jamais
  redéclarés. Sur une paire mutuelle, les deux briques ne peuvent pas être à jour l'une de
  l'autre en même temps : un retard d'**une** version est le coût structurel du cycle et
  ne sort qu'en avertissement ; **deux ou plus** reste une erreur. Sans cette nuance le
  contrôle ne pouvait jamais être vert, et on apprend vite à ignorer un outil qui crie
  toujours ;
- livrables générés plus anciens qu'une brique source.

Ce qui relève de l'information et **jamais de l'erreur** : les briques absentes. La
convention est explicite — une dépendance absente n'est jamais bloquante.

Il tourne en CI sur le **jeu d'essai** de la branche orpheline (job `jeu-essai`), qui est
son seul test de bout en bout : la course récupère la branche, lance le script sur
`jpo-800` et exige exit 1 avec la seule erreur que son `README` documente. Sans ce job,
deux défauts silencieux y étaient déjà passés inaperçus.

### Jeux d'essai

`check_plugin.py` ne vérifie que la mécanique. Pour juger une modification de skill sur le
fond, comparer sa sortie au **jeu d'essai de référence** — un dossier événement complet
produit en déroulant les skills de bout en bout (journée portes ouvertes, 800 personnes) :

```bash
git worktree add ../event-ops-jeux-essai jeu-essai
```

Les jeux d'essai vivent sur la **branche orpheline `jeu-essai`**, jamais dans l'arbre de
`main` : un plugin installé depuis git est cloné intégralement dans
`~/.claude/plugins/cache/`, et aucun des deux manifestes n'offre de filtre de fichiers.
Tout ce qu'on met ici part chez chaque membre de l'équipe. **Ne rien ajouter à la racine
qui ne serve pas à l'exécution du plugin.**

Le jeu d'essai `jpo-800` conserve **délibérément** une incohérence (`03-prestataires.md`
à 450 couverts quand `02` et `05` sont à 380) : elle documente le seul défaut de fond du
plugin — rien ne rejoue les sections « À faire remonter ». Son `README.md` l'explique.

### Changer de version

La version vit à **douze endroits** : le manifeste, les deux champs de `marketplace.json`,
et le frontmatter des neuf skills. Ne pas les modifier à la main :

```bash
python3 scripts/bump_version.py --patch     # ou --minor, --major, ou 0.5.0
```

Le manifeste fait foi pour la version courante. Le script ne remplace **que** là où la
valeur est déjà cette version : un fichier désaligné n'est pas rattrapé en silence, il
est signalé — son écart pose une question à laquelle le script n'a pas la réponse.
`--dry-run` n'écrit rien.

### Ajouter une skill

Trois endroits à mettre à jour, sinon le script échoue — c'est le but :
`skills/<nom>/SKILL.md`, la table lit/écrit de `references/convention-dossier.md`,
et le tableau du `README.md`.

Dans le `SKILL.md`, ne pas oublier le champ `lu:` : l'instruction de le renseigner, ou la
mention explicite qu'il n'y en a pas. Le linter refuse le silence sur ce point — et il
exige que les dépendances énumérées aux **deux** endroits (la phrase « Lis … » et
l'instruction `lu:`) soient exactement celles de la colonne « Lit ».

## Principes de conception

1. **Auto-suffisance** — aucune skill n'appelle une skill externe au plugin. Le plugin
   s'installe et se comporte à l'identique chez chaque membre de l'équipe.
2. **Persistance sur disque** — les skills lisent et écrivent dans un dossier événement
   (fichiers `.md` numérotés). Un dossier vit 3 à 6 mois et dépasse largement une session :
   l'état ne doit jamais vivre uniquement dans la conversation. Voir
   `references/convention-dossier.md`.
3. **Les hypothèses sont marquées comme telles** — toute date, tout responsable, tout
   montant supposé est explicitement signalé. Ne jamais inventer un nom ou un contact.
4. **Ne jamais masquer un trou** — les lentilles de complétude servent à révéler les
   manques, pas à produire un document lisse. Un manque détecté se liste noir sur blanc.

## Cible métier

Événements **corporate/conférence**, **salon/portes ouvertes**, **soirée/réception**.
Le pédagogique/wargame n'est pas une cible de ce plugin.

## Notes de cadre

`event-ops` est un **outil opérationnel réel** : les dossiers produits servent à monter
de vrais événements. Pas de mention EXERCICE/FICTIF, pas d'encadré « Limites du modèle » —
le cadre déontologique wargame du `CLAUDE.md` racine ne s'applique pas ici.

En revanche, les livrables engagent des budgets et de la sécurité du public : la rigueur
sur les hypothèses (principe 3) et sur les obligations légales (accessibilité/PMR, ERP,
assurances) n'est pas négociable.
