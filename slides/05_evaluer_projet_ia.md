# Évaluer un projet IA

## Durée : 2h00

---

## Objectifs de ce module

- Apprendre une méthodologie rigoureuse pour évaluer un projet IA
- Comprendre les risques et biais algorithmiques
- Maîtriser les aspects RGPD et éthiques
- Pratiquer l'analyse critique en groupe

---

## Méthodologie d'analyse : Les 3 piliers

```
┌──────────────────────────────────────────┐
│    ÉVALUATION PROJET IA                  │
├──────────────────────────────────────────┤
│                                          │
│  1. VALEUR MÉTIER                        │
│     - Quel problème ?                    │
│     - Quel gain ?                        │
│     - Quel ROI ?                         │
│                                          │
│  2. FAISABILITÉ TECHNIQUE                │
│     - Données disponibles ?              │
│     - Algorithmes adaptés ?              │
│     - Infrastructure nécessaire ?        │
│                                          │
│  3. RISQUES                              │
│     - Biais algorithmiques               │
│     - Éthique et RGPD                    │
│     - Dépendances et maintenance         │
│                                          │
└──────────────────────────────────────────┘
```

---

## 1. Évaluation de la valeur métier

### Questions fondamentales

#### A. Quel problème résolvons-nous ?

**Bon problème :**
- ✅ Clairement défini
- ✅ Mesurable
- ✅ Important pour le business
- ✅ Récurrent (pas one-shot)

**Mauvais problème :**
- ❌ Vague ("améliorer la qualité")
- ❌ Pas de métriques claires
- ❌ Impact business flou
- ❌ Solution déjà existante et satisfaisante

---

#### Exemple : Projet "Améliorer la qualité logicielle"

❌ **Trop vague**

✅ **Reformulation claire :**
> "Réduire de 30% le temps de détection des bugs critiques dans les logs de compilation des calculateurs moteur, en automatisant l'analyse via Machine Learning"

**Mesurable :**
- Baseline actuelle : 4h en moyenne pour identifier un bug critique
- Objectif : 2h50 max
- Métrique : Temps moyen de détection

---

### B. Quel est le gain attendu ?

#### Quantification des bénéfices

**Gains directs (€) :**
- Réduction coûts opérationnels
- Augmentation revenus
- Évitement de pertes

**Gains indirects :**
- Amélioration satisfaction client (NPS)
- Réduction time-to-market
- Avantage concurrentiel

**Exemple calculateur :**
```
Détection bugs plus rapide (4h → 2h50)
→ 1h10 gagnée par bug
→ 100 bugs/mois
→ 117h gagnées/mois
→ 1400h/an
→ À 80€/h d'ingénieur = 112 k€/an
```

---

### C. Quel est le ROI ?

**Formule :**
```
ROI = (Gains - Coûts) / Coûts × 100%
```

**Coûts à considérer :**
- Développement initial (6-12 mois)
- Infrastructure (serveurs, licences)
- Données (collecte, nettoyage, annotation)
- Maintenance annuelle (20-30% du coût initial)

---

#### Exemple complet : Projet détection bugs

**Coûts :**
- Développement (3 data scientists × 6 mois × 7k€) : 126 k€
- Infrastructure ML (cloud) : 10 k€/an
- Annotation données initiale : 30 k€
- Maintenance (20%/an) : 25 k€/an
- **Total première année : 191 k€**

**Gains :**
- Temps ingénieurs économisé : 112 k€/an
- Réduction bugs en production (-20%) : 80 k€/an
- **Total gains : 192 k€/an**

**ROI première année : (192 - 191) / 191 = 0,5%** → Limite
**ROI année 2+ : (192 - 35) / 35 = 450%** → Excellent

**→ Rentable à partir de 13 mois**

---

### D. Y a-t-il des alternatives ?

**Toujours comparer l'IA à :**

1. **Statu quo** : Ne rien faire, quel coût ?
2. **Solution non-IA** : Règles métier, heuristiques
3. **Solution tierce** : Logiciel existant (acheter vs développer)

