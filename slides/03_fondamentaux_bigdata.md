# Les fondamentaux du Big Data

## Durée : 2h30 (avec cas pratique)

---

## Objectifs de ce module

- Comprendre les 5V du Big Data
- Découvrir l'architecture d'un système Big Data
- Manipuler des données réelles de capteurs automobiles
- Visualiser et analyser des données massives

---

## Qu'est-ce que le Big Data ?

### Définition

> **"Ensemble de données si volumineuses qu'elles dépassent les capacités des outils traditionnels"**

**Outils traditionnels :**
- Excel : Limite ~ 1 million de lignes
- Base de données classique : Ralentit fortement au-delà de quelques millions d'enregistrements
- Traitement séquentiel sur une seule machine

**Big Data :**
- Milliards d'enregistrements
- Traitement distribué sur des clusters de serveurs
- Technologies spécialisées (Hadoop, Spark, etc.)

---

### Exemples automobiles

| Source | Volume par véhicule | Parc de 1 million |
|--------|---------------------|-------------------|
| **Capteurs embarqués** | 4 To/jour | 4 Po/jour |
| **Logs calculateurs** | 100 Mo/jour | 100 To/jour |
| **Données GPS** | 50 Mo/jour | 50 To/jour |
| **Maintenance** | 1 Mo/visite | Variable |

**Po = Pétaoctet = 1 000 To = 1 000 000 Go**

Une seule flotte de véhicules connectés génère plusieurs pétaoctets par jour !

---

## Les 5V du Big Data

```
    Volume
       │
   Vélocité ──── BIG DATA ──── Variété
       │
    Véracité ──── Valeur
```

---

### 1. Volume

**La quantité massive de données**

#### Ordres de grandeur

- **Mégaoctet (Mo)** : Une photo haute résolution
- **Gigaoctet (Go)** : Un film HD
- **Téraoctet (To)** : 1 000 Go - Disque dur standard
- **Pétaoctet (Po)** : 1 000 To - Datacenter moyen
- **Exaoctet (Eo)** : 1 000 Po - Les plus grands datacenters
- **Zettaoctet (Zo)** : 1 000 Eo - Données mondiales générées/an

---

#### Exemple Stellantis/Renault

**Hypothèses :**
- 2 millions de véhicules connectés
- Chaque véhicule génère 1 Go/jour de télémétrie

**Volume :**
- **Par jour** : 2 Po
- **Par an** : 730 Po = 0,73 Eo

**Conséquences :**
- Impossible de stocker sur une seule machine
- Nécessite un système de stockage distribué
- Coûts de stockage significatifs (mais décroissants)

---

#### Solutions pour gérer le Volume

**Stockage distribué :**
- **HDFS (Hadoop Distributed File System)** : Fichiers répartis sur plusieurs serveurs
- **Cloud Storage** : Google Cloud Storage, AWS S3, Azure Blob
- **Data Lakes** : Stockage centralisé de toutes les données brutes

**Compression :**
- Formats efficaces : Parquet, ORC, Avro
- Réduction de 70-90% de la taille
- Exemple : CSV 10 Go → Parquet 1 Go

**Archivage :**
- Données chaudes (accès fréquent) : SSD
- Données tièdes (accès occasionnel) : HDD
- Données froides (rarement accédées) : Cloud glacial

---

### 2. Vélocité

**La vitesse de génération et de traitement des données**

#### Trois types de traitement

| Type | Latence | Exemple automobile |
|------|---------|-------------------|
| **Batch** | Heures/jours | Analyse mensuelle des ventes |
| **Near Real-Time** | Minutes/secondes | Détection d'anomalies de flotte |
| **Real-Time** | Millisecondes | Freinage d'urgence automatique |

---

#### Cas d'usage : ADAS en temps réel

**Contrainte :** Décision en < 100 ms

**Pipeline :**
1. Capteurs (caméras, radars) : Génération données → 50 ms
2. Traitement image (détection obstacle) → 30 ms
3. Décision et action (freiner) → 20 ms

**Total : 100 ms = 0,1 seconde**

**Technologie :** Edge Computing (traitement dans le véhicule)

---

#### Technologies pour la vélocité

**Streaming de données :**
- **Apache Kafka** : Système de messages distribués
- **Apache Flink** : Traitement de flux en temps réel
- **Spark Streaming** : Extension Spark pour données en flux

**Exemple d'architecture :**
```
Véhicules → Kafka → Spark Streaming → Alertes
                          ↓
                      Stockage
```

**Use case :** Détection en temps réel de conduite dangereuse

