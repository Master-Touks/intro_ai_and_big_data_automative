# Cas d'usage concrets dans l'automobile

## Durée : 2h30

---

## Objectifs de ce module

- Découvrir des applications concrètes d'IA dans l'automobile
- Comprendre comment l'IA résout des problèmes réels
- Analyser des cas d'usage adaptés à votre contexte (Stellantis/Renault)
- Pratiquer avec des données réelles

---

## 1. IA pour la maintenance prédictive

### Contexte

**Problème traditionnel :**
- Maintenance préventive (calendaire) : Remplacer pièces à intervalles fixes
- Coûteux : Changement de pièces encore bonnes
- Inefficace : Certaines pannes surviennent entre deux révisions

**Solution IA : Maintenance prédictive**
- Prédire quand une pièce va tomber en panne
- Intervenir juste avant la défaillance
- Optimiser coûts et satisfaction client

---

### Fonctionnement

```
Données collectées → Modèle ML → Prédiction → Action
```

**1. Collecte de données**
- Capteurs en continu (température, vibrations, pression)
- Historique de pannes
- Conditions d'utilisation

**2. Entraînement du modèle**
- Algorithme : Random Forest, XGBoost
- Apprentissage supervisé
- Label : Panne dans les N prochains jours (oui/non)

**3. Déploiement**
- Prédiction en temps réel ou quotidienne
- Score de risque par véhicule/composant

**4. Action**
- Alerter le conducteur
- Planifier intervention SAV
- Commander pièces en avance

---

### Exemple concret : Prédiction de défaillance batterie

**Données utilisées :**
- Voltage
- Température
- Nombre de cycles de charge
- Âge de la batterie
- Conditions climatiques

**Modèle :**
- Random Forest avec 50 arbres
- Entraîné sur 100 000 véhicules
- Prédiction : Défaillance dans les 30 jours

**Résultats :**
- Précision : 85%
- Rappel : 92% (détecte 92% des pannes)
- Réduction des pannes imprévues : 60%

---

### ROI (Return on Investment)

**Coûts :**
- Infrastructure IoT : 1 M€
- Développement modèle : 500 k€
- Maintenance annuelle : 200 k€/an
- **Total première année : 1,7 M€**

**Gains (flotte de 500 000 véhicules) :**
- Réduction pannes imprévues : 5 M€/an
- Optimisation stock pièces : 1 M€/an
- Amélioration satisfaction client : 2 M€/an (estimé)
- **Total gains : 8 M€/an**

**ROI : (8 - 1,7) / 1,7 = 370%**
**Retour sur investissement en 3 mois !**

---

### Challenges techniques

#### 1. Qualité des données
- Capteurs défaillants → Données manquantes
- Variabilité environnementale (froid, chaleur)
- Biais de sélection (historique incomplet)

#### 2. Déséquilibre des classes
- 99% de "pas de panne" vs 1% de "panne"
- Modèle qui prédit toujours "pas de panne" = 99% précision mais inutile !
- Solution : SMOTE, ajustement des poids, métriques appropriées

#### 3. Explicabilité
- "Le modèle dit de changer la batterie" → Pourquoi ?
- Importance pour la confiance des mécaniciens
- Solution : SHAP values, feature importance

---

### Cas pratique : Notebook Python

**→ Passage au notebook**

`notebooks/02_maintenance_predictive.ipynb`

Nous allons :
1. Charger des données de télémétrie
2. Préparer les features
3. Entraîner un modèle de prédiction de pannes
4. Évaluer la performance
5. Identifier les véhicules à risque

---

## 2. Analyse comportementale des conducteurs

### Objectif

**Comprendre comment les conducteurs utilisent leurs véhicules**

**Applications :**
- **Assurance** : Tarification personnalisée (Pay How You Drive)
- **Sécurité** : Détecter conduite dangereuse, alerter
- **Marketing** : Segmentation pour offres ciblées
- **Produit** : Adapter fonctionnalités aux usages

