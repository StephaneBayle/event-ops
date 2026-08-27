# Obligations réglementaires d'un événement — référence de conformité

Source de vérité unique du plugin event-ops pour la **conformité**. Les skills
`event-conformite` et `event-retroplanning` doivent **PARCOURIR ce fichier entrée par
entrée**, et non le résumer de mémoire.

> **Ce fichier prépare la vérification, il ne la remplace pas.**
> Il ne dit pas le droit : il dit **quelle question poser, à qui, et avant quand**.
> Aucune entrée ne conclut « c'est conforme » — cette conclusion appartient à un humain
> identifié (gestionnaire du lieu, service de sécurité de la mairie, assureur, juriste,
> délégué à la protection des données). C'est l'application directe de la lentille 6 de
> `chantiers.md` : **ne jamais affirmer une règle de droit dont on n'est pas sûr.**

**Dernière vérification du contenu** : 2026-08-27 ·
**Relu par** : *personne* — rédaction initiale, relecture professionnelle à planifier.

Ces deux lignes sont **lues par `scripts/check_plugin.py`**, qui avertit tant que le
relecteur est « personne », et au-delà de douze mois sans vérification. Un fichier de
référence réglementaire vieillit en silence : c'est le seul défaut de ce fichier qu'aucune
relecture de sa structure ne peut attraper. Quand quelqu'un de qualifié l'a relu, son nom
remplace « personne » et la date passe à celle de la relecture.

**Périmètre : droit français, événement organisé en France.** Hors de France, rien de ce
fichier n'est transposable tel quel : tout est à revalider localement, et c'est à dire
explicitement dans le registre produit.

Les **ancres de vérification** citées ci-dessous sont des **points d'entrée pour
chercher**, jamais des citations faisant foi. Un texte se modifie ; un numéro d'article
recopié de mémoire est faux tôt ou tard. L'ancre sert à savoir quoi taper dans
Légifrance et quoi demander à l'interlocuteur — pas à trancher.

---

## Mode d'emploi (les 6 familles)

Les régimes sont regroupés par **ce qui les déclenche**, et non par autorité : c'est le
déclencheur qu'on sait lire dans une fiche d'identité.

1. **Lieu & public** — se déclenche dès qu'il y a un bâtiment et du public. C'est la
   famille qui commande le **go/no-go** : un avis défavorable de commission de sécurité
   n'a pas de plan B de dernière minute.
2. **Affluence & sûreté** — se déclenche au volume et à la configuration (voie publique,
   filtrage). Les seuils sont des seuils *réglementaires*, pas des seuils de confort.
3. **Restauration & boissons** — se déclenche dès qu'on sert à manger ou à boire, y
   compris gratuitement, y compris « juste un café et des viennoiseries ».
4. **Contenu, image & nuisances** — se déclenche par ce qui est diffusé : musique,
   captation, niveau sonore.
5. **Données personnelles** — se déclenche à la première inscription collectée. Souvent
   le dernier vu, alors qu'il commence le plus tôt.
6. **Contrats, travail & assurances** — se déclenche par les tiers qui interviennent :
   prestataires, artistes, bénévoles, entreprises extérieures.

Règle de sortie, identique à celle de `chantiers.md` : chaque régime est **applicable**,
**non applicable et pourquoi**, ou **indéterminé faute d'information**. Jamais laissé
vide en silence, et jamais marqué « conforme ».

**Un déclencheur peut porter plusieurs conditions cumulatives.** Les vérifier toutes, et
noter **laquelle** écarte le régime : « sans objet » sans motif est indistinguable d'un
oubli, et c'est la condition écartante qui redeviendra fausse si l'événement change de
format. Écarter un régime n'écarte pas ses voisins — un régime tombé peut laisser debout
une obligation générale que ce fichier traite ailleurs.

---

## Les 21 régimes

### Famille 1 — Lieu & public