---

### 3. Variété

**La diversité des types de données**

#### Classification

**1. Données structurées (20%)**
- Format fixe, tableaux
- Bases de données relationnelles
- Exemple : Historique de ventes

| VIN | Date | Modèle | Prix |
|-----|------|--------|------|
| 1234 | 2024-01-15 | Clio | 18000 |

---

**2. Données semi-structurées (10%)**
- Structure flexible (JSON, XML)
- Logs applicatifs
- Exemple : Log calculateur

```json
{
  "timestamp": "2024-11-02T14:30:00Z",
  "vin": "VF1234567890",
  "event": "ENGINE_TEMP_HIGH",
  "temperature": 98.5,
  "location": {"lat": 48.8566, "lon": 2.3522}
}
```

---

**3. Données non structurées (70%)**
- Pas de format prédéfini
- Images, vidéos, audio, texte libre
- Exemple :
  - Vidéos des caméras ADAS
  - Notes de maintenance (texte libre)
  - Enregistrements vocaux du support client

**Défi :** Extraire de la valeur de ces données

---

#### Exemple automobile : Fusion de données

**Pour prédire une panne moteur, on combine :**

1. **Structurées** :
   - Kilométrage, âge véhicule, historique entretien

2. **Semi-structurées** :
   - Logs calculateur (JSON)
   - Données CAN bus

3. **Non structurées** :
   - Notes mécanicien ("bruit inhabituel au démarrage")
   - Photos de pièces usées

**Technologies :**
- Bases de données NoSQL (MongoDB, Cassandra)
- Data Lakes (stockage unifié)
- NLP pour analyser le texte

---

### 4. Véracité

**La qualité et la fiabilité des données**

#### Problèmes courants

❌ **Données manquantes**
```
VIN: 1234, Température: NULL, Pression: 2.1 bar
```
→ Capteur défaillant ? Donnée non enregistrée ?

❌ **Données aberrantes**
```
Température moteur: -273°C
```
→ Impossible physiquement (0 Kelvin)

❌ **Données contradictoires**
```
Source A: Véhicule en France
Source B (GPS): Véhicule au Japon (même instant)
```

❌ **Données obsolètes**
```
Dernière mise à jour: Il y a 6 mois
```
→ Encore pertinente ?

---

#### Impact sur l'IA

**Règle d'or :**
> "Garbage In, Garbage Out" (GIGO)

**Conséquences :**
- Modèle ML entraîné sur données de mauvaise qualité → Prédictions erronées
- Décisions business basées sur données fausses → Pertes financières
- Sécurité compromise (ex: ADAS avec capteurs défaillants)

**Statistique :**
- Les data scientists passent 80% de leur temps à nettoyer les données
- Seulement 20% sur la modélisation

---

#### Solutions pour améliorer la véracité

**1. Validation à la source**
```python
if temperature < -50 or temperature > 150:
    flag_as_anomaly()
```

**2. Détection d'anomalies**
- Algorithmes statistiques
- Machine Learning (Isolation Forest, Autoencoders)

**3. Règles métier**
```python
if kilométrage < kilométrage_précédent:
    raise DataError("Kilométrage ne peut pas diminuer")
```

**4. Traçabilité**
- Qui a créé la donnée ?
- Quand ?
- Quelle version du capteur/logiciel ?

**5. Master Data Management (MDM)**
- Référentiel unique (ex: liste VINs valides)
- Dédoublonnage

---

### 5. Valeur

**Transformer les données en insights actionnables**

> "Les données n'ont de valeur que si elles mènent à l'action"

#### Pyramide de la valeur

```
        Décisions & Actions
              ↑
         Insights (Pourquoi ?)
              ↑
      Analytics (Quoi ?)
              ↑
         Informations
              ↑
          Données brutes
```

---

#### Exemple : De la donnée à la décision

**Niveau 1 : Données brutes**
```
VIN1: 15000 km, 2 ans, 0 pannes
VIN2: 180000 km, 10 ans, 3 pannes
VIN3: 95000 km, 5 ans, 1 panne
... (100 000 véhicules)
```

**Niveau 2 : Information**
```
Âge moyen du parc: 6,2 ans
Kilométrage moyen: 85 000 km
```

**Niveau 3 : Analyse**
```
Les véhicules > 150 000 km ont 4x plus de pannes
```

**Niveau 4 : Insight**
```
Les clients avec véhicules haute kilométrie
sont les plus coûteux en SAV
```

