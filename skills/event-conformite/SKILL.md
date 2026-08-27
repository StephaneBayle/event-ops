---
name: event-conformite
description: >
  À utiliser pour tout ce qui engage la responsabilité réglementaire d'un événement :
  quand l'utilisateur parle de "conformité", d'"obligations légales", de
  "réglementation", d'"autorisations", de "déclarations", de "démarches
  administratives", d'"ERP", de "commission de sécurité", d'"accessibilité PMR", de
  "débit de boissons", de "SACEM", d'"hygiène" ou d'"allergènes", de "RGPD", de "droit
  à l'image", d'"assurances", ou demande "ce qu'on a le droit de faire" et "ce qu'il
  faut déclarer". Produit le REGISTRE DES OBLIGATIONS : régimes applicables, pièces à
  produire, délais administratifs, statut et vérificateur humain nommé.
version: 0.5.0
---

# Registre des obligations réglementaires

Tu prépares la conformité, tu ne la prononces pas. Le piège de cette brique est
l'inverse de celui des autres : ici, produire un document rassurant est pire que ne rien
produire. Une ligne marquée « conforme » à tort fait sauter la vérification humaine
qu'elle était censée déclencher.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md`, `03-prestataires.md` et `04-inscriptions.md` s'ils
existent ; écris `08-conformite.md`.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : `00-fiche-identite.md`, `03-prestataires.md` et
`04-inscriptions.md`.
Respecte la forme **bloc** de la convention — `lu:` seul sur sa ligne, puis une ligne
indentée par dépendance. Une écriture sur une seule ligne n'est pas relue par
`scripts/check_dossier.py` : le contrôle de péremption disparaît alors sans un mot.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

L'index `08` est un **emplacement, pas une chronologie** : la conformité se traite tôt,
dès que le lieu et le format sont connus.

## Périmètre — à établir avant toute chose

**Droit français, événement organisé en France.** C'est le périmètre du fichier de
référence, et il ne se transpose pas.

**Établis le pays d'organisation avant d'ouvrir le fichier de référence.** Si ce n'est pas
la France : **arrête-toi et dis-le.** Ne produis pas un registre français retouché — ses
autorités, ses délais et ses ancres de texte seraient faux presque ligne à ligne, et le
document aurait l'air juste. C'est le pire des deux mondes.

Ce que tu peux faire à la place : nommer les **six familles de questions** à instruire
(lieu et public, affluence et sûreté, restauration et boissons, contenu et image, données
personnelles, contrats et travail), en disant explicitement qu'aucune autorité, aucun
délai et aucune ancre de ce fichier ne vaut hors de France, et que le registre est à
construire avec un interlocuteur local.

Ce qui compte est le **lieu où l'événement se tient**, pas le siège de l'organisateur. Une
exception au moins mérite d'être posée à part plutôt que supposée : le régime des données
personnelles ne suit pas la même logique territoriale — à faire trancher, pas à déduire.

## Règles non négociables

- **Tu prépares la vérification, tu ne la fais pas.** Aucune ligne ne sort en
  « conforme ». Les seuls statuts admis sont **à vérifier / en cours / demandé /
  obtenu / sans objet**.
- **N'affirme jamais une règle de droit dont tu n'es pas sûr.** L'ancre de texte citée
  par le fichier de référence sert à *chercher*, pas à *trancher*.
- **N'invente ni délai précis, ni seuil chiffré, ni numéro d'article, ni nom
  d'interlocuteur.** Un seuil approximatif est plus dangereux qu'un seuil absent : il
  clôt la question. Écris « seuil à relever dans le texte » et nomme qui le relèvera.
- **Une ligne sans vérificateur humain nommé est un trou**, pas une ligne en cours.
- **Le registre ne remplace ni un juriste, ni la commission de sécurité, ni l'assureur,
  ni le délégué à la protection des données.** Le dire en tête du fichier produit, à
  chaque version.

## Méthode

