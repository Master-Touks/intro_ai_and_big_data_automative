# 📚 INDEX - Formation IA et Big Data pour l'Automobile

## Vue d'ensemble

Cette formation complète de **14 heures (2 jours)** comprend :
- ✅ **6 modules de slides** (Markdown)
- ✅ **4 notebooks pratiques** (Jupyter)
- ✅ **Documentation complète** (README, Guide)
- ✅ **Datasets inclus** (RIIB + données simulées + LIDARS Volvo)

---

## 📖 JOUR 1 : Comprendre les bases et les enjeux

### Matin (7h)

#### 📄 Module 1 : Introduction à l'IA et Big Data (2h00)
**Fichier :** `slides/01_introduction_ia_bigdata_automobile.md`

**Contenu :**
- Définitions : IA, ML, DL, Big Data
- Panorama technologies automobile (ADAS, véhicules connectés)
- Tendances marché et innovations
- Quiz et exercice pratique

**Concepts clés :**
- Intelligence Artificielle vs Machine Learning vs Deep Learning
- ADAS, maintenance prédictive, véhicules connectés
- Edge AI, IA générative, Digital Twin

---

#### 📄 Module 2 : Les fondamentaux de l'IA (2h30)
**Fichier :** `slides/02_fondamentaux_ia.md`

**Contenu :**
- Types d'apprentissage (supervisé, non supervisé, renforcement)
- Modèles, algorithmes, données d'entraînement
- Overfitting, train/test split
- Feature engineering
- Exercice : Analyse projet IA calculateur

**Concepts clés :**
- Classification vs Régression
- Random Forest, XGBoost, Neural Networks
- Précision, Rappel, F1-Score, AUC
- Biais et variance

---

### Après-midi (5h30)

#### 📄 Module 3 : Les fondamentaux du Big Data (2h00)
**Fichier :** `slides/03_fondamentaux_bigdata.md`

**Contenu :**
- Les 5V du Big Data (Volume, Vélocité, Variété, Véracité, Valeur)
- Architecture Big Data (Ingestion, Stockage, Traitement, Visualisation)
- Technologies : Spark, Kafka, Hadoop, HDFS
- Data Lake vs Data Warehouse

**Concepts clés :**
- Batch vs Streaming vs Real-time
- Apache Spark, PySpark
- ETL (Extract, Transform, Load)
- Scalabilité horizontale

---

#### 💻 Notebook 1 : Visualisation données capteurs (1h15)
**Fichier :** `notebooks/01_visualisation_capteurs_riib.ipynb`

**Objectifs :**
- Charger et visualiser images de caméras embarquées (RIIB)
- Analyser données de télémétrie (3M enregistrements)
- Détecter anomalies (températures élevées)
- Visualiser avec matplotlib/seaborn

**Compétences développées :**
- Manipulation données avec pandas
- Visualisation séries temporelles
- Statistiques descriptives
- Détection d'anomalies par seuillage

**Données utilisées :**
- Dataset RIIB (images PGM)
- Télémétrie simulée (1000 véhicules × 30 jours)

---

## 📖 JOUR 2 : Appliquer, évaluer, projeter

### Matin (7h)

#### 📄 Module 4 : Cas d'usage concrets automobile (2h30)
**Fichier :** `slides/04_cas_usage_automobile.md`

**Contenu :**
1. **Maintenance prédictive**
   - Fonctionnement, ROI (370%)
   - Données nécessaires
   - Challenges (déséquilibre classes, drift)

2. **Analyse comportementale conducteurs**
   - Segmentation (Prudent, Routier, Sportif, Mixte)
   - Applications : Assurance, Marketing, Produit
   - RGPD et éthique

3. **Optimisation logistique**
   - Prévision demande
   - Optimisation stocks (Reinforcement Learning)
   - Vehicle Routing Problem

4. **IA embarquée (Edge AI)**
   - Détection somnolence
   - Mises à jour OTA
   - Assistant vocal (LLM)

**Concepts clés :**
- Edge vs Cloud computing
- Pay How You Drive (assurance)
- Over-The-Air updates
- Explicabilité (SHAP, LIME)

---

#### 💻 Notebook 2 : Maintenance prédictive (1h00)
**Fichier :** `notebooks/02_maintenance_predictive.ipynb`

