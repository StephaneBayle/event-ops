# event-ops

Plugin Claude **auto-suffisant** pour produire et piloter un dossier opérationnel
d'événement, de bout en bout. Aucune dépendance à des skills externes : tout est
embarqué dans le plugin, donc il s'installe et fonctionne à l'identique chez chaque
membre de l'équipe.

## Les six briques

Chaque brique est une *skill* : elle se déclenche automatiquement quand le contexte
de ta phrase correspond à sa description, **et** elle est invocable explicitement
en slash command sous la forme `/event-ops:<nom>`.

| Brique | Phase | Slash command | Produit |
|---|---|---|---|
| `event-cadrage` | Ancre | `/event-ops:event-cadrage` | Fiche d'identité : objectifs, KPIs, public, budget, gouvernance |
| `event-retroplanning` | Avant | `/event-ops:event-retroplanning` | Rétroplanning (chemin critique) + RACI + checklists J-30/J-7/J-1 |
| `event-conducteur` | Pendant | `/event-ops:event-conducteur` | Conducteur minuté + plan de salle + escalade + PACE |
| `event-risques` | Transverse | `/event-ops:event-risques` | Cartographie P×I + pre-mortem + plan de traitement 4T |
| `event-debrief` | Après | `/event-ops:event-debrief` | Bilan KPIs vs objectifs + After-Action Review |
| `event-dossier` | Chapeau | `/event-ops:event-dossier` | Assemble tout en un livrable HTML/docx stylisé |

## Frameworks mobilisés

RACI · chemin critique / rétroplanning · PACE planning · pre-mortem (Klein) ·
parcours-participant (service design) · cotation Probabilité × Impact + 4 T ·
After-Action Review.

## Usage typique

1. Démarrer : `/event-ops:event-cadrage` (ou « cadre-moi le nouvel événement … »).
2. Enchaîner avant / pendant / risques / après au fil du besoin.
3. Finaliser : `/event-ops:event-dossier` pour le dossier complet à diffuser.

Les briques sont indépendantes : on peut n'en appeler qu'une (« fais-moi juste le
conducteur ») sans passer par les autres.