**Exemple :**
- Développer IA interne : 191 k€
- Acheter outil SonarQube + plugin ML : 50 k€/an
- → Peut-être acheter est plus pertinent !

**Règle :** L'IA n'est PAS toujours la meilleure solution

---

## 2. Faisabilité technique

### A. Disponibilité et qualité des données

**Les 4 questions clés :**

#### 1. Avons-nous assez de données ?

| Type de problème | Minimum | Recommandé |
|------------------|---------|------------|
| Régression simple | 1 000 | 10 000+ |
| Classification | 1 000 par classe | 10 000+ par classe |
| Deep Learning (images) | 10 000 | 100 000+ |
| NLP (texte) | 10 000 | 1 000 000+ |

**Règle empirique :** 10x le nombre de features minimum

---

#### 2. Les données sont-elles de bonne qualité ?

**Checklist qualité :**

- [ ] **Complétude** : < 10% de valeurs manquantes ?
- [ ] **Exactitude** : Données cohérentes (pas de température -273°C) ?
- [ ] **Fraîcheur** : Données récentes (< 1 an) ?
- [ ] **Représentativité** : Couvrent tous les cas d'usage ?
- [ ] **Équilibre** : Classes équilibrées (pas 99% vs 1%) ?

**Si NON à plusieurs → Projet à risque**

---

#### 3. Avons-nous les bons labels ?

**Pour l'apprentissage supervisé, crucial !**

**Exemple : Détection bugs critiques dans logs**

❌ **Labels inexploitables :**
```
Log 1 : "Erreur" → Trop vague
Log 2 : "Problème" → Pas clair
```

✅ **Bons labels :**
```
Log 1 : "Bug critique - Overflow mémoire"
Log 2 : "Warning mineur - Variable unused"
Log 3 : "Bug bloquant - Segmentation fault"
```

**Coût d'annotation :**
- Manuelle : 5-50€/heure selon complexité
- Nécessite expertise métier
- 10 000 logs × 30s = 83h = 4 000€

---

#### 4. Les données sont-elles accessibles ?