**Objectifs :**
- Construire modèle ML pour prédire pannes de batterie
- Comprendre process ML end-to-end
- Évaluer avec métriques appropriées
- Calculer ROI

**Compétences développées :**
- Apprentissage supervisé (classification)
- Random Forest Classifier
- Matrice de confusion
- Feature importance
- Ajustement seuil décisionnel
- Calcul ROI (économies vs coûts)

**Pipeline complet :**
1. Génération données (5000 véhicules)
2. EDA (Exploratory Data Analysis)
3. Préparation (normalisation, train/test split)
4. Entraînement Random Forest
5. Évaluation (Précision, Rappel, AUC)
6. Identification véhicules à risque
7. Simulation intervention (calcul économies)

**Résultats attendus :**
- AUC > 0.85 (Très bon modèle)
- ROI : 450% (année 2+)
- Économies : 190 k€/an (flotte 5000 véhicules)

---

### Après-midi (5h30)

#### 📄 Module 5 : Évaluer un projet IA (2h00)
**Fichier :** `slides/05_evaluer_projet_ia.md`

**Contenu :**
1. **Méthodologie d'analyse**
   - Valeur métier (ROI, alternatives)
   - Faisabilité technique (données, algorithmes, infra)
   - Risques (biais, RGPD, maintenance)

2. **Biais algorithmiques**
   - Types de biais (sélection, mesure, historique)
   - Détection (fairness metrics)
   - Mitigation

3. **Explicabilité**
   - Feature importance
   - SHAP values
   - LIME

4. **RGPD**
   - 6 principes (licéité, minimisation, etc.)
   - Droits des personnes
   - Sanctions (4% CA ou 20 M€)

5. **Atelier pratique**
   - Analyse critique projet IA (en groupe)
   - Cas : Prédiction valeur résiduelle véhicule

**Concepts clés :**
- Trade-off performance vs interprétabilité
- Demographic parity, Equal opportunity
- DPIA (Data Protection Impact Assessment)
- Concept drift, model monitoring

---

#### 💻 Notebook 3 : Analyse comportementale (45 min)
**Fichier :** `notebooks/03_analyse_comportementale_conducteurs.ipynb`

**Objectifs :**
- Segmenter conducteurs en profils distincts
- Comprendre apprentissage non supervisé
- Appliquer K-Means et méthode du coude
- Tirer insights business

**Compétences développées :**
- Apprentissage non supervisé (clustering)
- K-Means
- Méthode du coude (Elbow Method)
- PCA pour visualisation 2D
- Normalisation des données
- Interprétation clusters

**Pipeline complet :**
1. Génération données (2000 conducteurs, 4 profils cachés)
2. EDA et corrélations
3. Normalisation (StandardScaler)
4. Méthode du coude → K=4
5. Application K-Means
6. Profilage clusters (heatmap, radar charts)
7. Validation vs vrais profils
8. Visualisation 2D avec PCA
9. Applications business (campagnes ciblées)

**Profils identifiés :**
- **Prudent** (30%) : Vitesse faible, peu de km, ADAS++
- **Routier** (25%) : Haute km, autoroute, régulateur++
- **Sportif** (15%) : Accélérations/freinages brusques
- **Mixte** (30%) : Comportement intermédiaire

---

#### 📄 Module 6 : Pistes d'action et conclusion (1h30)
**Fichier :** `slides/06_pistes_action_conclusion.md`

**Contenu :**
1. **Cartographie opportunités IA**
   - Matrice Impact vs Faisabilité
   - Quick Wins, Stars, Long-term
   - 5 opportunités pour calculateurs

2. **Identification données**
   - Disponibles vs Manquantes
   - Coût d'acquisition
   - Gaps à combler

3. **Exercice d'idéation**
   - Template de projet IA
   - Pitch individuel
   - Feedback groupe

4. **Tendances futures**
   - IA générative (LLMs, Copilot)
   - Edge Computing et IA embarquée
   - Federated Learning
   - Digital Twins
   - Quantum ML

5. **Plan d'action individuel**
   - Cette semaine
   - Ce mois
   - Ce trimestre

