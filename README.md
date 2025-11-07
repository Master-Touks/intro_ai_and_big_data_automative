# Formation : Les fondamentaux de l'intelligence artificielle et du big data

## 📋 Informations générales

**Durée :** 2 jours (14 heures)
**Public :** Ingénieurs produits - Développement calculateurs automobiles
**Contexte :** Stellantis / Renault - Conception logicielle de calculateurs moteur
**Niveau :** Débutant (aucun prérequis)

---

## 🎯 Objectifs de la formation

À l'issue de cette formation, vous serez capable de :
- ✅ Comprendre les fondamentaux de l'IA et de la data
- ✅ Découvrir et expérimenter des cas d'usage concrets adaptés à l'automobile
- ✅ Analyser les projets d'IA pour en évaluer le potentiel et les risques
- ✅ Identifier des pistes d'action réalistes pour votre périmètre d'activité

---

## 📁 Structure du projet

```
big_data_course/
│
├── slides/                          # Support de cours (Markdown)
│   ├── 01_introduction_ia_bigdata_automobile.md
│   ├── 02_fondamentaux_ia.md
│   ├── 03_fondamentaux_bigdata.md
│   ├── 04_cas_usage_automobile.md
│   ├── 05_evaluer_projet_ia.md
│   └── 06_pistes_action_conclusion.md
│
├── notebooks/                       # Exercices pratiques (Jupyter)
│   ├── 01_visualisation_capteurs_riib.ipynb
│   ├── 02_maintenance_predictive.ipynb
│   └── 03_analyse_comportementale_conducteurs.ipynb
│
├── data_source/                     # Données pour exercices
│   └── telemetry_simulated.csv
│
├── riib/                            # Dataset RIIB (images capteurs)
│   └── additional/
│
├── notes.md                         # Notes contextuelles
├── CLAUDE.md                        # Instructions de création
└── README.md                        # Ce fichier
```

---

## 📅 Programme détaillé

### **Jour 1 – Comprendre les bases et les enjeux**

#### 🌅 Matin (7h)

**1. Introduction à l'IA et au Big Data dans l'automobile** (2h00)
- Définitions clés : IA, Machine Learning, Deep Learning, Big Data
- Panorama des technologies émergentes (ADAS, véhicules connectés, maintenance prédictive)
- Tendances du marché et innovations récentes
- Quiz interactif et exercice de lecture critique

**2. Les fondamentaux de l'IA** (2h30)
- Types d'apprentissage : supervisé, non supervisé, par renforcement
- Notions de modèles, algorithmes, données d'entraînement
- Overfitting, underfitting, train/test split
- Exercice pratique : Analyse d'un projet IA automobile

**Pause déjeuner** (1h00)

#### 🌆 Après-midi (5h30)

**3. Les fondamentaux du Big Data** (2h00)
- Les 5V du Big Data (Volume, Vélocité, Variété, Véracité, Valeur)
- Architecture type d'un système Big Data
- Technologies de l'écosystème (Spark, Kafka, Hadoop)

**4. Cas pratique : Visualisation de données capteurs embarqués** (1h15)
- 📓 **Notebook 01** : `01_visualisation_capteurs_riib.ipynb`
- Exploration du dataset RIIB (images de caméras)
- Analyse de données de télémétrie simulées
- Détection d'anomalies

**Pause** (15 min)

**5. Discussion et synthèse du Jour 1** (30 min)

---

### **Jour 2 – Appliquer, évaluer, projeter**

#### 🌅 Matin (7h)

**1. Cas d'usage concrets dans l'automobile** (2h30)
- IA pour la maintenance prédictive
- Analyse comportementale des conducteurs
- Optimisation logistique et chaîne d'approvisionnement
- Étude de cas : IA embarquée dans véhicules connectés

**Pause** (15 min)

**2. Cas pratique : Maintenance prédictive** (1h00)
- 📓 **Notebook 02** : `02_maintenance_predictive.ipynb`
- Construction d'un modèle Random Forest pour prédire des pannes
- Évaluation avec métriques appropriées (précision, rappel, ROC-AUC)
- Calcul du ROI

**Pause déjeuner** (1h00)

#### 🌆 Après-midi (5h30)

**3. Évaluer un projet IA** (2h00)
- Méthodologie : valeur métier, faisabilité technique, risques
- Biais algorithmiques et explicabilité (SHAP, LIME)
- RGPD et protection des données
- Atelier pratique : Analyse critique d'un projet IA (en groupe)

**Pause** (15 min)

