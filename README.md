# Python SysAdmin Training

Bienvenue dans ce projet **Python SysAdmin Training** !

Ce dépôt propose un **parcours progressif et pratique** pour apprendre **Python
à travers des cas concrets d’administration système**. Pas de théorie abstraite
ici : chaque TP vous met dans la peau d’un admin qui cherche à automatiser une
tâche fastidieuse, surveiller un système, appeler une API ou générer un rapport.

C’est un guide pour monter en compétences **par la pratique**, avec des exemples
issus du quotidien des administrateurs systèmes.

---

## 🎯 Objectifs

* 🐍 Apprendre les bases du langage Python dans un contexte sysadmin.
* ⚙️ Automatiser des tâches à faible valeur ajoutée (nettoyage de fichiers,
  surveillance, backup…).
* 📈 Écrire des scripts robustes, testables et réutilisables.
* 🌐 Interagir avec des APIs, manipuler des fichiers de configuration (YAML,
  JSON), gérer des processus à distance.
* 🧪 Tester automatiquement vos scripts avec `pytest` et `testinfra`.

---

## 📚 Structure du Projet

Le projet est composé de deux parties :

1. **formation-base** : Concepts fondamentaux de Python.
2. **automatisation** : Exercices pratiques pour appliquer ces concepts dans un
   contexte d’administration système.

### Formation de base

**TP Disponibles :**

* [`00-Intro-Python`](./00-formation-base/00-Intro-Python) — Introduction à Python, syntaxe de base,
  variables, types de données.
* [`01-Structures-Collections`](./00-formation-base/01-Structures-Collections) — Structures de contrôle (if/else, boucles) et collections (listes, tuples, dictionnaires).
* [`02-Fonctions`](./00-formation-base/02-Fonctions) — Création de fonctions, paramètres, valeurs
  par défaut, lambdas, récursion.

### Automatisation

**TP Disponibles :**

* [`01-Nmap`](./01-automatisation/01-Nmap) — Utilisation de Nmap pour scanner des réseaux.

**Idées de TP** :

* [`02-Backup`](./01-automatisation/01-Backup) — Script de sauvegarde de fichiers.
* [`03-Log-Parser`](./01-automatisation/02-Log-Parser) — Analyse de fichiers log pour extraire des
  informations pertinentes.
* [`04-API-Client`](./01-automatisation/03-API-Client) — Client pour interagir avec une API REST
  (par exemple, récupérer des données météo).
* ...

---

## 🔧 Prérequis

* Un environnement Linux ou Incus (containers LXD-compatible avec systemd).
* Python 3.10 ou supérieur.
* Les outils suivants installés :

```bash
pipx install pytest
pipx inject pytest pytest-testinfra
```

> Une configuration Incus est recommandée pour certains TP. Voir ci-dessous.

---

### Installation d'Incus (facultatif mais recommandé)

Pour isoler proprement chaque TP dans un conteneur Linux, tu peux utiliser
**Incus**. Cf. guide complet d’installation ici :
[https://www.stephane-robert.info/docs/homelab/incus/](https://www.stephane-robert.info/docs/homelab/incus/)

---

## 🚀 Démarrage rapide

1. **Cloner le dépôt :**

```bash
git clone https://github.com/stephrobert/python-training.git
cd python-sysadmin-training
```

2. **Choisissez un TP et suivez les consignes dans le fichier `README.md` du
   dossier correspondant.**
3. **Les tests se lancent avec :**

```bash
pytest tests/
```

> Certains TP peuvent inclure des fichiers de simulation (`log.txt`,
> `users.csv`, etc.) dans un dossier `data/`.

---

## 🔄 Mise à jour du dépôt

Je continuerai à enrichir ce dépôt avec de nouveaux TP, inspirés de cas réels,
et des corrections issues des retours de la communauté.

```bash
git pull origin main
```

---

## 🤝 Contribuer

Vous avez une idée de TP ? Un script utile à partager ? Une amélioration à
proposer ?

1. Ouvrez une **issue** pour discuter du sujet.
2. Proposez une **pull request** avec un nouveau dossier TP complet :
   `README.md`, `main.py`, `tests/`, `data/`.

---

## ☕ Me soutenir

Si ce travail vous aide ou vous inspire, vous pouvez me soutenir ici :

[![Ko-fi](https://www.ko-fi.com/img/githubbutton_sm.svg)](https://ko-fi.com/stephanerobert89902)

---

## 📄 Licence

* **Auteur** : Stéphane Robert (2025)
* **Licence** : [Creative Commons BY-SA
  4.0](https://creativecommons.org/licenses/by-sa/4.0/)