**Projets suggérés :**
- **Quick Win** : Analyse logs compilation (ROI 300%)
- **Star** : Détection anomalies temps réel
- **Star** : Génération tests unitaires (ROI 500%)
- **R&D** : Optimisation paramètres calibration (RL)

---

## 📚 Documentation complémentaire

### 📄 README.md
**Fichier principal** décrivant :
- Objectifs de la formation
- Structure du projet
- Programme détaillé
- Installation et prérequis
- Ressources complémentaires (cours, livres, outils)

### 📄 GUIDE_UTILISATION.md
**Guide pratique** couvrant :
- Comment visualiser les slides (Markdown)
- Comment utiliser les notebooks (Jupyter)
- Organisation d'une session de formation
- Conseils pédagogiques
- Résolution de problèmes courants
- Checklist de préparation
- Évaluation et feedback

### 📄 notes.md
Contexte de la formation :
- Activité : Calculateurs moteur Stellantis/Renault
- 8 participants ingénieurs produits
- Liens vers datasets (GCP bucket)

### 📄 CLAUDE.md
Instructions originales du projet

---

## 📊 Statistiques de la formation

| Métrique | Valeur |
|----------|--------|
| **Durée totale** | 14 heures (2 jours) |
| **Modules théoriques** | 6 (slides Markdown) |
| **Exercices pratiques** | 3 (notebooks Jupyter) |
| **Lignes de code** | ~2000 (notebooks) |
| **Slides** | ~500 (total) |
| **Concepts abordés** | 50+ |
| **Algorithmes** | 10+ (Random Forest, K-Means, etc.) |
| **Datasets** | 3 (RIIB + 2 simulés) |

---

## 🗂️ Arborescence complète

```
big_data_course/
│
├── 📄 README.md                     # Documentation principale
├── 📄 GUIDE_UTILISATION.md          # Guide pratique
├── 📄 INDEX.md                      # Ce fichier
├── 📄 notes.md                      # Contexte entreprise
├── 📄 CLAUDE.md                     # Instructions originales
│
├── 📁 slides/                       # Supports de cours
│   ├── 01_introduction_ia_bigdata_automobile.md
│   ├── 02_fondamentaux_ia.md
│   ├── 03_fondamentaux_bigdata.md
│   ├── 04_cas_usage_automobile.md
│   ├── 05_evaluer_projet_ia.md
│   └── 06_pistes_action_conclusion.md
│
├── 📁 notebooks/                    # Exercices pratiques
│   ├── 01_visualisation_capteurs_riib.ipynb
│   ├── 02_maintenance_predictive.ipynb
│   └── 03_analyse_comportementale_conducteurs.ipynb
│
├── 📁 riib/                         # Dataset images capteurs
│   └── additional/
│       └── [13 dossiers de sessions]
│           └── [~200 fichiers .pgm]
│
├── 📁 data_source/                  # Données générées
│   └── telemetry_simulated.csv
│
└── 📁 venv/                         # Environnement virtuel Python
```

---

## 🎯 Parcours d'apprentissage recommandé

### Pour participants débutants

**Avant la formation :**
1. Lire `README.md`
2. Installer Python + Jupyter
3. Regarder vidéo : "What is Machine Learning?" (3Blue1Brown)

**Pendant la formation :**
1. Suivre ordre chronologique (Jour 1 → Jour 2)
2. Exécuter tous les notebooks
3. Poser des questions dès que nécessaire
4. Prendre des notes

**Après la formation :**
1. Revoir notebooks à tête reposée
2. Commencer cours "Machine Learning" par Andrew Ng (Coursera)
3. Identifier 1 projet concret dans votre périmètre
4. Partager learnings avec équipe

### Pour participants intermédiaires

**Avant la formation :**
1. Parcourir rapidement Module 2 (déjà connu)
2. Focus sur contexte automobile (Module 1)

**Pendant la formation :**
1. Aller vite sur bases
2. Approfondir Module 5 (évaluation projet IA)
3. Proposer cas d'usage avancés

**Après la formation :**
1. Deep dive sur explicabilité (SHAP/LIME)
2. Lire "Designing Data-Intensive Applications"
3. Lancer POC dans votre entreprise

---

## 📖 Glossaire rapide

**IA (Intelligence Artificielle)** : Capacité d'une machine à imiter l'intelligence humaine