---

### Données collectées

**Comportement de conduite :**
- Accélérations / Freinages brusques
- Vitesse moyenne et maximale
- Temps passé sur autoroute vs ville
- Nombre de virages serrés
- Utilisation du régulateur de vitesse

**Contexte :**
- Horaires de conduite (jour/nuit, semaine/week-end)
- Conditions météo
- Type de routes

**Véhicule :**
- Kilométrage annuel
- Utilisation ADAS
- Consommation carburant

---

### Approche : Clustering (Apprentissage non supervisé)

**Algorithme : K-Means**

**Processus :**
1. Normaliser les données (toutes variables sur même échelle)
2. Choisir K (nombre de groupes) via méthode du coude
3. Exécuter K-Means
4. Interpréter les clusters

**Résultat : 4 profils de conducteurs**

---

### Les 4 profils identifiés

#### 1. Le Prudent (30% des conducteurs)
- Vitesse faible
- Peu d'accélérations/freinages brusques
- Forte utilisation ADAS
- Faible kilométrage (10 000 km/an)
- **Profil** : Conducteur urbain, senior, débutant

#### 2. Le Routier (25%)
- Haute vitesse moyenne (stable)
- Kilométrage élevé (30 000+ km/an)
- Majoritairement autoroute
- Utilisation intensive régulateur
- **Profil** : Commercial, VRP

---

#### 3. Le Sportif (15%)
- Accélérations fréquentes
- Vitesse élevée avec variations
- Peu d'utilisation ADAS
- Conduite dynamique
- **Profil** : Jeune, passionné automobile

#### 4. Le Mixte (30%)
- Comportement intermédiaire
- Adapte conduite selon contexte
- Kilométrage moyen (15 000 km/an)
- **Profil** : Usage familial standard

---

### Applications business

#### Assurance
**Tarification personnalisée :**
- Prudent : -20% de réduction
- Sportif : +30% de majoration
- Suivi en temps réel : Réduction progressive si amélioration

**Résultat :**
- Meilleure adéquation risque/prime
- Incitation à la conduite sûre
- Réduction de 15% de la sinistralité (étude Allianz)

---

#### Marketing & CRM
**Offres ciblées :**
- Prudent : Garantie étendue, services assistance
- Routier : Offres pneumatiques, programme fidélité km
- Sportif : Options sportives, stages pilotage
- Mixte : Offres familiales

**Amélioration du taux de conversion : +40%**

---

#### Développement produit
**Priorisation fonctionnalités :**
- ADAS avancés → Cible : Prudent et Mixte (60% du marché)
- Modes de conduite personnalisables → Cible : Sportif
- Optimisation autonomie → Cible : Routier

**Réduction du time-to-market grâce à focus sur segments clés**

---

### Considérations éthiques et RGPD

#### Protection de la vie privée

**Données sensibles :**
- Localisation : Où habite le conducteur, où va-t-il ?
- Comportement : Profil psychologique indirect

**Obligations RGPD :**
- ✅ Consentement explicite
- ✅ Transparence (que faites-vous des données ?)
- ✅ Droit à l'oubli
- ✅ Portabilité des données
- ✅ Minimisation (collecter seulement le nécessaire)

---

#### Bonnes pratiques

1. **Anonymisation** : Pas de lien direct identité ↔ données
2. **Agrégation** : Analyser au niveau population, pas individu
3. **Purpose limitation** : Utiliser uniquement pour l'objectif annoncé
4. **Opt-in** : Système désactivé par défaut
5. **Transparence** : Dashboard pour voir ses propres données

**Exemple Renault : "My Renault" app**
- Conducteur visualise son profil
- Peut désactiver partage données
- Reçoit conseils d'éco-conduite

---

## 3. Optimisation logistique et chaîne d'approvisionnement

### Contexte automobile

