# Les fondamentaux de l'Intelligence Artificielle

## Durée : 2h30

---

## Objectifs de ce module

- Comprendre les différents types d'apprentissage automatique
- Découvrir les concepts de modèles et algorithmes
- Apprendre à analyser un projet IA de manière critique
- Faire le lien avec vos projets de calculateurs automobiles

---

## Les trois types d'apprentissage automatique

### Vue d'ensemble

```
Intelligence Artificielle
    │
    ├── Machine Learning
    │   ├── Apprentissage supervisé
    │   ├── Apprentissage non supervisé
    │   └── Apprentissage par renforcement
    │
    └── Autres approches (systèmes experts, logique floue...)
```

---

## 1. Apprentissage supervisé

### Principe

> **"Apprendre à partir d'exemples étiquetés"**

**Métaphore :** Un professeur qui montre des exemples avec les bonnes réponses

**Données d'entraînement :**
- Entrées (features) + Sorties attendues (labels)
- Le modèle apprend la relation entre entrées et sorties
- Puis prédit sur de nouvelles données

---

### Exemple automobile : Prédiction de pannes

**Données historiques :**

| Kilométrage | Âge (ans) | T° moyenne moteur | Nb démarrages | **Panne ?** |
|-------------|-----------|-------------------|---------------|-------------|
| 150 000     | 8         | 95°C              | 15 000        | **OUI**     |
| 50 000      | 2         | 88°C              | 5 000         | **NON**     |
| 200 000     | 12        | 98°C              | 25 000        | **OUI**     |
| 80 000      | 4         | 90°C              | 8 000         | **NON**     |

**Le modèle apprend :** Quels facteurs indiquent une panne probable

**Utilisation :** Prédire si un nouveau véhicule va tomber en panne

---

### Les deux grandes familles

#### Classification
**Prédire une catégorie**

**Exemples automobiles :**
- Détection d'obstacle (piéton / véhicule / rien)
- Diagnostic panne (moteur / freins / électronique)
- Qualité de pièce (conforme / non-conforme)
- Gravité d'erreur compilateur (warning / error / critical)

**Algorithmes populaires :**
- Arbres de décision
- Random Forest
- Support Vector Machines (SVM)
- Réseaux de neurones

---

#### Régression
**Prédire une valeur numérique**

**Exemples automobiles :**
- Durée de vie restante d'un composant (en km)
- Consommation carburant prévue
- Temps de compilation estimé
- Température moteur future

**Algorithmes populaires :**
- Régression linéaire
- Régression polynomiale
- Réseaux de neurones
- XGBoost

---

### Cas pratique : Détection d'anomalies dans les logs

**Contexte calculateur moteur :**

Vous avez des logs de compilation :
```
[INFO] Compilation started - Module ECU_Engine_Control
[WARN] Variable 'temp_sensor_value' unused in function check_temperature()
[ERROR] Undefined reference to 'init_can_bus()'
[INFO] Linking object files...
[ERROR] Stack overflow in interrupt handler ISR_Timer2()
```

**Objectif :** Classifier automatiquement la gravité des erreurs

**Approche supervisée :**
1. Annoter manuellement 10 000 lignes de logs (grave / moyen / mineur)
2. Entraîner un modèle de classification
3. Le modèle apprend les patterns de chaque gravité
4. Déployer pour classer automatiquement les nouveaux logs

---

### Métriques de performance

**Comment évaluer un modèle supervisé ?**

#### Matrice de confusion

|                    | **Prédiction Panne** | **Prédiction OK** |
|--------------------|----------------------|-------------------|
| **Réalité Panne**  | Vrais Positifs (VP)  | Faux Négatifs (FN)|
| **Réalité OK**     | Faux Positifs (FP)   | Vrais Négatifs (VN)|

**Métriques clés :**
- **Précision** = VP / (VP + FP) → "Quand je prédis une panne, ai-je raison ?"
- **Rappel** = VP / (VP + FN) → "Est-ce que je détecte toutes les pannes ?"
- **F1-Score** = Moyenne harmonique de Précision et Rappel