**Niveau 5 : Décision**
```
Actions:
1. Cibler ces clients pour renouvellement
2. Adapter l'offre de garantie étendue
3. Optimiser stock pièces détachées
```

---

#### Mesurer la valeur

**ROI (Return on Investment)**

**Exemple : Projet maintenance prédictive**

**Coûts :**
- Infrastructure Big Data : 500 k€
- Équipe (3 personnes, 1 an) : 300 k€
- **Total : 800 k€**

**Gains :**
- Réduction rappels : 2 M€/an
- Amélioration satisfaction client : 500 k€/an
- **Total : 2,5 M€/an**

**ROI = (2,5 - 0,8) / 0,8 = 212%**
**Retour sur investissement en 4 mois**

---

## Architecture d'un système Big Data

### Vue d'ensemble

```
┌─────────────────────────────────────────────────┐
│              SOURCES DE DONNÉES                 │
├─────────────────────────────────────────────────┤
│  Véhicules | Usines | Web | Fournisseurs | ... │
└──────────────────────┬──────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────┐
│              INGESTION / COLLECTE               │
├─────────────────────────────────────────────────┤
│     Kafka | ETL | APIs | IoT Hub | Scrapers     │
└──────────────────────┬──────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────┐
│              STOCKAGE (Data Lake)               │
├─────────────────────────────────────────────────┤
│  Raw Data | HDFS | Cloud Storage | Databases    │
└──────────────────────┬──────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────┐
│              TRAITEMENT / ANALYSE               │
├─────────────────────────────────────────────────┤
│  Spark | Hadoop | Presto | Machine Learning     │
└──────────────────────┬──────────────────────────┘
                       │
                       ↓
┌─────────────────────────────────────────────────┐
│              VISUALISATION / SERVING            │
├─────────────────────────────────────────────────┤
│  Dashboards | APIs | Reports | Applications     │
└─────────────────────────────────────────────────┘
```

---

### 1. Couche d'ingestion

**Rôle : Collecter les données de sources hétérogènes**

#### Technologies clés

**Apache Kafka**
- Système de messaging distribué
- Haute disponibilité
- Gestion de millions d'événements/seconde

**ETL (Extract, Transform, Load)**
- Extract : Récupération données sources
- Transform : Nettoyage, formatage
- Load : Chargement dans le système cible

**IoT Hubs**
- Azure IoT Hub, AWS IoT Core
- Spécialisés pour données capteurs

---

#### Exemple : Ingestion de données véhicules

```
Flotte véhicules (2M)
    │
    ├── 4G/5G Connection
    │
    ↓
Kafka Topic: "vehicle_telemetry"
    │
    ├── Partition 1 : Véhicules région Nord
    ├── Partition 2 : Véhicules région Sud
    └── Partition 3 : Véhicules région Est/Ouest
    │
    ↓
Data Lake (stockage brut)
```

**Bénéfices :**
- Scalabilité : Ajout facile de partitions
- Résilience : Réplication des données
- Découplage : Producteurs et consommateurs indépendants

---

### 2. Couche de stockage

**Rôle : Stocker les données de manière scalable et économique**

#### Approches

**1. Data Warehouse (entrepôt de données)**
- Données structurées, schéma défini
- Optimisé pour requêtes analytiques
- Exemples : Snowflake, BigQuery, Redshift

**2. Data Lake (lac de données)**
- Stockage brut de toutes données (structurées ou non)
- Schéma à la lecture (schema-on-read)
- Exemples : HDFS, S3, Azure Data Lake

**3. Lakehouse**
- Fusion des deux approches
- Exemple : Databricks Lakehouse, Delta Lake

---

#### Comparaison

| Critère | Data Warehouse | Data Lake |
|---------|----------------|-----------|
| **Données** | Structurées | Tous types |
| **Schéma** | À l'écriture | À la lecture |
| **Coût** | Élevé | Économique |
| **Performance** | Rapide (requêtes connues) | Variable |
| **Flexibilité** | Faible | Élevée |
| **Usage** | BI, reporting | Data science, ML |

---

#### Organisation d'un Data Lake

```
Data Lake
│
├── raw/                      # Données brutes
│   ├── vehicle_telemetry/
│   ├── maintenance_logs/
│   └── sales/
│
├── processed/                # Données nettoyées
│   ├── vehicle_telemetry_clean/
│   └── sales_enriched/
│
├── curated/                  # Données agrégées
│   ├── daily_fleet_summary/
│   └── monthly_sales_kpis/
│
└── ml/                       # Datasets ML
    ├── predictive_maintenance/
    └── customer_segmentation/
```

