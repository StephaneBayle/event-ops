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
  - `conformite.md` — régimes réglementaires : déclencheur, autorité, pièce à produire,
    délai, conséquence. **Droit français, événement en France.** Ne dit pas le droit :
    dit quelle question poser, à qui, avant quand. Les ancres de texte qu'il cite sont
    des points d'entrée de vérification, jamais des citations faisant foi.
- `scripts/check_plugin.py` — vérification structurelle (voir ci-dessous).
- `scripts/bump_version.py` — change la version aux treize endroits à la fois.

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
- Les comptes annoncés par un fichier de référence — « 7 lentilles » et « 16 domaines »
  pour `chantiers.md` (cinq occurrences), « 6 familles » et « 21 régimes » pour
  `conformite.md` — correspondent à ce que le fichier liste vraiment, et les skills qu'il
  nomme en en-tête le référencent effectivement. Le contrôle est **générique** : déclarer
  le fichier et ses noms de compte dans `REFERENCES_COMPTEES` suffit.
- Un fichier de référence réglementaire porte **sa date de vérification et son
  relecteur**, déclarés dans `REFERENCES_DATEES`. Le linter avertit au-delà du seuil en
  mois, **et tant que le relecteur est « personne »** — ce qui est le cas aujourd'hui de
  `conformite.md`. Le jaune permanent est voulu : ces 21 régimes n'ont jamais été relus
  par un humain qualifié, et le taire serait exactement le silence que le contrôle vise.
  Avertissement et jamais erreur, pour la raison déjà apprise sur les cycles.
- Aucun fichier de `references/` n'est mort : chacun est ouvert par au moins une skill.
  Un fichier de référence que plus personne n'ouvre est du poids mort cloné chez chaque
  membre de l'équipe. Ce contrôle attrape en prime le **nom de fichier accentué** — le
  charset de la référence `${CLAUDE_PLUGIN_ROOT}` exclut les accents, donc un
  `references/conformité.md` échapperait en silence au contrôle d'existence. *Même classe de bug que « les six
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
- livrables générés plus anciens qu'une brique source ;
- **empreinte de données personnelles** — téléphones et courriels comptés fichier par
  fichier, en **information** : un annuaire jour J avec des numéros est légitime, c'est son
  versionnement qui ne l'est pas. En faire un avertissement le ferait crier sur chaque
  dossier réel, et emporterait avec lui le seul avertissement utile ;
- **le registre `08-conformite.md`** — bandeau d'avertissement présent en tête, et chaque
  statut pris dans le vocabulaire fermé de la skill. C'est une **liste blanche** : interdire
  le seul mot « conforme » laisserait passer « OK », « validé », « RAS ». Le bandeau est
  cherché sur un vocabulaire large — la skill le fait *rédiger*, donc une comparaison de
  chaîne exacte casserait à la première reformulation ;
- **dossier versionné dont `livrables/` n'est pas ignoré** — avertissement. C'est git qui
  répond (`git check-ignore`), pas une relecture du `.gitignore` : les règles de
  précédence des motifs sont exactement ce qu'on relirait mal. Si git ne répond pas, le
  contrôle se tait plutôt que de conclure. **Sonder un fichier de `livrables/`, jamais le
  répertoire** : le motif `livrables/` ne vise que les répertoires, et tant que le
  répertoire n'existe pas git le traite comme un fichier et répond « non ignoré ». Et
  passer à `subprocess` un `cwd` qui existe : sonder un chemin absent avec `cwd` sur son
  parent absent fait échouer l'appel, donc **taire le contrôle** — les deux défauts ont eu
  lieu, et seule la contre-épreuve les a montrés.

Ce qui relève de l'information et **jamais de l'erreur** : les briques absentes et
l'empreinte de données personnelles. La convention est explicite — une dépendance absente
n'est jamais bloquante.

**Pourquoi ces deux derniers contrôles existent.** La convention impose la destruction des
régimes alimentaires et des besoins d'accessibilité après l'événement, et le dossier est
présenté comme versionnable en git. Les deux ne tiennent pas ensemble : l'historique
conserve ce qu'un commit a écrit, et chaque clone distribué garde sa copie. Le plugin
énonçait donc une obligation que son architecture invitait à enfreindre. La section
« Données personnelles du dossier » de la convention tranche, `event-cadrage` pose le
`.gitignore` à la création, et ces deux contrôles rendent l'écart visible.

`--no-annotations` supprime les lignes `::error::` / `::warning::` de GitHub Actions.
Indispensable quand la CI vérifie une sortie **attendue en erreur** : sans lui la course
s'affiche en rouge alors qu'elle valide le comportement nominal, **et** les annotations
polluent la sortie qu'on analyse. Ne pas essayer de s'en passer en forçant
`GITHUB_ACTIONS=false` dans le `env:` d'une étape — c'est une variable réservée, le runner
la réinjecte, et l'override passe inaperçu.

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