1. **Régime ERP du lieu** — *ancre : code de la construction et de l'habitation, partie
   sécurité incendie des ERP ; arrêté du 25 juin 1980 (règlement de sécurité).*
   - **Se déclenche si** : le lieu reçoit du public. Quel **type** (L salle de
     conférences, N restaurant, T salle d'exposition, W bureaux, X sportif…) et quelle
     **catégorie** (fonction de l'effectif) ? Quel **effectif maximal autorisé** ?
   - **Qui autorise / contrôle** : l'exploitant du lieu détient le registre de sécurité
     et le dernier avis de commission ; le service compétent de la mairie et le SDIS
     instruisent.
   - **Ce qu'il faut produire** : obtenir par écrit le type, la catégorie et l'effectif
     maximal autorisé, et les **verser au dossier**.
   - **Délai à anticiper** : immédiat si le lieu le connaît — à demander **dès le
     cadrage**, car c'est cette valeur qui plafonne la jauge et donc le budget.
   - **Si c'est raté** : la jauge commerciale dépasse la jauge réglementaire, et on ne
     s'en aperçoit qu'à la porte le jour J.

2. **Utilisation exceptionnelle d'un local** — *ancre : article GN6 de l'arrêté du
   25 juin 1980.*
   - **Se déclenche si** : le lieu est utilisé **pour autre chose que sa destination**
     (un hall industriel qui reçoit 800 visiteurs, un plateau de bureaux transformé en
     salle de conférences, un gymnase en salon).
   - **Qui autorise / contrôle** : le maire, après avis de la commission de sécurité.
   - **Ce qu'il faut produire** : une demande décrivant l'aménagement, l'effectif prévu,
     les dégagements et les moyens de secours — souvent accompagnée d'un plan.
   - **Délai à anticiper** : **plusieurs semaines**, la commission siégeant à dates
     fixes. Valeur exacte à confirmer auprès du service compétent de la mairie **dès que
     le lieu est arrêté**.
   - **Si c'est raté** : refus d'ouverture au public, sans recours utile à J-2.

3. **Chapiteaux, tentes et structures (CTS)** — *ancre : règlement de sécurité CTS,
   arrêté du 23 janvier 1985.*
   - **Se déclenche si** : une structure temporaire abrite du public (chapiteau, barnum
     de grande taille, structure gonflable, tribune).
   - **Qui autorise / contrôle** : le maire ; le loueur doit détenir un **registre de
     sécurité** et une attestation de conformité de la structure.
   - **Ce qu'il faut produire** : l'extrait du registre de sécurité de la structure, le
     plan d'implantation, l'attestation de montage.
   - **Délai à anticiper** : à traiter avec la demande d'utilisation exceptionnelle, même
     calendrier de commission.
   - **Si c'est raté** : structure non autorisée à recevoir du public — la surface
     louée devient inutilisable.

4. **Sécurité incendie et moyens de secours** — *ancre : arrêté du 25 juin 1980,
   dispositions relatives aux dégagements, au désenfumage et au service de sécurité.*
   - **Se déclenche si** : toujours, dès qu'il y a du public. Les dégagements
     restent-ils libres avec l'aménagement prévu ? Faut-il un **service de sécurité
     incendie** (personnel qualifié présent pendant l'ouverture) ? Qui le finance ?
   - **Qui autorise / contrôle** : l'exploitant du lieu, la commission de sécurité, le
     SDIS.
   - **Ce qu'il faut produire** : plan d'aménagement validé montrant les issues et leur
     largeur, consigne d'évacuation, désignation nominative du service de sécurité.
   - **Délai à anticiper** : le plan doit être arrêté **avant** le passage en
     commission ; le recrutement du service de sécurité suit les délais du prestataire.
   - **Si c'est raté** : un stand ou un buffet posé devant une issue de secours suffit à
     faire fermer.

5. **Accessibilité aux personnes handicapées** — *ancre : loi n° 2005-102 du 11 février
   2005 ; registre public d'accessibilité (décret n° 2017-431 du 28 mars 2017).*
   - **Se déclenche si** : toujours. Quel est l'état d'accessibilité **réel** du lieu, et
     l'aménagement prévu le préserve-t-il (cheminements, places réservées, accès à la
     scène pour un intervenant, sanitaires, signalétique) ? La **communication** est-elle
     accessible (inscription, supports, sous-titrage, boucle magnétique) ?
   - **Qui autorise / contrôle** : l'exploitant du lieu détient le registre public
     d'accessibilité ; les associations d'usagers et les participants constatent.
   - **Ce qu'il faut produire** : consultation du registre public d'accessibilité du
     lieu, et la liste des adaptations retenues **avec leur coût**.
   - **Délai à anticiper** : long dès qu'une adaptation est à commander (interprétation
     LSF, sous-titrage, rampe) — plusieurs semaines, car ces prestataires sont peu
     nombreux.
   - **Si c'est raté** : discrimination constituée, et un participant empêché d'entrer.
     C'est une obligation, pas une option de confort.

6. **Installations électriques et aménagements temporaires** — *ancre : dispositions
   « installations électriques » de l'arrêté du 25 juin 1980 ; obligations de l'employeur
   sur les installations temporaires.*
   - **Se déclenche si** : on ajoute de la puissance, des groupes électrogènes, des
     câblages au sol, des matériaux de décoration ou de la scénographie.
   - **Qui autorise / contrôle** : l'exploitant du lieu, le prestataire technique, un
     organisme de vérification si le lieu ou la commission l'exige.
   - **Ce qu'il faut produire** : bilan de puissance, attestation du prestataire
     technique, **classement au feu des matériaux** de décoration et de scénographie.
   - **Délai à anticiper** : à demander au prestataire technique dès la commande.
   - **Si c'est raté** : réserve en commission, ou refus de mise sous tension au montage.

### Famille 2 — Affluence & sûreté

7. **Grands rassemblements et service d'ordre** — *ancre : décret n° 97-646 du 31 mai
   1997 relatif au service d'ordre des manifestations sportives, récréatives ou
   culturelles **à but lucratif**.*
   - **Se déclenche si** : **deux conditions, à vérifier l'une et l'autre.** D'abord, la
     manifestation poursuit-elle un **but lucratif au sens du texte** ? La question se
     pose avant celle du seuil, et sa réponse n'a rien d'évident pour une journée portes
     ouvertes ou une convention interne — c'est au vérificateur nommé de la trancher, pas
     à ce fichier. Ensuite seulement : le nombre de personnes attendues franchit-il le
     seuil fixé par le texte ? **Le seuil est à relever dans le texte, pas de mémoire** —
     il se compte en personnes présentes simultanément, participants et personnel compris.
   - **Qui autorise / contrôle** : le maire, et le préfet selon la nature de la
     manifestation.
   - **Ce qu'il faut produire** : une déclaration décrivant la manifestation, l'effectif
     attendu et le service d'ordre mis en place.
   - **Délai à anticiper** : de l'ordre du mois avant la date ; valeur exacte à confirmer
     auprès de la mairie.
   - **Si c'est raté** : manifestation non déclarée — interdiction possible, et
     responsabilité pleine de l'organisateur en cas d'incident. **Et dans l'autre sens :
     régime écarté ne veut pas dire rien à faire.** Le service d'ordre peut tomber hors de
     ce décret sans que disparaissent les pouvoirs de police générale du maire, le
     dispositif de secours (régime 9) ni l'occupation du domaine public (régime 10). Note
     le motif d'écartement, jamais un simple « non concerné ».

8. **Sécurité privée et agents** — *ancre : livre VI du code de la sécurité intérieure ;
   agrément CNAPS ; régime des palpations de sécurité.*
   - **Se déclenche si** : on fait appel à des agents de sécurité, ou on met en place un
     **filtrage** (contrôle d'accès, inspection visuelle des sacs, palpation).
   - **Qui autorise / contrôle** : le CNAPS pour l'autorisation de l'entreprise et les
     cartes professionnelles des agents ; le préfet pour l'agrément permettant les
     palpations ; le participant, dont le **consentement** est requis.
   - **Ce qu'il faut produire** : autorisation d'exercer de l'entreprise, cartes
     professionnelles des agents affectés, et la note écrite de ce que les agents ont le
     droit de faire — et de ne pas faire.
   - **Délai à anticiper** : à la contractualisation du prestataire ; les pièces se
     vérifient **avant** la signature, pas au montage.
   - **Si c'est raté** : filtrage illégal, agents non habilités, et un incident dont la
     couverture d'assurance saute.

9. **Dispositif prévisionnel de secours (DPS)** — *ancre : référentiel national des
   dispositifs prévisionnels de secours.*
   - **Se déclenche si** : l'affluence, la durée, la nature du public ou l'éloignement
     des secours le justifient. L'évaluation est **à la charge de l'organisateur**, même
     quand aucun texte n'impose de dispositif.
   - **Qui autorise / contrôle** : l'association agréée de sécurité civile qui réalise
     l'évaluation ; le préfet et le SDIS en sont destinataires.
   - **Ce qu'il faut produire** : la grille d'évaluation des risques renseignée, puis la
     convention avec l'association agréée.
   - **Délai à anticiper** : plusieurs semaines — les équipes de secouristes se réservent
     tôt, surtout en haute saison.
   - **Si c'est raté** : aucun moyen de secours sur place au premier malaise, et une
     responsabilité difficile à défendre.

10. **Voie publique et domaine public** — *ancre : pouvoirs de police du maire (code
    général des collectivités territoriales) ; autorisation d'occupation temporaire du
    domaine public.*
    - **Se déclenche si** : quoi que ce soit déborde de la propriété privée — file
      d'attente sur le trottoir, signalétique, stationnement réservé, navette, dépose
      minute, camion du traiteur, fléchage.
    - **Qui autorise / contrôle** : la mairie (voirie, occupation du domaine public,
      police municipale).
    - **Ce qu'il faut produire** : demande d'autorisation d'occupation, plan de
      circulation et de stationnement, arrêté municipal le cas échéant.
    - **Délai à anticiper** : plusieurs semaines, et une **redevance** possible — à
      inscrire au budget.
    - **Si c'est raté** : fléchage retiré, camion verbalisé, file d'attente dispersée.

### Famille 3 — Restauration & boissons

11. **Hygiène alimentaire et chaîne du froid** — *ancre : règlement (CE) n° 852/2004 ;
    obligation de déclaration de l'établissement.*
    - **Se déclenche si** : on sert à manger, **y compris gratuitement**, y compris un
      simple buffet de viennoiseries.
    - **Qui autorise / contrôle** : les services vétérinaires et de protection des
      populations ; le traiteur porte ses propres obligations.
    - **Ce qu'il faut produire** : la preuve que le traiteur est déclaré, son plan de
      maîtrise sanitaire, et **les conditions de maintien en température sur site** —
      c'est le point qui casse quand la cuisine est à trente kilomètres.
    - **Délai à anticiper** : à demander avec le devis, pas après.
    - **Si c'est raté** : intoxication collective — le risque le plus lourd de tout le
      dossier, et le plus banal.

12. **Information sur les allergènes** — *ancre : règlement (UE) n° 1169/2011 (INCO) et
    ses dispositions sur les denrées non préemballées.*
    - **Se déclenche si** : on sert à manger. L'information sur les allergènes est due
      **même pour un buffet**, et même sans vente.
    - **Qui autorise / contrôle** : les services de protection des populations ; le
      traiteur fournit l'information, l'organisateur la met à disposition.
    - **Ce qu'il faut produire** : l'étiquetage ou l'affichage par plat, et la manière
      dont l'information est portée au public sur place.
    - **Délai à anticiper** : à exiger au cahier des charges, à vérifier à la réception
      de prestation.
    - **Si c'est raté** : un participant allergique sans information — et une
      responsabilité qui ne se transfère pas au traiteur par un simple contrat.

13. **Débit de boissons temporaire** — *ancre : code de la santé publique, classement des
    boissons par groupes, autorisations temporaires, interdiction de vente aux mineurs.*
    - **Se déclenche si** : on sert de l'alcool, **même offert**. Quel groupe de
      boissons ? Le lieu dispose-t-il déjà d'une licence ? Y a-t-il des mineurs présents ?
    - **Qui autorise / contrôle** : le maire pour l'autorisation temporaire ; la police
      municipale et les services de l'État contrôlent.
    - **Ce qu'il faut produire** : la demande d'autorisation temporaire, l'affichage de
      l'interdiction de vente aux mineurs, et la consigne donnée au personnel de bar.
    - **Délai à anticiper** : de l'ordre de quelques semaines ; le nombre d'autorisations
      annuelles peut être **limité** pour une association — à vérifier tôt.
    - **Si c'est raté** : débit illégal, et une responsabilité personnelle en cas
      d'accident sur le trajet de retour.

### Famille 4 — Contenu, image & nuisances

14. **Droits d'auteur et musique** — *ancre : code de la propriété intellectuelle ;
    SACEM pour les droits d'auteur, SPRE pour la rémunération équitable des
    enregistrements.*
    - **Se déclenche si** : de la musique est diffusée — playlist d'accueil comprise,
      musique d'attente comprise, générique de vidéo compris.
    - **Qui autorise / contrôle** : la SACEM (déclaration préalable) ; la SPRE pour les
      enregistrements du commerce ; d'autres sociétés selon le répertoire.
    - **Ce qu'il faut produire** : la déclaration préalable et le programme des œuvres ;
      la **redevance** est une ligne budgétaire, pas un imprévu.
    - **Délai à anticiper** : déclaration avant l'événement — un tarif majoré s'applique
      généralement à la déclaration tardive.
    - **Si c'est raté** : redevance majorée, et contrefaçon caractérisée.

15. **Niveaux sonores** — *ancre : réglementation des lieux diffusant des sons amplifiés
    (code de la santé publique).*
    - **Se déclenche si** : sonorisation d'un concert, d'une soirée dansante, d'un
      spectacle. **Les valeurs plafonds et les obligations associées (enregistrement des
      niveaux, affichage, protections auditives, zone de repos) sont à relever dans le
      texte en vigueur** — ne pas les citer de mémoire.
    - **Qui autorise / contrôle** : l'agence régionale de santé, la mairie ; le
      prestataire son applique.
    - **Ce qu'il faut produire** : l'engagement écrit du prestataire son, et l'étude
      d'impact des nuisances si le lieu ou la mairie l'exige.
    - **Délai à anticiper** : à porter au cahier des charges du prestataire technique.
    - **Si c'est raté** : arrêt de la diffusion en cours de soirée sur plainte du
      voisinage.

16. **Droit à l'image et captation** — *ancre : droit au respect de la vie privée (code
    civil) ; autorisation des titulaires de l'autorité parentale pour les mineurs.*
    - **Se déclenche si** : photo, vidéo, streaming, replay, photocall — dès qu'un visage
      est reconnaissable et que l'image sera diffusée.
    - **Qui autorise / contrôle** : chaque personne filmée ; les parents pour un mineur ;
      le photographe cède ses droits par contrat.
    - **Ce qu'il faut produire** : mention à l'inscription, **signalétique des zones
      captées** à l'entrée, autorisations écrites pour les intervenants et les plans
      individualisés, cession de droits du photographe.
    - **Délai à anticiper** : la mention doit exister **avant l'ouverture des
      inscriptions** — elle ne se rattrape pas après coup.
    - **Si c'est raté** : retrait des photos exigé après diffusion, et la communication
      d'après-événement s'effondre.

### Famille 5 — Données personnelles

17. **Traitement des données des participants (RGPD)** — *ancre : règlement (UE)
    2016/679 — base légale, information des personnes, contrat de sous-traitance,
    catégories particulières de données, registre des traitements.*
    - **Se déclenche si** : une seule inscription est collectée. Quelle **base légale** ?
      Quelle **durée de conservation** ? Qui héberge (plateforme de billetterie, tableur
      partagé, badges) et **où** ? Les **régimes alimentaires et besoins d'accessibilité
      sont des données sensibles** : les traiter comme telles, séparément, et les
      détruire après l'événement.
    - **Qui autorise / contrôle** : le délégué à la protection des données de
      l'organisation s'il existe ; la CNIL contrôle ; chaque participant exerce ses
      droits.
    - **Ce qu'il faut produire** : mention d'information au formulaire, inscription au
      registre des traitements, **contrat de sous-traitance avec la plateforme**,
      procédure de purge après l'événement.
    - **Délai à anticiper** : **avant l'ouverture des inscriptions** — c'est le régime
      qui commence le plus tôt, et celui qu'on regarde le plus tard.
    - **Si c'est raté** : collecte sans base légale, fichier conservé indéfiniment, et
      une réclamation qui arrive des mois après l'événement.

### Famille 6 — Contrats, travail & assurances

18. **Assurances de l'événement** — *ancre : responsabilité civile de l'organisateur
    (code civil) ; conditions du contrat souscrit.*
    - **Se déclenche si** : toujours. La police existante de l'organisation couvre-t-elle
      **cet** événement (lieu, effectif, activités, alcool, extérieur) ? Faut-il une
      **extension** ? Une assurance **annulation** ? Les **biens loués** (matériel
      technique, mobilier) sont-ils couverts, et par qui ?
    - **Qui autorise / contrôle** : l'assureur de l'organisation ; le gestionnaire du
      lieu, qui exige généralement une attestation ; chaque prestataire pour sa propre RC.
    - **Ce qu'il faut produire** : attestation d'assurance de l'organisateur pour la
      période et le lieu, **et les attestations de RC de chaque prestataire**, collectées
      avant le montage.
    - **Délai à anticiper** : une extension se demande **plusieurs semaines** avant, et
      l'assureur pose des questions auxquelles il faut d'abord répondre.
    - **Si c'est raté** : sinistre non couvert — c'est le seul régime de cette liste dont
      la sanction est directement financière et illimitée.

19. **Intervention d'entreprises extérieures** — *ancre : code du travail — plan de
    prévention pour les travaux réalisés par une entreprise extérieure ; protocole de
    sécurité pour les opérations de chargement et de déchargement.*
    - **Se déclenche si** : des prestataires interviennent dans les locaux (montage,
      accroche, levage, travail en hauteur), ou qu'un transporteur charge et décharge.
      **Le régime dépend de la nature des travaux et du volume d'heures** — à qualifier,
      pas à supposer.
    - **Qui autorise / contrôle** : l'inspection du travail ; le responsable du site,
      qui reste l'entreprise utilisatrice.
    - **Ce qu'il faut produire** : inspection commune préalable, plan de prévention
      écrit quand il est requis, protocole de sécurité pour les livraisons.
    - **Délai à anticiper** : l'inspection commune se tient **avant** le début des
      travaux, donc avant le montage — à placer au rétroplanning.
    - **Si c'est raté** : accident au montage, avec une responsabilité de l'entreprise
      utilisatrice pleinement engagée.

20. **Emploi, rémunération et vigilance** — *ancre : code du travail — guichet unique du
    spectacle occasionnel pour l'emploi d'artistes hors du secteur, licence
    d'entrepreneur de spectacles, attestation de vigilance à réclamer au cocontractant
    au-delà d'un seuil de contrat.*
    - **Se déclenche si** : on rémunère un artiste ou un technicien du spectacle, ou on
      signe un contrat dont le montant dépasse le seuil de vigilance. Un **bénévole**
      n'est pas un salarié : quelles tâches lui confie-t-on, et sous quelle couverture ?
    - **Qui autorise / contrôle** : l'URSSAF ; l'inspection du travail ; le guichet
      unique pour l'emploi occasionnel d'artistes.
    - **Ce qu'il faut produire** : **attestation de vigilance** de chaque prestataire
      au-dessus du seuil, à renouveler pendant l'exécution ; contrats d'engagement des
      artistes ; note de cadrage du bénévolat.
    - **Délai à anticiper** : à la contractualisation, et à renouveler — une attestation
      a une durée de validité.
    - **Si c'est raté** : solidarité financière pour travail dissimulé, dette du
      prestataire mise à la charge de l'organisateur.

21. **Accueil de mineurs** — *ancre : autorisation des titulaires de l'autorité
    parentale ; réglementation des accueils collectifs de mineurs pour les formats qui en
    relèvent.*
    - **Se déclenche si** : des mineurs sont attendus — portes ouvertes, visite scolaire,
      événement familial. Viennent-ils **avec leur établissement** (qui porte alors
      l'encadrement) ou **de leur propre initiative** ? Quel taux d'encadrement ? Que
      fait-on d'un mineur isolé ou d'un mineur blessé ?
    - **Qui autorise / contrôle** : les titulaires de l'autorité parentale ;
      l'établissement scolaire pour une sortie ; les services de l'État selon le format.
    - **Ce qu'il faut produire** : autorisations parentales, convention avec
      l'établissement, consigne écrite pour le mineur isolé et pour l'accès aux zones
      interdites, règle d'accès à l'alcool.
    - **Délai à anticiper** : les autorisations parentales suivent le calendrier de
      l'établissement, plus lent que celui de l'événement.
    - **Si c'est raté** : un mineur sous la responsabilité de personne.

---

## Calendrier des délais

Ordre de grandeur pour poser les jalons — **chaque valeur est à confirmer auprès de
l'interlocuteur nommé**, jamais à reprendre telle quelle. Ce tableau est la matière que
`event-retroplanning` place sur le **chemin critique**.

| Régime | Délai à anticiper | Auprès de qui |
|---|---|---|
| Utilisation exceptionnelle d'un local, CTS | Plusieurs semaines, commission à dates fixes | Service compétent de la mairie, SDIS |
| Dispositif prévisionnel de secours | Plusieurs semaines, réservation des équipes | Association agréée de sécurité civile |
| Adaptations d'accessibilité (LSF, sous-titrage) | Plusieurs semaines, prestataires rares | Prestataires spécialisés |
| Extension d'assurance, assurance annulation | Plusieurs semaines, avec questionnaire préalable | Assureur de l'organisation |
| Grands rassemblements, service d'ordre | De l'ordre du mois | Mairie, préfecture |
| Occupation du domaine public, plan de circulation | Plusieurs semaines, redevance possible | Mairie — voirie |
| Débit de boissons temporaire | Quelques semaines, quota annuel possible | Mairie |
| Mention RGPD et droit à l'image | **Avant l'ouverture des inscriptions** | DPO, juriste |
| Autorisations parentales | Calendrier de l'établissement scolaire | Établissement, familles |
| Déclaration SACEM | Avant l'événement, tarif majoré si tardif | SACEM |
| Attestations d'assurance et de vigilance | À la signature, à renouveler | Chaque prestataire |
| Inspection commune et plan de prévention | Avant le début du montage | Prestataires intervenants |

Deux régimes commencent **plus tôt que le rétroplanning lui-même** : le RGPD et le droit
à l'image, parce qu'ils conditionnent le formulaire d'inscription. Un dossier qui les
découvre en cours de route a déjà collecté des données qu'il faudra reprendre.

## Ce qui reste toujours à l'organisateur

Un prestataire porte **ses** obligations, pas les tiennes. Le contrat répartit la charge
de travail, il ne transfère pas la responsabilité de l'organisateur :

- **La jauge et le régime ERP** ne se délèguent pas au gestionnaire du lieu. C'est
  l'organisateur qui fait entrer les gens.
- **L'accessibilité** ne se délègue pas : le lieu peut être conforme et l'événement
  inaccessible (comptoir trop haut, cheminement encombré, programme non annoncé).
- **L'information sur les allergènes** est due au public même si c'est le traiteur qui la
  produit : l'organisateur doit vérifier qu'elle est effectivement affichée.
- **Les données des participants** restent sous la responsabilité de l'organisateur, la
  plateforme de billetterie n'étant que sous-traitant.
- **La vérification des habilitations** (cartes professionnelles des agents, déclaration
  du traiteur, attestations de vigilance) incombe à celui qui contracte.

Corollaire pratique : chaque ligne du registre porte un **vérificateur humain nommé**.
Une ligne sans vérificateur n'est pas une ligne en cours — c'est un trou.