**Principe : "Zone d'atterrissage" → "Zone transformée" → "Zone consommation"**

---

### 3. Couche de traitement

**Rôle : Transformer et analyser les données**

#### Apache Spark

**Le framework de référence pour le Big Data**

**Caractéristiques :**
- Traitement distribué en mémoire (100x plus rapide que Hadoop)
- API en Python (PySpark), Scala, Java, R
- Gère batch et streaming
- Intègre ML (MLlib)

---

#### Exemple : Analyse avec PySpark

**Problème :** Calculer la température moteur moyenne par modèle de véhicule

**Données :** 10 milliards d'enregistrements de télémétrie

```python
from pyspark.sql import SparkSession

# Initialiser Spark
spark = SparkSession.builder.appName("TempAnalysis").getOrCreate()

# Lire les données (format Parquet)
df = spark.read.parquet("gs://bucket/vehicle_telemetry/")

# Analyse
result = df.groupBy("vehicle_model") \
           .agg({"engine_temp": "avg"}) \
           .orderBy("avg(engine_temp)", ascending=False)

# Afficher
result.show()
```

**Résultat en quelques minutes sur un cluster**, même avec milliards de lignes !

---

#### Pourquoi Spark est distribué ?

**Architecture :**

```
Driver (coordonne)
    │
    ├── Worker 1 (traite partition 1)
    ├── Worker 2 (traite partition 2)
    ├── Worker 3 (traite partition 3)
    └── Worker N (traite partition N)
```

**Parallélisation automatique :**
- Données réparties sur N workers
- Chaque worker traite sa partition
- Agrégation finale des résultats

**Exemple :**
- 10 milliards de lignes
- 100 workers
- Chaque worker traite 100 millions de lignes
- Temps divisé par 100 !

---

### 4. Couche de visualisation

**Rôle : Rendre les insights accessibles aux utilisateurs**

#### Outils

**Business Intelligence :**
- **Tableau** : Visualisations interactives
- **Power BI** : Intégration Microsoft
- **Looker** : Analytics moderne
- **Superset** : Open source (Apache)

**Notebooks :**
- **Jupyter** : Standard data science
- **Databricks Notebooks** : Intégré Spark

**Dashboards custom :**
- Applications web (React, Vue.js)
- APIs REST pour intégration

---

#### Exemple de dashboard pour flotte automobile

**KPIs principaux :**