**Dans l'automobile, quel est le pire ?**
- Faux Négatif → Ne pas détecter un problème critique (danger !)
- Faux Positif → Alerter alors qu'il n'y a rien (coûteux mais moins grave)

---

## 2. Apprentissage non supervisé

### Principe

> **"Découvrir des structures cachées dans les données sans étiquettes"**

**Métaphore :** Explorer une grotte sans carte, trouver des patterns naturels

**Caractéristiques :**
- Pas de "bonnes réponses" à apprendre
- Le modèle cherche des groupes, des similarités
- Utile pour l'exploration de données

---

### Cas d'usage : Clustering

**Clustering = Regroupement automatique**

**Exemple automobile : Segmentation des conducteurs**

Données collectées de 10 000 conducteurs :
- Vitesse moyenne
- Nombre de freinages brusques
- Kilomètres annuels
- Utilisation autoroute vs ville

**Le modèle découvre automatiquement 4 groupes :**

1. **Conducteurs urbains calmes** : Peu de km, vitesse faible, conduite douce
2. **Conducteurs sportifs** : Freinages fréquents, accélérations rapides
3. **Conducteurs autoroutiers** : Beaucoup de km, vitesse élevée stable
4. **Conducteurs mixtes** : Profil intermédiaire

**Applications :**
- Personnalisation des alertes ADAS
- Tarification d'assurance
- Ciblage marketing

---

### Algorithmes de clustering

#### K-Means
**Le plus populaire**

- Définir K groupes à trouver
- Algorithme itératif qui minimise les distances intra-groupe
- Rapide et simple

#### DBSCAN
**Détection de densité**

- Ne nécessite pas de définir K à l'avance
- Trouve des groupes de forme arbitraire
- Identifie les outliers (points aberrants)

---

### Cas pratique : Analyse de comportements de compilation

**Données :** 1000 builds de calculateurs

Pour chaque build :
- Durée de compilation
- Nombre de warnings
- Nombre d'erreurs
- Taille du binaire final
- Modules modifiés

**Clustering automatique révèle :**

- **Cluster 1** : Builds rapides et propres (développement normal)
- **Cluster 2** : Builds lents avec beaucoup d'erreurs (refactoring)
- **Cluster 3** : Builds moyens mais binaires volumineux (ajout fonctionnalités)
- **Outliers** : Builds anormaux à investiguer

**Bénéfice :** Détecter automatiquement les builds anormaux

---

### Détection d'anomalies

**Application non supervisée importante**

**Principe :**
- Modéliser ce qui est "normal"
- Identifier ce qui s'en écarte

**Exemple : Surveillance de calculateurs en production**

Données en temps réel :
- Température CPU
- Charge processeur
- Erreurs CAN bus
- Temps de réponse

**Le modèle apprend le comportement normal**

**Alerte si :**
- Température soudainement anormale
- Pics de charge inexpliqués
- Pattern de communication inhabituel

**Avantage :** Détecte des problèmes jamais vus avant

---

## 3. Apprentissage par renforcement

### Principe

> **"Apprendre par essais-erreurs et récompenses"**

**Métaphore :** Un enfant qui apprend à faire du vélo en tombant et réessayant

**Composants :**
- **Agent** : Le système qui apprend (ex: voiture autonome)
- **Environnement** : Le monde dans lequel il évolue (route, trafic)
- **Actions** : Ce que l'agent peut faire (accélérer, freiner, tourner)
- **Récompenses** : Feedback (+1 si bien, -1 si mal)
- **État** : Situation actuelle

---

### Fonctionnement

```
1. Observer l'état actuel
2. Choisir une action
3. Exécuter l'action
4. Recevoir une récompense (ou pénalité)
5. Observer le nouvel état
6. Apprendre de cette expérience
7. Répéter
```

**Objectif :** Maximiser la récompense cumulée à long terme

---

### Exemple : Optimisation de trajectoire

**Contexte :** Système de parking automatique

