# Jeu d'essai de référence — journée portes ouvertes, 800 personnes

Dossier événement **complet et réel dans sa forme**, produit en déroulant les skills du
plugin de bout en bout sur un cas fictif. Il sert de **référence de sortie** : à quoi
ressemble un dossier correctement produit, et où le plugin trouve ses limites.

**Ce n'est pas un événement réel.** Aucune société, aucun contact, aucun devis authentique.
Les prestataires sont désignés A / B / C, tous les téléphones sont vides.

## Pourquoi ce cas

Une journée portes ouvertes à 800 personnes sollicite les quatre points les plus fragiles
du plugin en même temps :

| Point de fragilité | Où le voir |
|---|---|
| **Jauge et no-show** | `00` § 4 (distinction 800 cumulés / 280 simultanés), `04` § 2-3 |
| **Accessibilité PMR** | `00` § 6 (alerte de cadrage), `02` poste 5, `05` § 7 |
| **Sûreté de foule** | `03` § 4-5 (dimensionnement des agents), `05` § 4 (escalade) |
| **Budget avec garantie traiteur** | `02` F01, `03` § 2-3, **`04` § 4 (la décision)** |

Le site est un **site industriel ouvert au public pour la journée** : il n'est pas ERP en
fonctionnement normal, il n'est pas accessible par construction, et il n'a jamais accueilli
de public. Tout ce qui va de soi dans une salle de conférence est ici un chantier.

## Ordre de production

```
event-cadrage  →  event-budget  →  event-prestataires  →  event-conducteur  →  event-inscriptions
    00 v1           02 v1              03 v1                  05 v1                  04 v1
                    02 v2 ←────────────┘                                             │
                    02 v3 ←──────────────────────────────────────────────────────────┤
                                                            05 v2 ←──────────────────┘
```

**État final : `00` v1 · `02` v3 · `03` v1 · `04` v1 · `05` v2.**

`01-retroplanning.md`, `06-risques.md` et `07-debrief.md` sont **volontairement absents** —
le trou dans la numérotation rend l'incomplétude du dossier lisible sur un simple `ls`.

## Ce que le jeu d'essai démontre

1. **La reprise d'état fonctionne et se voit.** Chaque fichier annonce en tête ce qu'il a
   trouvé sur disque et ce qui manquait. Les hypothèses posées faute de dépendance sont
   marquées (`⚠️[04]` dans le conducteur v1, `B1` dans le budget).
2. **Le cycle `02` ↔ `03` impose bien deux passes.** Le budget v2 intègre les devis et
   chiffre l'écart ligne à ligne : un net de **+63 €** qui masque un F&B surestimé de 785 €
   et une sécurité sous-estimée de 848 €. C'est l'exemple qui justifie la règle de la
   convention.
3. **Une brique tardive force les briques amont à bouger.** `04-inscriptions` ramène la
   garantie traiteur de 450 à 380 couverts (`02` → v3) et le check-in de 2 à 5 postes
   (`05` → v2).
4. **Le versionnement du conducteur est utilisable.** `05` v2 porte en tête « v2 —
   31/07/2026 » et une table des sept changements depuis la v1.

## Le défaut délibérément conservé

🔴 **`03-prestataires.md` porte encore 450 couverts dans son cahier des charges**, alors
que `02` v3 et `04` v1 sont à 380. Le budget v3 le signale (« à notifier au Prestataire B
avant signature ») mais le fichier n'a pas été repassé.

**C'est volontaire.** C'est la démonstration du seul défaut de fond que le run ait révélé :
la convention repose sur des sections « À faire remonter » que rien ne rejoue. Sur un
dossier qui vit 3 à 6 mois, c'est le devis à 450 qui part en signature.

Depuis que les briques renseignent `lu:`, **le défaut est détecté mécaniquement** — c'est
précisément ce qu'il sert à démontrer :

```
$ python3 scripts/check_dossier.py jpo-800
·  briques absentes : 01 (retroplanning), 06 (risques), 07 (debrief)
·  jour J dans N jours (J-N)          ← dépend de la date du jour
⚠  cycle 02↔04: 04-inscriptions.md porte 02-budget.md v2, actuel v3 —
   retard d'une version, coût normal du cycle
⚠  cycle 04↔05: 04-inscriptions.md porte 05-conducteur.md v1, actuel v2 —
   retard d'une version, coût normal du cycle
✗  lu: 03-prestataires.md a été écrit sur la base de 02-budget.md v1,
   or 02-budget.md est en v3 — à repasser

1 erreur(s) — voir ci-dessus.
```

**Les deux avertissements de cycle sont attendus et ne se corrigent pas.** Sur une paire
mutuelle (`02`↔`04`, `04`↔`05`), les deux briques ne peuvent pas être à jour l'une de
l'autre en même temps : celle qui n'a pas été écrite en dernier porte forcément la version
précédente de l'autre. Un retard d'**une** version est ce coût structurel — avertissement.
L'erreur de `03`, elle, est un retard de **deux** versions : celle-là est un vrai oubli.

**Ce jeu d'essai sort donc en exit 1, et c'est le comportement attendu.** Un jour où il
sortira en exit 0, c'est que quelqu'un l'aura « réparé » — et il faudra alors soit revenir
en arrière, soit réécrire ce README pour dire ce qu'il démontre à la place.

Ne pas « corriger » ce fichier sans supprimer ce paragraphe — le jeu d'essai perdrait son
intérêt principal.

## Vérification

```bash
python3 <chemin-du-plugin>/scripts/check_dossier.py jpo-800
```

Attendu : **exit 1**, une seule erreur, celle du `lu:` périmé de `03-prestataires.md`,
plus les deux avertissements de cycle ci-dessus. Toute **erreur** supplémentaire est une
vraie régression.

## Ce qu'il ne faut pas y chercher

- **Des prix de marché.** Les montants sont des ordres de grandeur cohérents entre eux,
  pas une base tarifaire. Ne jamais les réutiliser comme référence de chiffrage.
- **Du droit.** Les points réglementaires (régime d'ouverture au public, effectif
  autorisé, débit de boissons, SACEM) sont formulés comme **points à faire vérifier**,
  jamais comme règles établies. C'est le comportement attendu du plugin, et il doit le
  rester dans toute évolution du jeu d'essai.
- **Un dossier complet.** Trois briques sur huit manquent, dix lots sur douze ne sont pas
  sourcés, l'annuaire est vide à 100 % et le budget dépasse son enveloppe de 27,6 %.
  Un dossier à J-71 ressemble à ça.