📊 **Vue d'ensemble**
- Nombre de véhicules actifs
- Kilométrage total parcouru (aujourd'hui)
- Alertes critiques en cours

📈 **Tendances**
- Évolution température moteur moyenne (7 jours)
- Distribution kilométrage journalier
- Top 10 codes d'erreur

🗺️ **Carte géographique**
- Localisation des véhicules
- Heatmap des zones de conduite

⚠️ **Alertes**
- Véhicules avec anomalies détectées
- Prédictions de pannes (7 jours)

---

## Technologies de l'écosystème Big Data

### Stockage distribué

- **HDFS (Hadoop Distributed File System)** : Historique, toujours utilisé
- **Amazon S3** : Stockage objet cloud le plus populaire
- **Google Cloud Storage** : Alternative GCP
- **Azure Blob Storage** : Alternative Azure

---

### Traitement batch

- **Hadoop MapReduce** : Premier framework (obsolète)
- **Apache Spark** : Standard actuel
- **Apache Flink** : Concurrent de Spark
- **Presto** : Requêtes SQL sur data lake

---

### Traitement streaming

- **Apache Kafka** : Plateforme de streaming #1
- **Apache Flink** : Excellent pour streaming
- **Spark Streaming** : Extension Spark
- **Amazon Kinesis** : Managed sur AWS

---

### Bases de données NoSQL

**Key-Value :**
- **Redis** : In-memory, ultra-rapide
- **DynamoDB** : AWS managed

**Document :**
- **MongoDB** : Le plus populaire
- **Couchbase** : Performant

**Column-family :**
- **Cassandra** : Haute disponibilité
- **HBase** : Basé sur Hadoop

**Graph :**
- **Neo4j** : Relations complexes

---

### Orchestration

- **Apache Airflow** : Orchestration de workflows (le plus utilisé)
- **Luigi** : Alternative Spotify
- **Argo** : Pour Kubernetes

**Rôle :** Planifier et coordonner les jobs
- Exemple : "Tous les jours à 2h, extraire les données, les transformer, et générer les rapports"

---

## Cas pratique : Visualisation de données capteurs embarqués

### Objectif

Analyser et visualiser des données réelles de capteurs provenant de véhicules Volvo (dataset RIIB)

**Dataset RIIB (Robot for Interaction in Buildings)**
- Images de caméras embarquées
- Données de capteurs (LIDAR, odométrie)
- Cas d'usage : Navigation autonome

---

### Déroulement (1h15)

**1. Introduction au dataset (10 min)**
- Présentation de la structure
- Types de données disponibles

**2. Exploration avec notebook Python (45 min)**
- Chargement des données
- Nettoyage et préparation
- Visualisations (matplotlib, seaborn)
- Analyse statistique

**3. Questions / Discussion (20 min)**
- Interprétation des résultats
- Lien avec vos projets

---

### Notebook pratique

**→ Passage au notebook Jupyter**

`notebooks/01_visualisation_capteurs_riib.ipynb`

Nous allons :
1. Charger des images de caméras
2. Analyser des données de trajectoires
3. Créer des visualisations interactives
4. Calculer des statistiques sur les données de capteurs

---

## Points clés à retenir

### Les 5V du Big Data

1. **Volume** : Stockage distribué nécessaire (Po de données)
2. **Vélocité** : Batch, near real-time, ou real-time selon le besoin
3. **Variété** : Structuré (20%), semi-structuré (10%), non-structuré (70%)
4. **Véracité** : Qualité cruciale (GIGO : Garbage In, Garbage Out)
5. **Valeur** : Objectif ultime → Décisions actionnables

---

### Architecture Big Data

```
Sources → Ingestion (Kafka) → Stockage (Data Lake)
       → Traitement (Spark) → Visualisation (BI)
```

**Principes :**
- Distribution pour la scalabilité
- Découplage des couches
- Schema-on-read pour la flexibilité

---

### Technologies essentielles

| Besoin | Technologie |
|--------|-------------|
| Stockage | HDFS, S3, GCS |
| Traitement batch | Spark |
| Traitement streaming | Kafka, Flink |
| Bases NoSQL | MongoDB, Cassandra |
| Orchestration | Airflow |
| Visualisation | Tableau, Power BI |

---

## Pour aller plus loin

### Livres
- "Designing Data-Intensive Applications" - Martin Kleppmann (bible)
- "Big Data: Principles and best practices" - Nathan Marz

### Cours
- Coursera : "Big Data Specialization" (UC San Diego)
- Databricks Academy : Formation Spark officielle

### Certifications
- **Databricks Certified Data Engineer**
- **Google Professional Data Engineer**
- **AWS Certified Big Data - Specialty**

---

## Fin du Jour 1

### Récapitulatif

**Matin :**
- ✅ Introduction à l'IA et Big Data dans l'automobile
- ✅ Les trois types d'apprentissage (supervisé, non supervisé, renforcement)
- ✅ Lecture critique d'un projet IA

**Après-midi :**
- ✅ Les 5V du Big Data
- ✅ Architecture d'un système Big Data
- ✅ Cas pratique avec données réelles

---

### Demain – Jour 2

**Matin :**
- Cas d'usage concrets (maintenance prédictive, analyse comportementale, logistique)
- Étude de cas : IA embarquée dans véhicules connectés

**Après-midi :**
- Évaluer un projet IA (méthodologie, biais, RGPD)
- Identifier des pistes d'action pour votre entreprise
- Conclusion et plan d'action individuel

---

### Questions / Discussion

**Thèmes de discussion :**
- Quels sont les principaux défis Big Data dans votre service ?
- Quelles données collectez-vous actuellement ?
- Quels cas d'usage vous semblent les plus pertinents ?

---

## Annexe : Glossaire Big Data

**Batch processing** : Traitement de données par lots (heures/jours)

**Cluster** : Ensemble de serveurs travaillant ensemble

**Data Lake** : Stockage centralisé de toutes les données brutes

**Data Warehouse** : Entrepôt de données structurées pour l'analyse

**Distributed system** : Système réparti sur plusieurs machines

**ETL** : Extract, Transform, Load (processus de chargement de données)

**HDFS** : Hadoop Distributed File System (stockage distribué)

**Lakehouse** : Architecture combinant data lake et data warehouse

**NoSQL** : Bases de données non relationnelles

**Parquet** : Format de fichier colonnaire optimisé pour Big Data

**Partition** : Subdivision de données pour traitement parallèle

**Schema-on-read** : Schéma défini lors de la lecture (vs à l'écriture)

**Streaming** : Traitement de données en flux continu

**Worker** : Serveur exécutant une partie du traitement distribué
