# Challenge — Jeu de devinette

Bienvenue dans ce premier **challenge Python** de la formation !

---

## 🎯 Objectif

Vous allez créer un petit jeu en ligne de commande où l’utilisateur doit
**deviner un nombre mystère**. Ce sera l’occasion de mettre en pratique tout ce
que vous avez appris dans le TP `00-Intro-Python` :

* Lecture d’entrées utilisateur
* Boucles et conditions
* Conversion de types
* Affichage dynamique
* Modules Python (`random`)

---

## 📝 Consignes

* Choisissez un **nombre mystère** entre 1 et 100.
* Demandez à l’utilisateur de **saisir un nombre**.
* Affichez s’il est **trop petit**, **trop grand**, ou **juste**.
* Comptez le **nombre d’essais** nécessaires.
* Affichez un message de victoire quand l’utilisateur a trouvé.

---

## ✅ Critères attendus

* Le script fonctionne sans erreur.
* La logique de boucle est bien maîtrisée (`while`, `break` ou booléen).
* La comparaison des entiers est correcte.
* L’utilisateur est guidé par des messages clairs.
* Le nombre d’essais est compté et affiché à la fin.
* Bonus : gestion des entrées invalides (ex : lettres au lieu de chiffres).

---

## 🔧 Fichier à créer

Créez un fichier `devinette.py` dans ce dossier :

```bash
cd challenge
touch devinette.py
```

---

## ▶️ Exemple d’exécution

```bash
Bienvenue au jeu de devinette !
Devine le nombre mystère (entre 1 et 100) :

> 50
C'est plus petit.

> 25
C'est plus grand.

> 32
Bravo ! Tu as trouvé en 3 essais 🎉
```

---

## 🧪 Test manuel

Vous pouvez relancer le script plusieurs fois pour tester différentes valeurs :

```bash
python3 devinette.py
```

## Validation automatique

Pour valider votre solution, vous pouvez utiliser les tests fournis dans le dossier `tests/` :

```bash
pytest -v
```

Vous devriez voir un test passer avec succès :

```bash
=== test session starts ===
platform linux -- Python 3.10.12, pytest-8.3.5, pluggy-1.5.0
rootdir: /home/outscale/Projets/python-training/00-Intro-Python/challenge
plugins: testinfra-10.2.2
collected 2 items

tests/test_devinette.py ..     [100%]

=== 2 passed in 0.01s ===
```

---

📚 Amusez-vous bien et bravo si vous trouvez du premier coup 😉
