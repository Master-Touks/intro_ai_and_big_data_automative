# Guide d'utilisation de la formation

## 📖 Comment utiliser ce matériel de formation ?

---

## 1. Visualiser les slides (Markdown)

Les slides sont au format Markdown (.md) et peuvent être visualisés de plusieurs façons :

### Option A : Dans votre éditeur de code (recommandé)

**VSCode :**
1. Ouvrir le fichier `.md`
2. Appuyer sur `Cmd+Shift+V` (Mac) ou `Ctrl+Shift+V` (Windows/Linux)
3. Prévisualisation Markdown s'affiche

**PyCharm :**
1. Ouvrir le fichier `.md`
2. Cliquer sur l'icône de prévisualisation en haut à droite
3. Vue Markdown s'affiche à côté du code

### Option B : Avec un visualiseur Markdown en ligne

1. Copier le contenu du fichier `.md`
2. Aller sur https://dillinger.io/
3. Coller le contenu
4. Visualisation instantanée

### Option C : Convertir en slides HTML (avancé)

**Avec Marp (recommandé pour présentation) :**

```bash
# Installer Marp CLI
npm install -g @marp-team/marp-cli

# Convertir en HTML
marp slides/01_introduction_ia_bigdata_automobile.md -o output.html

# Convertir en PDF
marp slides/01_introduction_ia_bigdata_automobile.md -o output.pdf
```

**Avec reveal-md (présentation interactive) :**

```bash
# Installer reveal-md
npm install -g reveal-md

# Lancer la présentation
reveal-md slides/01_introduction_ia_bigdata_automobile.md

# Ouvre automatiquement dans le navigateur
```

---

## 2. Utiliser les notebooks Jupyter

### Lancement de Jupyter

```bash
# Aller dans le dossier du projet
cd /Users/tukanebari/PycharmProjects/big_data_course

# Activer l'environnement virtuel (si créé)
source venv/bin/activate

# Lancer Jupyter
jupyter notebook

# Ou JupyterLab (interface moderne)
jupyter lab
```

### Naviguer dans les notebooks

1. Le navigateur s'ouvre automatiquement
2. Aller dans le dossier `notebooks/`
3. Cliquer sur le notebook souhaité (`.ipynb`)
4. Exécuter les cellules une par une : `Shift + Enter`

### Ordre recommandé

**Jour 1 :**
1. `01_visualisation_capteurs_riib.ipynb` (après les slides du matin)

**Jour 2 :**
2. `02_maintenance_predictive.ipynb` (matin)
3. `03_analyse_comportementale_conducteurs.ipynb` (après-midi)

---

### Déroulement type

#### Jour 1 Matin

**8h30 - 9h00 : Accueil et café**
- Tour de table
- Présentation des objectifs
- Vérification setup technique

**9h00 - 11h00 : Module 1 (slides/01_introduction_ia_bigdata_automobile.md)**
- Présentation théorique : 1h30
- Quiz interactif : 15 min
- Exercice lecture critique : 15 min

**11h00 - 11h15 : Pause**

**11h15 - 13h30 : Module 2 (slides/02_fondamentaux_ia.md)**
- Présentation théorique : 1h00
- Exercice pratique en groupe : 45 min
- Discussion collective : 30 min

**13h30 - 14h30 : Pause déjeuner**

#### Jour 1 Après-midi

**14h30 - 16h30 : Module 3 (slides/03_fondamentaux_bigdata.md)**
- Présentation théorique : 1h15
- Pause : 15 min
- **Notebook pratique** : 45 min
  - Lancer `notebooks/01_visualisation_capteurs_riib.ipynb`
  - Exécuter cellule par cellule
  - Expliquer les résultats

**16h30 - 17h00 : Synthèse Jour 1**
- Questions/Réponses
- Teasing Jour 2

---

#### Jour 2 Matin

**9h00 - 11h30 : Module 4 (slides/04_cas_usage_automobile.md)**
- Cas d'usage concrets : 1h30
- Pause : 15 min
- **Notebook pratique** : 1h00
  - Lancer `notebooks/02_maintenance_predictive.ipynb`
  - Construire modèle ML pas à pas
  - Analyser résultats

**11h30 - 13h30 : Pause déjeuner**

#### Jour 2 Après-midi

**13h30 - 15h30 : Module 5 (slides/05_evaluer_projet_ia.md)**
- Méthodologie d'évaluation : 1h00
- Atelier en groupe : 1h00

**15h30 - 15h45 : Pause**

**15h45 - 16h30 : Notebook pratique**
- Lancer `notebooks/03_analyse_comportementale_conducteurs.ipynb`
- Clustering K-Means

**16h30 - 18h00 : Module 6 (slides/06_pistes_action_conclusion.md)**
- Cartographie opportunités : 45 min
- Exercice d'idéation : 30 min
- Conclusion et plan d'action : 15 min

**18h00 : Clôture**

---

## 4. Conseils pédagogiques

### Pour les participants