**4. Cas pratique : Analyse comportementale** (45 min)
- 📓 **Notebook 03** : `03_analyse_comportementale_conducteurs.ipynb`
- Clustering K-Means pour segmenter les conducteurs
- Interprétation des profils (Prudent, Routier, Sportif, Mixte)
- Applications business

**5. Identifier des pistes d'action** (1h30)
- Cartographie des opportunités IA dans votre périmètre
- Identification des données disponibles et manquantes
- Exercice d'idéation : Imaginer un projet IA réaliste
- Construction de votre roadmap personnelle

**6. Conclusion et perspectives** (30 min)
- Synthèse des apprentissages
- Discussion sur les tendances futures (IA générative, edge computing, etc.)
- Plan d'action individuel : que puis-je initier dès demain ?

---

## 🛠️ Installation et prérequis

### Environnement technique

**Requis :**
- Python 3.8+
- Jupyter Notebook ou JupyterLab
- Bibliothèques : voir `requirements.txt` (à créer si nécessaire)

**Installation :**

```bash
# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate

# Installer les dépendances
pip install numpy pandas matplotlib seaborn scikit-learn pillow

# Lancer Jupyter
jupyter notebook
```

### Données

- **Dataset RIIB** : Déjà inclus dans le dossier `riib/`
- **Données de télémétrie** : Générées automatiquement dans les notebooks

---

## 📓 Notebooks pratiques

### Notebook 01 : Visualisation de données capteurs
**Fichier :** `notebooks/01_visualisation_capteurs_riib.ipynb`