**Obstacles fréquents :**
- Données dans systèmes legacy (difficulté d'extraction)
- Silotage entre départements
- Restrictions légales (RGPD)
- Données chez partenaire/fournisseur

**Exemple automobile :**
- Données véhicules : Propriété constructeur ? Conducteur ?
- Données fournisseurs : Partage possible ?

**→ Clarifier AVANT de lancer le projet**

---

### B. Choix de l'algorithme

#### Arbre de décision simplifié

```
Quel est votre objectif ?
│
├─ Prédire une CATÉGORIE
│  │
│  ├─ Données tabulaires → Random Forest, XGBoost
│  ├─ Images → CNN (Convolutional Neural Networks)
│  ├─ Texte → Transformers (BERT, GPT)
│  └─ Séries temporelles → LSTM, GRU
│
├─ Prédire une VALEUR NUMÉRIQUE
│  │
│  ├─ Relation linéaire → Régression linéaire
│  ├─ Relation complexe → XGBoost, Neural Networks
│  └─ Séries temporelles → ARIMA, Prophet
│
└─ Découvrir des GROUPES
   └─ Clustering → K-Means, DBSCAN, Hierarchical
```

---

#### Critères de choix

| Critère | Importance | Exemples |
|---------|-----------|----------|
| **Performance** | ⭐⭐⭐ | XGBoost souvent meilleur |
| **Interprétabilité** | ⭐⭐⭐ | Arbres décision > Réseaux neurones |
| **Temps d'entraînement** | ⭐⭐ | Logistic Regression rapide |
| **Temps d'inférence** | ⭐⭐⭐ | Critique si temps réel |
| **Taille du modèle** | ⭐⭐ | Important si embarqué |

**Automobile = Interprétabilité et temps d'inférence cruciaux**

---

### C. Infrastructure nécessaire

#### On-premise vs Cloud

**On-premise (serveurs internes) :**
- ✅ Contrôle total
- ✅ Pas de coûts variables
- ✅ Données restent en interne
- ❌ Investissement initial élevé
- ❌ Maintenance complexe
- ❌ Scalabilité limitée

**Cloud (AWS, GCP, Azure) :**
- ✅ Pay-as-you-go
- ✅ Scalabilité infinie
- ✅ Services managés (moins de maintenance)
- ❌ Coûts récurrents
- ❌ Dépendance fournisseur
- ❌ Données dans cloud (RGPD à gérer)

---

#### Composants nécessaires

**Stack ML typique :**

1. **Stockage** : Data Lake (S3, GCS, Azure Blob)
2. **Compute** : GPU pour entraînement (cher : 1-10€/h)
3. **Orchestration** : Airflow, Kubeflow
4. **ML Platform** : MLflow, SageMaker, Vertex AI
5. **Serving** : API REST pour inférence
6. **Monitoring** : Grafana, Prometheus

**Budget mensuel exemple (startup) : 5-20 k€/mois**
**Groupe automobile : 500 k€ - 2 M€/mois**

---

### D. Compétences de l'équipe

**Rôles nécessaires :**

| Rôle | Compétences | Ratio |
|------|-------------|-------|
| **Data Scientist** | ML, stats, Python | 40% |
| **Data Engineer** | ETL, Big Data, infra | 30% |
| **ML Engineer** | Déploiement, DevOps | 20% |
| **Expert métier** | Connaissance domaine | 10% |

**Équipe minimale pour projet :** 3-5 personnes

**Disponibilité chez Stellantis/Renault ?**
- Former en interne (6-12 mois)
- Recruter (marché tendu, salaires élevés)
- Sous-traiter (consulting, mais coûteux)

---

## 3. Risques et mitigation

### A. Biais algorithmiques

#### Qu'est-ce qu'un biais ?

> **"Erreur systématique conduisant à des prédictions injustes ou discriminatoires"**

**Origine :**
1. **Biais des données** : Données non représentatives
2. **Biais d'algorithme** : Certains algorithmes amplifient biais
3. **Biais de feedback** : Prédictions influencent données futures

---

#### Exemples de biais

**1. Biais de sélection**

**Contexte : Prédiction de pannes**
- Entraîné uniquement sur véhicules ayant eu révision
- Véhicules mal entretenus (jamais en révision) absents des données
- → Modèle sous-estime risque de ces véhicules

**Mitigation :**
- Collecte de données sur TOUS véhicules (y compris non révisés)
- Pondération pour compenser déséquilibre

---

**2. Biais de mesure**

**Contexte : Capteurs température moteur**
- Capteurs Série A (précis) : ±0,5°C
- Capteurs Série B (ancien) : ±3°C
- Modèle apprend noise de Série B → Moins performant

**Mitigation :**
- Uniformiser capteurs
- Feature engineering (indiquer série capteur)
- Calibration

---

**3. Biais historique**

**Contexte : Assistant vocal**
- Entraîné sur voix masculines principalement (historiquement, conducteurs majoritairement hommes)
- Moins performant sur voix féminines et enfants

**Mitigation :**
- Dataset équilibré (50% hommes, 50% femmes)
- Augmentation de données (modifier pitch)
- Tests sur tous groupes

---

#### Détection des biais

**Méthodes :**

1. **Analyse de performance par sous-groupe**
   - Précision pour conducteurs jeunes vs âgés ?
   - Précision pour véhicules neufs vs anciens ?

2. **Matrice de confusion détaillée**
   - Faux négatifs plus fréquents sur un groupe ?

3. **Tests d'équité (fairness metrics)**
   - Demographic parity
   - Equal opportunity
   - Predictive parity

**Outil recommandé : Fairlearn (Microsoft)**

---

### B. Explicabilité (Explainability)

#### Pourquoi l'explicabilité est cruciale en automobile ?

1. **Confiance** : Mécanicien doit comprendre pourquoi changement pièce
2. **Debugging** : Si erreur, comprendre pourquoi
3. **Réglementation** : RGPD droit à l'explication
4. **Certification** : ISO 26262 nécessite traçabilité

---

#### Spectre d'interprétabilité

```
Interprétable ←────────────────────────→ Boîte noire

Régression     Arbres      Random      XGBoost    Neural
linéaire       décision    Forest                 Networks
                                                   (Deep)
```

**Trade-off performance vs interprétabilité**

---

#### Techniques d'explicabilité

**1. Feature Importance**
Quelles variables ont le plus d'impact ?

**Exemple : Prédiction panne batterie**
```
1. Âge batterie : 35%
2. Nombre cycles charge : 28%
3. Température moyenne : 20%
4. Voltage : 12%
5. Autres : 5%
```

---

**2. SHAP (SHapley Additive exPlanations)**

**Explication au niveau instance :**

```
Véhicule #1234 prédit "Panne probable"

Contributions :
Âge batterie (6 ans) : +0.3
Voltage faible (11.8V) : +0.25
Température élevée (40°C) : +0.15
Cycles charge élevés : +0.1
────────────────────────────
Score final : 0.8 (Panne probable)
```

**→ Mécanicien comprend : "Batterie vieille + Voltage faible = À changer"**

---

**3. LIME (Local Interpretable Model-agnostic Explanations)**

**Principe :** Approximer modèle complexe localement par modèle simple

**Usage :**
- Expliquer pourquoi CETTE image est classée "Piéton"
- Afficher zones d'attention (heatmap)

---

#### Recommandation pour l'automobile

**Privilégier modèles interprétables si possible :**
- Random Forest > Deep Neural Networks
- Sauf si gain de performance justifie la complexité

**Si modèle complexe nécessaire :**
- Implémenter SHAP/LIME
- Dashboard d'explication pour utilisateurs
- Documentation détaillée

---

### C. RGPD et protection des données

#### Principes du RGPD

**6 principes clés :**

1. **Licéité** : Base légale (consentement, contrat, intérêt légitime)
2. **Limitation des finalités** : Utiliser uniquement pour objectif annoncé
3. **Minimisation** : Collecter seulement le nécessaire
4. **Exactitude** : Données à jour et corrigées si erronées
5. **Limitation de la conservation** : Durée définie
6. **Intégrité et confidentialité** : Sécurité

---

#### Droits des personnes

**Conducteurs ont le droit :**

- **Accès** : Voir leurs données
- **Rectification** : Corriger erreurs
- **Effacement** : "Droit à l'oubli"
- **Portabilité** : Récupérer données (format lisible)
- **Limitation** : Demander arrêt du traitement
- **Opposition** : Refuser traitement (sauf intérêt légitime)

**Application automobile :**
- Interface dans l'appli constructeur
- Export CSV/JSON des données
- Suppression en 30 jours max

---

#### Données sensibles en automobile

**Particulièrement sensibles :**

- **Localisation GPS** : Trajets révèlent habitudes, domicile, lieux fréquentés
- **Comportement de conduite** : Peut inférer état de santé (détection somnolence)
- **Enregistrements vocaux** : Conversations privées
- **Caméras habitacle** : Image visage, passagers

**Obligations renforcées :**
- Consentement explicite (opt-in)
- Anonymisation / Pseudonymisation
- Chiffrement
- Audits réguliers

---

#### Cas pratique : Conformité RGPD d'un projet

**Projet : Analyse comportementale conducteurs**

**Checklist RGPD :**

- [ ] Base légale définie (consentement)
- [ ] Information claire donnée au conducteur
- [ ] Opt-in (désactivé par défaut)
- [ ] Minimisation (seulement données nécessaires)
- [ ] Anonymisation (pas de lien direct identité ↔ données)
- [ ] Durée de conservation définie (ex: 2 ans)
- [ ] Droit d'accès implémenté (dashboard)
- [ ] Droit à l'effacement implémenté
- [ ] Sécurité (chiffrement en transit et au repos)
- [ ] DPO (Data Protection Officer) consulté
- [ ] DPIA (Data Protection Impact Assessment) réalisée si risque élevé

---

#### Sanctions en cas de non-conformité

**CNIL peut infliger :**
- Avertissement
- Mise en demeure
- Limitation temporaire du traitement
- **Amende jusqu'à 4% du CA mondial ou 20 M€**

**Exemples récents :**
- Amazon : 746 M€ (2021)
- Google : 90 M€ (2020)
- Renault : Pas de sanction publique connue (encore)

**→ Conformité RGPD = Impératif business**

---

### D. Dépendances et maintenance

#### Dépendances techniques

**Risques :**

1. **Vendor lock-in** : Dépendance à un fournisseur cloud
   - Coût de migration élevé
   - Perte de contrôle sur prix

2. **Obsolescence** : Technologies évoluent vite
   - TensorFlow 1.x → 2.x (breaking changes)
   - Python 2 → 3

3. **APIs tierces** : Service externe disparaît
   - Google Vision API change de prix
   - Startup rachetée, service fermé

---

**Mitigation :**

- **Multi-cloud** : Ne pas mettre tous œufs dans même panier (mais complexe)
- **Abstractions** : Couches d'abstraction pour changer facilement
- **Open-source privilégié** : Moins de risque de disparition
- **Veille technologique** : Anticiper obsolescence

---

#### Maintenance du modèle

**Modèle ML n'est PAS statique**

**Phénomène de drift :**
> **"Performance du modèle dégrade au fil du temps"**

**Causes :**
- Distribution des données change (concept drift)
- Relation input/output change (covariate drift)

**Exemple automobile :**
- Modèle entraîné sur essence, flotte devient électrique
- Performance se dégrade car caractéristiques différentes

---

**Monitoring nécessaire :**

**Métriques à suivre :**
1. **Précision du modèle** (si labels dispos)
2. **Distribution des entrées** (détection drift)
3. **Temps d'inférence** (dégradation perf système)
4. **Feedback utilisateurs** (insatisfaction)

**Actions si drift détecté :**
- Réentraînement avec nouvelles données
- Fine-tuning
- Si échec : Reconsidérer architecture

**Fréquence réentraînement :** Tous les 3-6 mois (selon domaine)

---

## Atelier : Analyse critique d'un projet IA (60 min)

### Cas d'étude : Système de prédiction de valeur résiduelle

---

### Description du projet

**Contexte :**
Renault souhaite prédire la valeur de revente d'un véhicule d'occasion après 3 ans, pour optimiser les offres de location longue durée (LLD).

**Données disponibles (200 000 véhicules) :**
- Modèle, motorisation, options
- Kilométrage, âge
- Historique entretien
- État du véhicule (évaluation à la reprise)
- Prix de revente réel

**Algorithme proposé :** XGBoost (régression)

**Déploiement :** API REST utilisée par équipes commerciales

---

### Travail en 4 groupes (35 min)

**Chaque groupe analyse un aspect :**

#### Groupe 1 : Valeur métier
- Quel problème cela résout ?
- Quel est le ROI estimé ?
- Y a-t-il des alternatives ?

#### Groupe 2 : Faisabilité technique
- Les données sont-elles suffisantes et de qualité ?
- XGBoost est-il adapté ?
- Quelle infrastructure ?

#### Groupe 3 : Biais et explicabilité
- Quels biais potentiels ?
- Explicabilité nécessaire ? Comment ?
- Tests de fairness à prévoir ?

#### Groupe 4 : RGPD et risques
- Conformité RGPD ?
- Dépendances et maintenance ?
- Plan de mitigation des risques ?

---

### Restitution (25 min)

**Chaque groupe présente (5 min) :**
- Principaux constats
- Forces du projet
- Points de vigilance
- Recommandations

---

### Correction : Points clés attendus

#### Valeur métier

**Problème :**
- Aujourd'hui : Estimation manuelle, imprécise (±15%)
- Impact : Offres LLD peu compétitives OU marges faibles

**ROI potentiel :**
- 50 000 LLD/an
- Amélioration précision → +5% de marge
- Gain : 10-20 M€/an (selon prix moyen véhicule)

**Alternative :**
- Cotation Argus (service tiers)
- Mais : Données génériques, pas spécifique à Renault

**→ ROI excellent, projet pertinent**

---

#### Faisabilité technique

**Données :**
- ✅ 200 000 véhicules = Suffisant
- ⚠️ Qualité "état véhicule" : Subjective, peut varier selon évaluateur
- ⚠️ Données externes manquantes : Cote occasion, tendances marché

**Algorithme :**
- ✅ XGBoost adapté (régression, données tabulaires)
- ✅ Interprétable (feature importance)

**Infrastructure :**
- Simple : API REST (latence non critique)
- Cloud ou on-premise viable

**→ Faisable, mais attention qualité données**

---

#### Biais et explicabilité

**Biais potentiels :**
- **Biais géographique** : Données principalement France, moins pertinent pour export
- **Biais temporel** : Marché occasion fluctue (Covid, pénurie semi-conducteurs)
- **Biais de sélection** : Véhicules repris ≠ Véhicules revendus par particuliers

**Explicabilité :**
- ✅ Nécessaire pour commerciaux (justifier offre client)
- Feature importance + SHAP
- Dashboard : "Valeur estimée 15 k€ car kilométrage faible (60%) + bon entretien (30%)"

**→ Explicabilité = Avantage concurrentiel (vs Argus boîte noire)**

---

#### RGPD et risques

**RGPD :**
- ⚠️ Données véhicule = Données personnelles si identifiables
- Solution : Anonymisation (hash VIN)
- Durée conservation : 5 ans (durée de vie LLD)

**Risques :**
- **Drift** : Marché occasion change → Réentraînement trimestriel nécessaire
- **Dépendance** : Si API tombe, commerciaux bloqués → Fallback sur méthode manuelle
- **Erreurs** : Sur/sous-estimation → Pertes financières → Monitoring continu

**Plan de mitigation :**
- A/B testing avant déploiement complet
- Rollout progressif (10% commerciaux → 100%)
- KPI : Écart estimation vs réel < 10%

**→ Risques maîtrisables avec bonne gouvernance**

---

### Conclusion atelier

**Faut-il faire ce projet ?**

**✅ OUI, MAIS avec conditions :**

1. **Améliorer données** : Enrichir avec cote Argus, données externes
2. **Pilot** : 6 mois avec 20% flotte pour valider
3. **Explicabilité** : Dashboard pour commerciaux (obligatoire)
4. **Monitoring** : KPIs précis, alertes si drift
5. **Réentraînement** : Prévoir process tous les 3 mois
6. **Budget** : 300 k€ développement + 50 k€/an maintenance

**ROI projeté : 10 M€/an vs 300 k€ → Go !**

---

## Points clés à retenir

### Méthodologie en 3 étapes

1. **Valeur métier** : Quel problème ? Quel ROI ? Alternatives ?
2. **Faisabilité** : Données, algorithmes, infra, compétences
3. **Risques** : Biais, RGPD, dépendances, maintenance

**Tous les 3 doivent être validés**

---

### Biais algorithmiques

- Origine : Données non représentatives, feedback loops
- Détection : Tests par sous-groupes, fairness metrics
- Mitigation : Collecte équilibrée, pondération, audits

---

### Explicabilité

- Cruciale en automobile (confiance, certification)
- Privilégier modèles interprétables si possible
- Sinon : SHAP, LIME, dashboards

---

### RGPD

- 6 principes, droits des personnes
- Données sensibles (GPS, caméras) = Vigilance ++
- Non-conformité = Amendes 4% CA

---

## Ressources

### Outils d'explicabilité
- **SHAP** : https://github.com/slundberg/shap
- **LIME** : https://github.com/marcotcr/lime
- **Fairlearn** (Microsoft) : https://fairlearn.org/

### RGPD
- Guide CNIL : https://www.cnil.fr/
- DPIA template : https://ico.org.uk/for-organisations/

### Lectures
- "Weapons of Math Destruction" - Cathy O'Neil (biais)
- "Interpretable Machine Learning" - Christoph Molnar (gratuit en ligne)

---

## Pause - 15 minutes

**À suivre :**
- Identifier des pistes d'action pour votre entreprise
- Conclusion de la formation
- Plan d'action individuel