Deux jeux d'essai, et ils forment une **paire** — même piège, issue opposée :

| Jeu d'essai | Cas | Sortie attendue |
|---|---|---|
| `jpo-800` | Portes ouvertes, 800 personnes, site industriel | **exit 1** — défaut délibéré |
| `convention-250` | Convention interne, 250 personnes, hybride | **exit 0** — dossier sain |

`jpo-800` conserve **délibérément** une incohérence (`03-prestataires.md` à 450 couverts
quand `02` et `05` sont à 380) : une garantie traiteur estimée par une brique qui n'en est
pas propriétaire, puis figée dans un devis. `convention-250` montre la même chaîne qui
**tient** — l'hypothèse reste une fourchette au cahier des charges jusqu'à ce que
`event-inscriptions` tranche.

Depuis la v0.5.0 les deux portent `08-conformite.md`, et l'opposition des deux registres
est le plus utile de la paire : `jpo-800` doit faire **autoriser** l'ouverture d'un site
non ERP et sort avec deux indéterminés et deux lignes sans vérificateur ; `convention-250`
s'appuie sur un lieu qui porte déjà son régime, tranche les vingt et un et écarte huit
régimes **avec leur motif**. `jpo-800` conserve en prime un doublon assumé — `00` § 6 garde
son tableau réglementaire d'avant la brique, parce que le réduire ferait passer la fiche en
v2 et périmerait les quatre briques qui la lisent. C'est l'état que rencontrera toute
équipe qui met le plugin à jour.

`convention-250` porte en plus la propriété qu'aucun autre ne peut porter : **un dossier
sain sort en exit 0**. Ça paraît trivial ; avant la correction du cycle `02`↔`03`, aucun
dossier réel ne le pouvait.

Les deux tournent en CI. Leurs `README.md` disent ce qu'ils démontrent — un jeu d'essai
« nettoyé » sans lire son README perd son intérêt.

### Changer de version

La version vit à **treize endroits** : le manifeste, les deux champs de `marketplace.json`,
et le frontmatter des dix skills. Ne pas les modifier à la main :

```bash
python3 scripts/bump_version.py --patch     # ou --minor, --major, ou 0.5.0
```

Le manifeste fait foi pour la version courante. Le script ne remplace **que** là où la
valeur est déjà cette version : un fichier désaligné n'est pas rattrapé en silence, il
est signalé — son écart pose une question à laquelle le script n'a pas la réponse.
`--dry-run` n'écrit rien.

### Ajouter une skill

**Six** endroits à mettre à jour, sinon le script échoue — c'est le but :

1. `skills/<nom>/SKILL.md`.
2. La table lit/écrit de `references/convention-dossier.md` (et son arborescence).
3. Le tableau du `README.md` — **et son compte en toutes lettres** (« Les dix briques »).
4. Dans le `SKILL.md`, la phrase « Lis … ».
5. Dans le `SKILL.md`, l'instruction `lu:` — soit l'instruction de le renseigner, soit la
   mention explicite qu'il n'y en a pas. Le linter refuse le silence sur ce point, et il
   exige que les dépendances énumérées aux **deux** endroits (4 et 5) soient exactement
   celles de la colonne « Lit ». Attention : la phrase « Lis … » peut citer le fichier
   que la skill écrit, l'instruction `lu:` **non**.
6. Si la skill parcourt un fichier de référence qui la nomme en en-tête, le
   `${CLAUDE_PLUGIN_ROOT}/references/<fichier>` correspondant.

Contraintes de nommage, toutes silencieuses si on les enfreint :

| Contrainte | Pourquoi |
|---|---|
| Nom de skill `event-[a-z]+` — **un seul segment, sans chiffre ni accent** | `event-x-y` n'est pas reconnu par la table lit/écrit, et le scan du README le capture tronqué |
| Fichier écrit `NN-nom.md`, sans accent | `08-conformité.md` n'est reconnu ni par la convention ni par `check_dossier.py` |
| Nom de fichier de référence **ASCII** | le charset `${CLAUDE_PLUGIN_ROOT}` exclut les accents |
| Au plus 30 caractères entre « écris » et le nom de fichier | tolérance du linter à la prose, pas plus |
| Jamais `lu:` sur une seule ligne dans un exemple | neutralise le contrôle de péremption sans un message |

Un index d'un dossier événement est un **emplacement, pas une chronologie** : une brique
qui se remplit tôt peut porter un index élevé si les précédents sont pris. Renuméroter
casserait tous les dossiers déjà produits et les deux jeux d'essai.

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