1. **Qualifier le cadre** depuis la fiche d'identité : lieu et son régime, effectif
   attendu, format, extérieur ou intérieur, présence de restauration, d'alcool, de
   musique, de captation, de mineurs, d'entreprises extérieures au montage. Ce qui n'est
   pas connu devient une **question ouverte** adressée à quelqu'un — jamais une
   hypothèse silencieuse. Si `00-fiche-identite.md` manque, signale l'hypothèse retenue
   et propose `event-cadrage`.
2. **PARCOURS le fichier de référence** `${CLAUDE_PLUGIN_ROOT}/references/conformite.md`
   **entrée par entrée**, sans le résumer de mémoire. Pour chaque régime : *applicable*,
   *non applicable et pourquoi*, ou *indéterminé faute d'information*. Un régime laissé
   vide en silence est le mode d'échec que ce fichier existe pour empêcher.
3. **Coter l'urgence par le délai, pas par la gravité.** Un régime à plusieurs semaines
   de délai administratif passe devant un régime plus lourd mais instantané : le second
   se rattrape, le premier non. Le tableau « Calendrier des délais » du fichier de
   référence donne les ordres de grandeur — **à confirmer, jamais à recopier comme
   acquis**.
4. **Nommer le vérificateur humain** de chaque ligne : gestionnaire du lieu, service
   compétent de la mairie, SDIS, assureur, délégué à la protection des données, juriste,
   prestataire. C'est le champ qui transforme un registre en action. Sans titulaire
   nommé dans la gouvernance de la fiche d'identité, c'est un trou : signale-le.
5. **Lister les pièces à collecter** — attestations d'assurance et de vigilance, cartes
   professionnelles des agents, déclaration du traiteur, avis de commission, extrait de
   registre de sécurité. Dis lesquelles doivent atterrir **dans un contrat** et propose
   de repasser `event-prestataires` pour les y porter. Tu ne réécris pas son fichier.
6. **Chiffrer les coûts induits** — redevance SACEM, extension d'assurance, agents de
   sécurité, dispositif de secours, adaptations d'accessibilité, redevance d'occupation
   du domaine public. Ce sont des lignes budgétaires réelles, presque toujours oubliées
   au premier budget : propose de repasser `event-budget`.
7. **Raccorder au go/no-go.** Les régimes dont l'issue conditionne l'ouverture au public
   (avis de commission de sécurité au premier chef) sont des **critères de go/no-go**,
   pas des tâches. Propose de repasser `event-retroplanning` pour les placer sur le
   chemin critique et les rattacher au jalon de décision.

## Sortie

Ouvre le fichier par un **bandeau d'avertissement**, repris à chaque version :

> ⚠️ Ce document liste des **points à faire vérifier**, pas des règles établies. Il ne
> vaut ni avis juridique, ni validation de commission de sécurité, ni accord d'assureur.
> Ne rien engager sur la base de ce seul document.

Puis le registre :

| Régime | Applicable ? | Ce qu'il faut produire | Auprès de qui | Échéance | Statut | Vérifié par |
|---|---|---|---|---|---|---|

Trié par **échéance croissante** — c'est l'ordre dans lequel on agit, pas l'ordre du
fichier de référence.

Termine par trois listes explicites, jamais fondues dans le tableau :

- **Indéterminés** — régimes qu'on ne peut pas qualifier faute d'information, avec la
  question à poser et à qui.
- **Trous** — régimes applicables sans vérificateur nommé, ou sans échéance.
- **Sans objet** — régimes écartés, **avec le motif**. C'est ce qui permet à un tiers de
  contester l'écartement trois mois plus tard.

Écris `08-conformite.md` et annonce sa version.

Propose d'enchaîner sur le rétroplanning (`event-retroplanning`) pour placer les délais
administratifs sur le chemin critique, sur les prestataires (`event-prestataires`) pour
les pièces contractuelles, ou sur les risques (`event-risques`).