**Objectifs :**
- Charger et explorer des images de caméras embarquées (RIIB)
- Analyser des données de télémétrie simulées (3M d'enregistrements)
- Visualiser avec matplotlib et seaborn
- Détecter des anomalies (températures élevées)

**Concepts abordés :**
- Les 5V du Big Data en pratique
- Manipulation de données avec pandas
- Visualisation de séries temporelles
- Détection d'anomalies par seuillage

**Durée estimée :** 45-60 min

---

### Notebook 02 : Maintenance prédictive
**Fichier :** `notebooks/02_maintenance_predictive.ipynb`

**Objectifs :**
- Construire un modèle ML pour prédire des pannes de batterie
- Comprendre le processus end-to-end d'un projet ML
- Évaluer avec des métriques adaptées (précision, rappel, ROC-AUC)
- Calculer le ROI d'un projet IA

**Concepts abordés :**
- Apprentissage supervisé (classification)
- Random Forest Classifier
- Matrice de confusion
- Feature importance
- Ajustement du seuil décisionnel
- Trade-off business (coût intervention vs coût panne)

**Durée estimée :** 60-75 min

---

### Notebook 03 : Analyse comportementale des conducteurs
**Fichier :** `notebooks/03_analyse_comportementale_conducteurs.ipynb`

**Objectifs :**
- Segmenter les conducteurs en profils distincts
- Comprendre l'apprentissage non supervisé (clustering)
- Appliquer K-Means et la méthode du coude
- Tirer des insights business actionnables

**Concepts abordés :**
- Apprentissage non supervisé
- K-Means Clustering
- Méthode du coude (Elbow Method)
- PCA pour visualisation 2D
- Normalisation des données
- Interprétation et profilage des clusters

**Durée estimée :** 45-60 min

---

## 💡 Concepts clés abordés

### Intelligence Artificielle
- Machine Learning vs Deep Learning
- Apprentissage supervisé, non supervisé, par renforcement
- Algorithmes : Régression, Classification, Clustering
- Évaluation de modèles (précision, rappel, F1-score, AUC)
- Overfitting / Underfitting
- Feature engineering

### Big Data
- Les 5V : Volume, Vélocité, Variété, Véracité, Valeur
- Architecture : Ingestion → Stockage → Traitement → Visualisation
- Technologies : Spark, Kafka, Hadoop, HDFS
- Data Lake vs Data Warehouse
- Traitement batch vs streaming

### Cas d'usage automobile
- Maintenance prédictive
- Analyse comportementale conducteurs
- ADAS et IA embarquée (Edge AI)
- Optimisation logistique
- Mises à jour OTA (Over-The-Air)

### Éthique et gouvernance
- Biais algorithmiques (détection et mitigation)
- Explicabilité (SHAP, LIME)
- RGPD et protection des données
- Équité et non-discrimination

---

## 🎓 Ressources complémentaires

### Cours en ligne recommandés

**Débutant :**
- [Coursera : Machine Learning par Andrew Ng](https://www.coursera.org/learn/machine-learning) (Référence absolue)
- [Fast.ai : Practical Deep Learning for Coders](https://course.fast.ai/)
- [Google : Machine Learning Crash Course](https://developers.google.com/machine-learning/crash-course)

**Intermédiaire :**
- [Coursera : Deep Learning Specialization](https://www.coursera.org/specializations/deep-learning)
- [Udacity : AI for Automotive](https://www.udacity.com/)

### Livres recommandés

**Non-techniques :**
- "Prediction Machines" - Agrawal, Gans, Goldfarb
- "AI Superpowers" - Kai-Fu Lee

**Techniques :**
- "Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow" - Aurélien Géron
- "The Hundred-Page Machine Learning Book" - Andriy Burkov

**Spécialisés :**
- "Designing Data-Intensive Applications" - Martin Kleppmann (Big Data)
- "Interpretable Machine Learning" - Christoph Molnar (Gratuit en ligne)

### Outils à explorer

**Langages :**
- Python (incontournable)
- SQL (manipulation de données)

**Bibliothèques ML :**
- Scikit-learn (ML classique)
- TensorFlow / PyTorch (Deep Learning)
- XGBoost / LightGBM (Gradient Boosting)

**Big Data :**
- PySpark (Python + Spark)
- Dask (Pandas à l'échelle)

**Visualisation :**
- Matplotlib / Seaborn
- Plotly (interactif)
- Tableau / Power BI (Business Intelligence)

### Communautés

- [Kaggle](https://www.kaggle.com/) : Compétitions ML, datasets
- [GitHub](https://github.com/) : Projets open-source
- [Hugging Face](https://huggingface.co/) : LLMs, datasets, modèles

---

## 🚀 Projets suggérés pour votre contexte

### Quick Wins (3-6 mois)

**1. Analyse intelligente des logs de compilation**
- **Impact :** Gain de 6000h/an = 240 k€
- **Faisabilité :** Moyenne
- **Données :** Disponibles
- **ROI :** 300%

### Stars (6-12 mois)

**2. Détection d'anomalies en temps réel (bancs d'essai)**
- **Impact :** Sécurité ++
- **Faisabilité :** Moyenne
- **Données :** Partiellement disponibles
- **Urgence :** Critique

**3. Génération automatique de tests unitaires (LLM)**
- **Impact :** Qualité logicielle +30%
- **Faisabilité :** Difficile
- **Données :** Code source disponible
- **ROI :** 500%

### R&D Long Terme (12-24 mois)

**4. Optimisation automatique des paramètres de calibration (RL)**
- **Impact :** Très élevé (compétitivité produit)
- **Faisabilité :** Très difficile
- **Données :** À créer (simulation)
- **Risque :** Élevé

---

## 📞 Contact et support

**Formateur :** BADE Tuka - Data Scientist
**Email :** [bade.tuka@gmail.com](mailto:bade.tuka@gmail.com)
**LinkedIn :** [linkedin/in/tukanebaribade](https://www.linkedin.com/in/tukanebaribade)

**Ressources :**
- Slides : `slides/`
- Notebooks : `notebooks/`
- GitHub : [lien à ajouter]

---

## 📝 Notes importantes

### Avant la formation

- [ ] Installer Python 3.8+ et Jupyter
- [ ] Vérifier que les notebooks se lancent correctement
- [ ] Télécharger les datasets (RIIB déjà inclus)
- [ ] Préparer des exemples de projets de votre contexte

### Pendant la formation

- [ ] Prendre des notes dans les notebooks
- [ ] Poser des questions dès que nécessaire
- [ ] Participer aux exercices de groupe
- [ ] Réfléchir aux applications pour votre périmètre

### Après la formation

- [ ] Revoir les notebooks à votre rythme
- [ ] Identifier 1 projet concret à proposer
- [ ] Suivre un cours en ligne (Andrew Ng recommandé)
- [ ] Partager les learnings avec votre équipe

---

## 📄 Licence et utilisation

Cette formation a été créée spécifiquement pour les ingénieurs de Stellantis/Renault travaillant sur le développement de calculateurs automobiles.

**Contenu :**
- Slides (Markdown) : Libre d'utilisation en interne
- Notebooks (Jupyter) : Libre d'utilisation en interne
- Datasets : RIIB sous licence non-commerciale, données simulées libres

**Restrictions :**
- Usage interne uniquement
- Pas de redistribution externe sans autorisation

---

## 🎉 Bonne formation !

N'hésitez pas à expérimenter, poser des questions, et surtout : **prenez du plaisir à découvrir l'IA et le Big Data !**

L'avenir de l'automobile se construit aujourd'hui, et vous en êtes les acteurs.

---

**Dernière mise à jour :** Novembre 2024
**Version :** 1.0
