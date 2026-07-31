---
name: event-conducteur
description: >
  À utiliser pour la phase PENDANT d'un événement : quand l'utilisateur demande un
  "conducteur", un "run of show", un "minutage du jour J", un "déroulé", un "plan
  de salle", un "annuaire jour J", des "tops régie" ou des "procédures d'escalade".
  Produit la pièce maîtresse de l'exécution : séquencement minuté, tops régie,
  ressources, responsables, et plans de repli.
version: 0.3.0
---

# Conducteur jour J (run of show)

Tu produis l'instrument que l'équipe tient en main sous tension. C'est la partie
que la plupart des dossiers négligent et qui fait toute la différence.

## Dossier

OUVRE `${CLAUDE_PLUGIN_ROOT}/references/convention-dossier.md` et applique-la.
Lis `00-fiche-identite.md`, `01-retroplanning.md`, `03-prestataires.md` et
`04-inscriptions.md` s'ils existent ; écris `05-conducteur.md`.

**Renseigne le champ `lu:`** du frontmatter avec la version de chaque fichier que tu as
effectivement lu : `00-fiche-identite.md`, `01-retroplanning.md`, `03-prestataires.md`,
`04-inscriptions.md`.
C'est ce qui permet de détecter plus tard que tu as travaillé sur une version périmée —
sans lui, personne ne sait sur quoi tu t'es appuyé.

**Le conducteur est le fichier le plus versionné du dossier** — il change dix à quinze
fois entre J-30 et J-1. Incrémente `version` à chaque réécriture et fais figurer
« v<N> — <date> » en tête du document lui-même : l'équipe doit pouvoir vérifier d'un
coup d'œil qu'elle tient la bonne version. Si tu modifies un conducteur existant,
résume les changements depuis la version précédente.

## Méthode

1. **Conducteur minuté** — une ligne par séquence :

   | H début | Durée | H fin | Séquence | Action détaillée | Responsable | Tops régie (son / lumière / vidéo) | Ce que voit et entend le public | Ressources | Signal de transition |

   - La colonne **Durée** n'est pas décorative : c'est elle qui permet de recalculer
     toute la feuille quand une séquence glisse. Sans elle, le moindre retard oblige
     à tout refaire à la main.
   - Les **tops régie** sont la raison pour laquelle la régie tient ce document.
     Sois précis : « top son : lancer jingle 8 s », « lumière : plein feu scène ».
   - **Ce que voit et entend le public** révèle les trous de mise en scène — les
     moments de flottement, d'écran noir, de silence non voulu.
   - Signale explicitement les séquences **compressibles** (celles qu'on peut raccourcir
     si on prend du retard) et celles qui ne le sont pas.
2. **Plan de salle** : zones, flux, points de contrôle d'accès, **cheminements PMR**
   et places réservées, issues de secours.
3. **Annuaire jour J** : contacts opérationnels (nom, rôle, téléphone), regroupés
   par fonction. N'invente jamais un numéro : laisse le champ vide et marque-le
   « à compléter ».
4. **Procédures d'escalade** : pour chaque incident plausible, qui décide et selon
   quel seuil. Format clair « Si X alors Y, décideur = Z ». Inclus obligatoirement
   les décisions lourdes : **interruption, évacuation, annulation en cours
   d'événement** — et qui en a le pouvoir.
5. **PACE planning** pour chaque fonction vitale (son, accès, intervenant clé,
   électricité, connexion pour le distanciel si hybride) : **P**rimary / **A**lternate /
   **C**ontingency / **E**mergency — quatre niveaux de repli.
6. **Volet hybride** — si l'événement est hybride, le distanciel a son propre fil :
   modération du chat, régie de streaming, temps de latence, moment de bascule,
   captation pour rediffusion. Ne le traite pas comme une note en bas de page.
7. **Test du parcours-participant** : suis mentalement chaque persona (VIP,
   intervenant, presse, public, personne à mobilité réduite, prestataire) de
   l'arrivée au départ. Tout point de contact non couvert par le conducteur = un
   trou ; signale-le.

## Sortie

En-tête « v<N> — <date> » + conducteur en tableau chronologique + plan de salle
(description ou schéma) + annuaire + table d'escalade + grille PACE des fonctions
vitales. Termine par les trous détectés et les champs restant à compléter.

Écris `05-conducteur.md` et annonce sa version. Le rendu A4 paysage imprimable pour
la régie est produit par `event-dossier`.