**ML (Machine Learning)** : Branche de l'IA permettant aux machines d'apprendre sans être explicitement programmées

**DL (Deep Learning)** : Sous-ensemble du ML utilisant des réseaux de neurones profonds

**Big Data** : Données massives dépassant les capacités des outils traditionnels

**Les 5V** : Volume, Vélocité, Variété, Véracité, Valeur

**Apprentissage supervisé** : Entraînement avec des labels (ex: panne/pas panne)

**Apprentissage non supervisé** : Découverte de patterns sans labels (ex: clustering)

**Overfitting** : Modèle trop spécialisé sur données d'entraînement

**ROI (Return on Investment)** : (Gains - Coûts) / Coûts × 100%

**AUC** : Area Under Curve (métrique pour classifieurs, 0.5-1.0)

**Clustering** : Regroupement automatique de données similaires

**Feature** : Variable utilisée par le modèle ML

**RGPD** : Règlement Général sur la Protection des Données

**Edge AI** : IA exécutée localement dans l'appareil (vs cloud)

**Biais algorithmique** : Erreur systématique conduisant à prédictions injustes

---

## 🚀 Quick Start (5 minutes)

```bash
# 1. Aller dans le dossier
cd /Users/tukanebari/PycharmProjects/big_data_course

# 2. Installer dépendances
pip install numpy pandas matplotlib seaborn scikit-learn pillow

# 3. Décompresser données
python unzipping_data.py

# 4. Lancer Jupyter
jupyter notebook

# 5. Ouvrir notebooks/01_visualisation_capteurs_riib.ipynb

# 6. Exécuter cellule par cellule (Shift + Enter)

# 7. Enjoy! 🎉
```

---

## 📞 Besoin d'aide ?

**Documentation :**
1. Lire `README.md` (vue d'ensemble)
2. Consulter `GUIDE_UTILISATION.md` (problèmes techniques)
3. Chercher dans `INDEX.md` (ce fichier - navigation)

**Support :**
- Email : [bade.tuka@gmail.com](mailto:bade.tuka@gmail.com)
- Issues : [à compléter]

---

## 📝 Checklist avant de commencer

Avant la formation, vérifier que :
- [ ] Python 3.8+ installé (`python --version`)
- [ ] Jupyter installé (`jupyter --version`)
- [ ] Bibliothèques installées (`pip list`)
- [ ] Données RIIB décompressées (`ls riib/additional/`)
- [ ] Au moins 1 notebook s'ouvre sans erreur
- [ ] Accès Internet (ressources en ligne)

---

## 🎓 Certification (optionnelle)

Après la formation, envisager :
- **Google : TensorFlow Developer Certificate** (débutant)
- **Microsoft : Azure AI Fundamentals (AI-900)** (débutant)
- **Databricks : Certified Data Engineer Associate** (intermédiaire)
- **Google : Professional ML Engineer** (avancé)

---

## 🌟 Remerciements

Cette formation a été conçue spécifiquement pour les ingénieurs produits de **Stellantis / Renault** travaillant sur le développement de calculateurs automobiles.

**Objectif :** Démystifier l'IA et le Big Data, et donner les outils pour identifier et lancer des projets concrets.

---

## 📅 Mises à jour

**Version 1.0** (Novembre 2024) : Version initiale
- 6 modules de slides
- 3 notebooks pratiques
- Documentation complète

**Version 1.1** (prévue Q1 2025) :
- Module IA générative (LLMs, ChatGPT, Copilot)
- Cas d'usage "Génération de tests unitaires"
- Dataset réel Stellantis/Renault (si accord)

**Version 2.0** (Formation niveau 2 - prévue Q2 2025) :
- Deep Learning avancé
- Déploiement ML (MLOps)
- Spark avancé (PySpark)
- Projet fil rouge

---

## 🎉 Bonne formation !

Vous avez maintenant toutes les clés en main pour :
- ✅ Comprendre l'IA et le Big Data
- ✅ Identifier des opportunités dans votre entreprise
- ✅ Lancer vos premiers projets
- ✅ Continuer à apprendre

**L'avenir de l'automobile se construit aujourd'hui.**
**Et vous en êtes les acteurs !**

---

**Dernière mise à jour :** Novembre 2024
**Version :** 1.0
