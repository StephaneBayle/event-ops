# Event-ops Plugin

Plugin Claude pour la gestion d'événements et la production de dossiers opérationnels.

## Structure

- `.claude-plugin/plugin.json` — **manifeste du plugin, source de vérité de la version.**
  Ne pas ajouter de `package.json` : le plugin ne contient aucun code JS.
- `skills/` — les briques, chacune auto-suffisante (aucune dépendance à une skill externe).
- `references/` — fichiers de référence partagés, parcourus par les skills.
  - `chantiers.md` — taxonomie des domaines + lentilles de complétude.
  - `convention-dossier.md` — convention du dossier événement persistant.

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