**Maximiser l'apprentissage :**
- **Prendre des notes** dans les notebooks (cellules Markdown)
- **Poser des questions** dès que quelque chose n'est pas clair
- **Expérimenter** : Modifier le code, voir ce qui se passe
- **Réfléchir** : Comment appliquer à mon projet ?

**Après la formation :**
- Revoir les notebooks à tête reposée
- Suivre un cours en ligne (Andrew Ng recommandé)
- Identifier 1 projet concret à lancer
- Former des collègues (best way to learn = teach)

---

## 5. Résolution de problèmes courants

### Problème : Jupyter ne se lance pas

**Solution :**
```bash
# Vérifier l'installation
jupyter --version

# Si erreur, réinstaller
pip install --upgrade jupyter

# Essayer JupyterLab
pip install jupyterlab
jupyter lab
```

### Problème : Module not found (numpy, pandas, etc.)

**Solution :**
```bash
# Installer toutes les dépendances
pip install numpy pandas matplotlib seaborn scikit-learn pillow

# Vérifier l'installation
python -c "import numpy; print(numpy.__version__)"
```

### Problème : Le notebook est lent / se bloque

**Solution :**
1. Redémarrer le kernel : `Kernel → Restart`
2. Réduire la taille des données si possible
3. Fermer les autres notebooks ouverts

### Problème : Les images (RIIB) ne s'affichent pas

**Solution :**
```bash
# Vérifier que le dossier riib/ existe
ls riib/additional/

# Si absent, décompresser
python unzipping_data.py

# Vérifier PIL
python -c "from PIL import Image; print('OK')"
```

### Problème : Erreur "No module named 'sklearn'"

**Solution :**
```bash
# C'est scikit-learn, pas sklearn
pip install scikit-learn

# Vérifier
python -c "import sklearn; print(sklearn.__version__)"
```

---

## 6. Personnalisation de la formation

### Adapter à votre contexte

**Exemples spécifiques :**
- Remplacer exemples génériques par cas de votre entreprise
- Utiliser vos propres données (si possible)
- Inviter un expert métier pour témoignage

**Durée :**
- Formation complète : 2 jours (14h)
- Version courte : 1 jour (7h) - Modules 1, 2, 4, 6
- Version express : 4h - Modules 1, 4, 6 (sensibilisation)

**Niveau :**
- Débutants : Suivre ordre proposé
- Intermédiaires : Passer rapidement sur Module 2, focus sur 4 et 5
- Avancés : Focus sur Module 5 (évaluation) et exercices pratiques

---

---

## 7. Ressources complémentaires

### Slides alternatifs

Si vous préférez PowerPoint :
1. Convertir Markdown → HTML avec Marp
2. Ouvrir HTML dans navigateur
3. Imprimer en PDF
4. Importer PDF dans PowerPoint

### Vidéos d'introduction

À montrer en début de formation :
- **"What is Machine Learning?"** - 3Blue1Brown (10 min)
- **"How Tesla uses AI"** - Tesla AI Day (20 min)
- **"Big Data Explained"** - IBM (5 min)

### Datasets alternatifs

Si RIIB ne convient pas :
- [Kaggle Automotive Datasets](https://www.kaggle.com/datasets?search=automotive)
- [UCI ML Repository](https://archive.ics.uci.edu/ml/index.php)
- Créer données simulées (comme dans les notebooks)

---

## 8. Évaluation et feedback

### Quiz de fin de formation

Créer un Google Form avec :
- 10 questions QCM (concepts clés)
- 3 questions ouvertes (applications)
- 1 question de satisfaction

### Feedback participants

Questions à poser :
- Qu'avez-vous le plus apprécié ?
- Qu'avez-vous trouvé difficile ?
- Quels sujets approfondir dans formation niveau 2 ?
- Recommanderiez-vous cette formation ?

### Auto-évaluation formateur

Après chaque session :
- Quels modules ont bien fonctionné ?
- Où ai-je perdu les participants ?
- Quelles questions reviennent souvent ?
- Comment améliorer pour la prochaine fois ?

---

## 9. Versions et mises à jour (possibilité)

### Version actuelle : 1.0 (Novembre 2024)

**Prochaines versions prévues :**

**Version 1.1 (Q1 2025) :**
- Ajouter module sur IA générative (LLMs, ChatGPT, Copilot)
- Cas d'usage "Génération de tests unitaires"
- Dataset réel Stellantis/Renault (si accord)

**Version 2.0 (Formation niveau 2) :**
- Deep Learning avec TensorFlow/PyTorch
- Déploiement de modèles en production (MLOps)
- Spark avancé (PySpark)
- Projet fil rouge sur toute la formation

---

## 📧 Contact

**Questions ou suggestions ?**
- Email : [bade.tuka@gmail.com](mailto:bade.tuka@gmail.com)
- Issues GitHub : [à compléter]

---

## 🎉 Bonne formation !

**Remember:** L'objectif est de démystifier l'IA et donner envie aux participants de se lancer !

---