**Complexité :**
- 30 000 pièces par véhicule
- 500+ fournisseurs
- Réseau mondial (usines en Europe, Asie, Amérique)
- Just-in-Time (stock minimal pour réduire coûts)

**Risques :**
- Rupture de stock → Arrêt chaîne de production (coût : 1 M€/jour)
- Surstock → Immobilisation financière
- Prévisions de demande erronées → Invendus ou manque à vendre

---

### Applications de l'IA

#### 1. Prévision de la demande

**Algorithme : Time Series Forecasting (ARIMA, LSTM)**

**Données :**
- Historique des ventes (5 ans)
- Saisonnalité
- Indicateurs économiques (pouvoir d'achat, prix carburant)
- Tendances marché (électrification, SUV)
- Campagnes marketing

**Résultat :**
- Prédiction mensuelle des ventes par modèle
- Précision : 92% (vs 78% avec méthode traditionnelle)
- Réduction invendus : 20%

---

#### 2. Optimisation des stocks

**Algorithme : Reinforcement Learning**

**Objectif :** Minimiser coût total = coût stock + coût rupture

**Agent IA apprend :**
- Quand commander
- Quelle quantité
- Quels fournisseurs prioriser

**Gain :**
- Réduction de 30% du stock moyen
- Réduction de 50% des ruptures
- Économies : 50 M€/an (groupe automobile)

---

#### 3. Optimisation des tournées de livraison

**Problème : Vehicle Routing Problem (VRP)**
- 500 concessionnaires à livrer
- Flotte de 50 camions
- Contraintes : horaires, capacité, coûts

**Algorithme : Optimisation combinatoire + ML**
- Recherche locale
- Algorithmes génétiques
- Apprentissage des patterns historiques

**Résultat :**
- Réduction de 15% de la distance parcourue
- Réduction de 20% des délais de livraison
- Économies carburant : 2 M€/an

---

#### 4. Prédiction de défaillance fournisseur

**Contexte : Covid-19 et pénurie semi-conducteurs**

**IA pour anticiper les risques :**
- Analyse sentiment (news, réseaux sociaux)
- Données financières fournisseurs
- Événements géopolitiques
- Météo (catastrophes naturelles)

**Alerte précoce :**
- 3 mois avant rupture de chaîne
- Temps de trouver fournisseur alternatif
- Éviter arrêt production

**Valeur : Incalculable (pénurie 2021 = perte 10 Md€ industrie auto)**

---

## 4. Étude de cas : IA embarquée dans véhicules connectés

### Architecture d'un véhicule connecté moderne

```
┌─────────────────────────────────────────┐
│         VÉHICULE CONNECTÉ               │
│                                         │
│  ┌──────────────────────────────────┐  │
│  │   Edge AI (Calculateurs)         │  │
│  │   - ADAS                         │  │
│  │   - Reconnaissance vocale        │  │
│  │   - Monitoring temps réel        │  │
│  └──────────────────────────────────┘  │
│                 ↕                       │
│  ┌──────────────────────────────────┐  │
│  │   Connectivité (4G/5G)           │  │
│  └──────────────────────────────────┘  │
│                 ↕                       │
└─────────────────────────────────────────┘
                  ↕
┌─────────────────────────────────────────┐
│         CLOUD BACKEND                   │
│  - Machine Learning (entraînement)      │
│  - Big Data Analytics                   │
│  - Mises à jour OTA                     │
│  - Services connectés                   │
└─────────────────────────────────────────┘
```

---

### Cas d'usage 1 : Détection de somnolence

**Edge AI (dans le véhicule) :**

**Capteurs :**
- Caméra infrarouge (visage conducteur)
- Volant (microvibrations)
- Voie (déviations)

**Algorithme : Deep Learning (CNN)**
- Détection du visage
- Reconnaissance expressions (yeux fermés, bâillements)
- Analyse posture

**Pipeline temps réel :**
1. Capture image (30 FPS)
2. Détection visage (10 ms)
3. Classification niveau de vigilance (5 ms)
4. Décision (5 ms)
5. **Alerte en < 100 ms**

---

**Pourquoi Edge AI (local) et pas Cloud ?**

❌ **Cloud :**
- Latence : 200-500 ms (inacceptable)
- Dépendance connectivité (tunnels, zones blanches)
- Coût data
- Vie privée (caméra → cloud = sensible)

✅ **Edge AI :**
- Latence < 100 ms
- Fonctionne hors connexion
- Pas de transfert données sensibles
- Pas de coût data

**Trade-off :** Modèle plus simple (contraintes matériel) mais suffisant

---

### Cas d'usage 2 : Mise à jour Over-The-Air (OTA)

**Problématique traditionnelle :**
- Rappel constructeur = véhicules en concession
- Coût : 100-500€ par véhicule
- Satisfaction client faible

**Solution OTA (Tesla, pionnier) :**
- Mise à jour logiciel via Internet
- Déploiement en quelques jours
- Coût marginal

---

**Architecture :**

```
1. Développement nouvelle version firmware
2. Tests simulation + véhicules pilotes
3. Déploiement progressif :
   - Phase 1 : 1% flotte (bêta testeurs)
   - Phase 2 : 10% si OK
   - Phase 3 : 100%
4. Monitoring anomalies en temps réel
5. Rollback si problème détecté
```

**IA impliquée :**
- Détection d'anomalies post-mise à jour
- Prédiction de compatibilité (hardware, version OS)
- Optimisation de l'ordre de déploiement (priorité zones géo)

---

**Exemple concret : Stellantis**

**Mise à jour ADAS (Août 2024) :**
- Amélioration détection piétons (nouveau modèle Deep Learning)
- 500 000 véhicules concernés
- Déployé en 2 semaines
- Économies vs rappel classique : 150 M€

**Bénéfices au-delà du coût :**
- Amélioration continue des véhicules
- Ajout de nouvelles fonctionnalités post-achat
- Correction de bugs de sécurité rapide

---

### Cas d'usage 3 : Assistant vocal intelligent

**Évolution :**
- **Génération 1 (2010)** : Commandes prédéfinies ("Appelle Jean")
- **Génération 2 (2015)** : Reconnaissance langage naturel (Siri, Google)
- **Génération 3 (2023)** : LLM (ChatGPT-like) embarqués

**Nouvelle génération avec LLMs :**

**Exemple de dialogue :**
```
Conducteur : "Il fait chaud ici"
IA : "Je mets la climatisation à 21°C"

Conducteur : "Trouve-moi un restaurant italien pas trop loin"
IA : "J'ai trouvé 3 restaurants italiens dans un rayon de 5 km.
     Le mieux noté est Bella Vita, à 7 minutes.
     Voulez-vous que je vous y guide ?"

Conducteur : "Oui, et appelle-les pour réserver une table"
IA : "J'appelle Bella Vita... [Conversation téléphonique automatisée]
     Réservation confirmée pour 20h, 2 personnes."
```

---

**Architecture hybride Edge + Cloud :**

**Edge (dans véhicule) :**
- Commandes simples (climat, musique, navigation)
- Modèle léger (< 1 Go)
- Latence < 500 ms

**Cloud :**
- Requêtes complexes (recherche, réservation)
- Modèle complet (GPT-4, Claude)
- Latence 2-3 secondes (acceptable)

**Bascule intelligente :**
- IA décide edge vs cloud selon requête
- Mode dégradé si pas de connexion

---

### Challenges de l'IA embarquée

#### 1. Contraintes matérielles
- CPU/GPU limitée (coût, consommation)
- Mémoire restreinte (< 8 Go)
- Températures extrêmes (-40°C à +85°C)

**Solutions :**
- Quantification des modèles (réduire poids)
- Pruning (supprimer neurones peu utiles)
- Hardware spécialisé (NPU - Neural Processing Unit)

---

#### 2. Certification et sécurité
- Norme ISO 26262 (sécurité fonctionnelle)
- Véhicules = systèmes critiques
- Modèle IA doit être déterministe et testable

**Approches :**
- Tests exhaustifs (milliards de scénarios en simulation)
- Redondance (capteurs multiples)
- Fallback sur système classique si IA défaillante

---

#### 3. Explicabilité
- "Pourquoi l'IA a freiné ?" → Doit pouvoir expliquer
- Crucial pour confiance conducteur
- Obligatoire pour certification

**Techniques :**
- Attention maps (Deep Learning)
- LIME, SHAP (explication locale)
- Logging détaillé pour analyse post-incident

---

## Comparaison des cas d'usage

| Cas d'usage | Type ML | Où | Latence | Principale difficulté |
|-------------|---------|----|---------|-----------------------|
| **Maintenance prédictive** | Supervisé | Cloud | Heures/jours | Qualité données, déséquilibre |
| **Analyse conducteurs** | Non supervisé | Cloud | Temps réel | Interprétation, éthique |
| **Optimisation logistique** | Renforcement | Cloud | Minutes | Complexité combinatoire |
| **Détection somnolence** | Deep Learning | Edge | < 100 ms | Contraintes hardware |
| **OTA** | Anomaly detection | Cloud | Minutes | Fiabilité, rollback |
| **Assistant vocal** | LLM | Hybride | < 3 s | Compréhension contexte |

---

## Points clés à retenir

### IA résout des problèmes business réels

1. **Maintenance prédictive** : ROI 370% en réduisant pannes imprévues
2. **Analyse comportementale** : Personnalisation offres, +40% conversion
3. **Logistique** : 30% réduction stocks, 50 M€ économies
4. **IA embarquée** : Sécurité, confort, mises à jour continues

---

### Architecture : Edge vs Cloud

**Edge (véhicule) :**
- Temps réel critique (< 100 ms)
- Pas de dépendance réseau
- Contraintes hardware

**Cloud (backend) :**
- Entraînement modèles
- Analyses complexes
- Big Data

**Hybride = Optimal**

---

### Défis transverses

1. **Qualité des données** : GIGO (Garbage In, Garbage Out)
2. **Éthique et RGPD** : Consentement, transparence
3. **Explicabilité** : Confiance et certification
4. **ROI** : Mesurer valeur créée

---

## Discussion collective (20 min)

### Questions à débattre :

1. **Dans votre service (développement calculateurs), quels cas d'usage IA seraient les plus utiles ?**
   - Analyse logs de compilation ?
   - Génération de tests ?
   - Détection de bugs ?
   - Optimisation de code ?

2. **Quels sont les principaux freins à l'adoption d'IA chez Stellantis/Renault ?**
   - Compétences ?
   - Données ?
   - Infrastructure ?
   - Culture d'entreprise ?

3. **Éthique : Jusqu'où aller dans la surveillance du conducteur ?**

---

## Pause - 15 minutes

**À suivre :**
- Évaluer un projet IA (méthodologie complète)
- Identifier des biais et risques
- Atelier pratique d'analyse critique

---

## Ressources complémentaires

### Articles de référence
- "Predictive Maintenance in Automotive Industry" - McKinsey
- "Tesla's Over-the-Air Updates" - MIT Technology Review
- "Ethics of Driver Monitoring Systems" - Nature

### Entreprises à suivre
- **Waymo** : Conduite autonome (Alphabet)
- **Mobileye** : Vision pour ADAS (Intel)
- **Aurora** : Trucks autonomes
- **Rivian** : Électrique + Software-defined vehicle

### Standards
- ISO 26262 : Sécurité fonctionnelle automobile
- ISO/SAE 21434 : Cybersécurité automobile
- RGPD : Protection des données personnelles
