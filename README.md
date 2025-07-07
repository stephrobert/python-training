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

Pour le moment, je pense à une quinzaine de TP, chacun abordant un aspect
différent de l’administration système avec Python. Chaque TP est autonome et
peut être réalisé indépendamment des autres. Vous pouvez les suivre dans l’ordre
qui vous convient.

**TP Disponibles :**

* [`00-Intro-Python`](./00-Intro-Python) — Introduction à Python, syntaxe de base,
  variables, types de données.
* [`01-Fonctions`](./01-Fonctions) — Création de fonctions, paramètres, valeurs
  par défaut, lambdas, récursion.

**Idées de TP :**

* [`02-Fichiers`](./02-Fichiers) — Lecture, écriture, suppression de fichiers et
  arborescences.
* [`03-Subprocess`](./03-Subprocess) — Exécution de commandes système, analyse
  des résultats.
* [`04-Logs`](./04-Logs) — Analyse et extraction d’erreurs dans des fichiers
  journaux simulés.
* [`05-APIs`](./05-APIs) — Appels d’API HTTP (GET, POST), authentification,
  parsing JSON.
* [`06-YAML-JSON`](./06-YAML-JSON) — Conversion entre formats, génération de
  fichiers de configuration.
* [`07-SSH`](./07-SSH) — Connexion à distance avec `paramiko`, exécution de
  commandes.
* [`08-Disque`](./08-Disque) — Surveillance de l’espace disque, génération
  d’alertes.
* [`09-Users-Expiration`](./09-Users-Expiration) — Vérification des comptes
  expirés ou inactifs.
* [`10-Certificats`](./10-Certificats) — Détection des certificats expirés dans
  un répertoire.
* [`11-Rapports`](./11-Rapports) — Génération de rapports HTML à partir
  d’informations système.
* [`12-Inventory-API`](./12-Inventory-API) — Création d’une API REST pour
  exposer l’état système avec FastAPI.
* [`13-Rotation-Logs`](./13-Rotation-Logs) — Gestion manuelle de la rotation des
  logs.
* [`14-Nettoyage-Temp`](./14-Nettoyage-Temp) — Suppression automatisée de
  fichiers temporaires obsolètes.
* [`15-Ping-Subnet`](./15-Ping-Subnet) — Scan IP d’un sous-réseau avec rapport
  de disponibilité.
* [`16-Backup-Automation`](./16-Backup-Automation) — Sauvegarde automatique avec
  noms dynamiques.
* [`17-Supervision-Services`](./17-Supervision-Services) — Vérification et
  redémarrage automatique de services critiques.

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
[https://blog.stephane-robert.info/docs/homelab/incus/](https://blog.stephane-robert.info/docs/homelab/incus/)

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