**Agent :** Le calculateur qui contrôle le véhicule

**Actions possibles :**
- Tourner à gauche
- Tourner à droite
- Avancer
- Reculer

**Récompenses :**
- +100 : Se garer correctement
- -10 : Toucher un obstacle
- -1 : Chaque seconde qui passe (pour inciter à la rapidité)
- +10 : Se rapprocher de la place

**Le système apprend :** La séquence d'actions optimale pour se garer

---

### Applications automobiles

#### 1. Conduite autonome
- Apprendre à naviguer dans le trafic
- Optimiser la consommation d'énergie
- Adapter le style de conduite au passager

#### 2. Gestion énergétique (véhicules hybrides)
- Décider quand utiliser moteur thermique vs électrique
- Maximiser l'autonomie
- Apprendre des habitudes du conducteur

#### 3. Calibration automatique
- Optimisation des paramètres moteur
- Adaptation aux conditions (altitude, température)
- Amélioration continue des performances

---

### Comparaison des trois approches

| Critère              | **Supervisé**                      | **Non supervisé**               | **Renforcement**                  |
|----------------------|------------------------------------|---------------------------------|-----------------------------------|
| **Données**          | Étiquetées (coûteux)               | Non étiquetées                  | Générées par simulation/réel      |
| **Objectif**         | Prédire                            | Découvrir                       | Décider                           |
| **Feedback**         | Réponse attendue                   | Aucun                           | Récompense différée               |
| **Exemple auto**     | Détection d'obstacles              | Segmentation conducteurs        | Parking automatique               |
| **Difficulté**       | Moyenne                            | Élevée (interprétation)         | Très élevée (convergence)         |

---

## Notions fondamentales

### 1. Modèle

**Définition :**
> Représentation mathématique de la relation entre entrées et sorties

**Analogie :**
- **Modèle** = Recette de cuisine
- **Algorithme** = Méthode pour créer la recette
- **Données** = Ingrédients

**Exemple simple : Régression linéaire**

```
y = a × x + b

où :
- x = kilométrage du véhicule
- y = nombre de pannes prédites
- a, b = paramètres du modèle (appris)
```

---

### 2. Algorithme

**Définition :**
> Méthode pour entraîner le modèle à partir des données

**Processus :**
1. Initialiser les paramètres du modèle
2. Faire des prédictions
3. Calculer l'erreur
4. Ajuster les paramètres pour réduire l'erreur
5. Répéter jusqu'à convergence

**Algorithmes courants en automobile :**

- **Decision Trees** : Simples à interpréter (important pour la certification)
- **Random Forest** : Robustes, bon compromis performance/interprétabilité
- **Neural Networks** : Très performants mais "boîte noire"
- **XGBoost** : État de l'art pour données tabulaires

---

### 3. Données d'entraînement

**La ressource la plus critique**

#### Qualité > Quantité

**Problèmes courants :**

❌ **Données déséquilibrées**
- 99% de cas normaux, 1% de pannes
- Le modèle apprend juste à dire "pas de panne"

❌ **Biais dans les données**
- Entraîné uniquement sur véhicules neufs
- Mauvaises performances sur véhicules anciens

❌ **Données manquantes**
- Capteur défaillant = données incomplètes
- Impacte la qualité du modèle

❌ **Données bruitées**
- Erreurs de mesure
- Étiquettes incorrectes

---

### Stratégies d'amélioration

✅ **Augmentation des données**
- Créer des variations artificielles
- Ex image : rotation, zoom, changement luminosité

✅ **Équilibrage des classes**
- Sur-échantillonner la classe minoritaire
- Sous-échantillonner la classe majoritaire
- Techniques SMOTE ([Synthetic Minority Oversampling Technique](https://www.analyticsvidhya.com/blog/2020/10/overcoming-class-imbalance-using-smote-techniques/))

✅ **Feature engineering**
- Créer de nouvelles variables pertinentes
- Ex : "ratio température/charge" plutôt que les deux séparément

✅ **Nettoyage rigoureux**
- Détecter et supprimer outliers
- Imputer valeurs manquantes intelligemment

---

### 4. Train / Validation / Test Split

**Erreur fréquente : entraîner et tester sur les mêmes données**

**Bonne pratique :**

```
Données totales (100%)
    │
    ├── 70% : Entraînement (apprentissage des patterns)
    ├── 15% : Validation (ajustement des hyper-paramètres)
    └── 15% : Test (évaluation finale, données jamais vues)
```

**Principe fondamental :**
> Le modèle ne doit JAMAIS voir les données de test pendant l'entraînement

**Pourquoi ?** Évaluer la capacité de généralisation

---

### 5. Surapprentissage (Overfitting)

**Le problème le plus courant en ML**

**Symptômes :**
- Excellentes performances sur données d'entraînement (99%)
- Mauvaises performances sur nouvelles données (60%)

**Métaphore :**
Un étudiant qui apprend par cœur les exercices corrigés mais ne comprend pas les concepts → Échec à l'examen

---

### Détection et solutions

**Détection :**
```
Précision entraînement : 98%
Précision validation : 72%
→ Overfitting détecté !
```

**Solutions :**

1. **Plus de données** (solution #1)
2. **Régularisation** : Pénaliser la complexité
3. **Early stopping** : Arrêter avant de trop spécialiser
4. **Simplifier le modèle** : Moins de paramètres
5. **Dropout** (réseaux neurones) : Désactiver aléatoirement des neurones

---

### 6. Sous-apprentissage (Underfitting)

**Le modèle est trop simple**

**Symptômes :**
- Mauvaises performances partout (train et test)

**Exemple :**
Essayer de prédire des pannes complexes avec juste une régression linéaire simple

**Solutions :**
- Modèle plus complexe
- Ajouter des features
- Entraîner plus longtemps

---

## Exercice : Lecture critique d'un projet IA automobile

### Cas d'étude : Système de prédiction de défaillance calculateur

---

### Description du projet

**Contexte :**
Stellantis souhaite prédire les défaillances de calculateurs moteur avant qu'elles ne surviennent.

**Objectif :**
Réduire les rappels constructeur coûteux en anticipant les pannes.

**Données disponibles :**
- Logs de 50 000 véhicules sur 3 ans
- Données de télémétrie (température, charge CPU, erreurs CAN)
- Historique de maintenance
- Conditions d'utilisation

**Approche proposée :**
- Algorithme : Random Forest
- Apprentissage supervisé (label : panne oui/non dans les 6 mois)
- Déploiement : Prédiction mensuelle via cloud

---

### Travail en groupe (45 min)

**Formez 4 groupes de 2 personnes**

Chaque groupe analyse un aspect différent :

#### Groupe 1 : Données
- La quantité de données est-elle suffisante ?
- Quels problèmes potentiels (biais, déséquilibre, qualité) ?
- Quelles données supplémentaires seraient utiles ?

#### Groupe 2 : Algorithme et modèle
- Random Forest est-il adapté à ce problème ?
- Quels sont ses avantages/inconvénients ?
- Quelles alternatives considérer ?

#### Groupe 3 : Évaluation
- Comment mesurer le succès du projet ?
- Quelles métriques utiliser ?
- Quel niveau de performance est acceptable ?

#### Groupe 4 : Déploiement et risques
- Quels risques techniques ?
- Quels risques métier ?
- Comment assurer la maintenance du système ?

---

### Grille d'analyse

#### Questions à se poser

**Valeur métier :**
- Quel est le ROI attendu ?
- Combien coûte actuellement le problème ?
- Quelle amélioration est réaliste ?

**Faisabilité technique :**
- Les données sont-elles accessibles ?
- L'infrastructure existe-t-elle ?
- Avons-nous les compétences ?

**Risques :**
- Que se passe-t-il si le modèle se trompe ?
- Problèmes de RGPD / confidentialité ?
- Dépendance à un fournisseur ?

**Maintenabilité :**
- Comment mettre à jour le modèle ?
- Comment monitorer ses performances ?
- Qui sera responsable ?

---

### Restitution et discussion (30 min)

**Chaque groupe présente (5 min) :**
- Principaux constats
- Recommandations
- Points de vigilance

**Discussion collective :**
- Feriez-vous ce projet ?
- Quelles modifications suggérez-vous ?
- Quelles étapes prioritaires ?

---

### Correction : Points clés à identifier

#### ✅ Points forts
- Problème réel et coûteux (ROI clair)
- Données disponibles en quantité
- Random Forest = bon choix (interprétable, robuste)
- Approche supervisée adaptée

#### ⚠️ Points d'attention

**Données :**
- Déséquilibre probable (peu de pannes vs beaucoup de OK)
- Biais de survie (véhicules déjà en panne exclus ?)
- Qualité des labels (comment définir "défaillance" ?)

**Modèle :**
- Random Forest peut être lourd pour du temps réel
- Risque d'overfitting si trop de features
- Nécessite feature engineering soigneux

**Évaluation :**
- Privilégier le Rappel (détecter toutes les pannes)
- Coût d'un faux négatif >> coût d'un faux positif
- Validation sur données temporelles (pas aléatoire !)

**Déploiement :**
- Prédiction cloud = dépendance connectivité
- Latence acceptable pour prédiction mensuelle
- Plan de rollback si le modèle dérive
- Explicabilité pour les techniciens

---

### Recommandations

**Avant de lancer :**

1. **Proof of Concept (POC) :**
   - 2-3 mois avec données historiques
   - Valider faisabilité et performance
   - Budget limité

2. **Métriques de succès claires :**
   - Ex : "Détecter 80% des pannes avec max 20% de faux positifs"
   - Comparaison avec baseline (méthode actuelle)

3. **Stratégie de données :**
   - Audit qualité des données
   - Plan d'enrichissement si nécessaire

4. **Équipe dédiée :**
   - Data scientist + Ingénieur calcul + Expert métier
   - Formation continue

5. **Itération :**
   - Commencer simple (régression logistique)
   - Complexifier si nécessaire
   - Mesurer l'amélioration à chaque étape

---

## Application à votre contexte : Code embarqué

### Cas d'usage IA pour le développement de calculateurs

#### 1. Analyse automatique des logs de compilation

**Problème :**
- Milliers de lignes de logs par build
- Erreurs critiques noyées dans les warnings
- Temps perdu à analyser manuellement

**Solution IA :**
- Classification automatique des messages
- Priorisation des erreurs
- Détection de patterns anormaux

**Type d'apprentissage :** Supervisé (classification)

---

#### 2. Prédiction du temps de compilation

**Problème :**
- Builds très longs (30+ minutes)
- Difficile de planifier la journée

**Solution IA :**
- Prédire la durée en fonction des modifications
- Alerter si build anormalement long
- Optimiser l'ordonnancement

**Type d'apprentissage :** Supervisé (régression)

---

#### 3. Génération de tests automatiques

**Problème :**
- Couverture de code insuffisante
- Écrire des tests est chronophage

**Solution IA :**
- LLM (GPT-4, Copilot) pour générer tests unitaires
- Analyse du code pour identifier cas limites
- Suggestion de scénarios de test

**Type d'approche :** IA générative + Analyse statique

---

#### 4. Détection de code similaire (refactoring)

**Problème :**
- Duplication de code
- Maintenance difficile

**Solution IA :**
- Clustering de fonctions similaires
- Suggestion de factorisation

**Type d'apprentissage :** Non supervisé (clustering)

---

#### 5. Optimisation de paramètres

**Problème :**
- Nombreux paramètres de calibration moteur
- Optimiser manuellement = semaines

**Solution IA :**
- Apprentissage par renforcement
- Simulation pour explorer l'espace des paramètres
- Convergence vers optimal

**Type d'apprentissage :** Renforcement

---

## Points clés à retenir

### Types d'apprentissage

| Type | Quand l'utiliser | Exemple automobile |
|------|------------------|-------------------|
| **Supervisé** | Vous avez des exemples étiquetés | Détection pannes |
| **Non supervisé** | Vous voulez explorer les données | Segmentation conducteurs |
| **Renforcement** | Vous voulez optimiser une séquence d'actions | Parking autonome |

---

### Concepts fondamentaux

1. **Modèle** = Représentation mathématique apprise
2. **Données** = La ressource critique (qualité > quantité)
3. **Train/Val/Test** = Toujours évaluer sur données non vues
4. **Overfitting** = Ennemi n°1 (apprendre par cœur vs comprendre)
5. **Métriques** = Choisir selon le coût des erreurs

---

### Checklist pour évaluer un projet IA

- [ ] Problème clairement défini ?
- [ ] Données disponibles en quantité et qualité ?
- [ ] Type d'apprentissage adapté ?
- [ ] Métriques de succès définies ?
- [ ] Risques identifiés et plan de mitigation ?
- [ ] Équipe compétente et disponible ?
- [ ] ROI clair ?
- [ ] Plan de déploiement et maintenance ?

---

## Ressources pour aller plus loin

### Livres recommandés (niveau débutant)
- "The Hundred-Page Machine Learning Book" - Andriy Burkov
- "Machine Learning for Absolute Beginners" - Oliver Theobald

### Cours en ligne
- Coursera : "Machine Learning" par Andrew Ng (référence)
- Fast.ai : "Practical Deep Learning for Coders"

### Outils à explorer
- **Scikit-learn** : Bibliothèque Python ML
- **TensorFlow/PyTorch** : Deep Learning
- **Hugging Face** : LLMs et IA générative

### Communautés
- Kaggle : Compétitions et datasets
- Papers With Code : Dernières recherches

---

## Pause déjeuner - 1h00

**Cet après-midi :**
- Les fondamentaux du Big Data
- Cas pratique avec données de capteurs Volvo

---

## Annexes : Aller plus loin

### A. Méthodes d'ensemble (Ensemble Learning)

**Principe :** Combiner plusieurs modèles pour améliorer la performance

#### Bagging (Bootstrap Aggregating)
- Entraîner plusieurs modèles sur des sous-ensembles aléatoires
- **Random Forest** = Bagging d'arbres de décision
- Réduit l'overfitting

#### Boosting
- Entraîner séquentiellement des modèles
- Chaque nouveau modèle corrige les erreurs du précédent
- **XGBoost**, **LightGBM**, **CatBoost**
- État de l'art sur données tabulaires

---

### B. Feature Engineering

**Art de créer de bonnes variables**

**Exemple automobile :**

Données brutes :
- Kilométrage : 150 000 km
- Âge véhicule : 8 ans

Features engineerées :
- Kilométrage annuel moyen : 18 750 km/an
- Ratio km/âge : Indicateur d'usage intensif

**Techniques :**
- Combinaisons de variables
- Transformations logarithmiques
- Encoding de variables catégorielles
- Interaction features

**Impact :** Peut améliorer la performance de 10-30% !

---

### C. Transfer Learning

**Réutiliser un modèle pré-entraîné**

**Exemple :**
- Modèle pré-entraîné sur ImageNet (1M images)
- Fine-tuner sur vos 10 000 images de pièces automobiles
- Gain de temps et de performance

**Pertinent pour :**
- Vision (détection objets, classification images)
- NLP (analyse de logs textuels)
- Audio (reconnaissance voix conducteur)

---

### D. AutoML

**Automatisation du Machine Learning**

**Outils :**
- **H2O.ai** : AutoML open source
- **Google AutoML** : Solution cloud
- **Auto-sklearn** : Basé sur scikit-learn

**Ce qu'ils automatisent :**
- Choix de l'algorithme
- Hyper-paramètres
- Feature engineering
- Ensemble learning

**Limite :** Moins flexible qu'une approche manuelle

**Usage recommandé :** Baseline rapide, puis affiner manuellement
