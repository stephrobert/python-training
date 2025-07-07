# 00 - Introduction à Python

Bienvenue dans ce premier chapitre de la formation **Python pour administrateurs
systèmes**.

Ce TP vous guide dans la création de votre **premier script Python interactif**.
À chaque étape, vous modifierez le script et **l’exécuterez immédiatement** pour
observer son comportement.

---

## 🎯 Objectifs

* Comprendre la structure d’un script Python
* Lire des données utilisateur
* Manipuler des types (`str`, `int`)
* Afficher des messages dynamiques
* Utiliser un module standard (`datetime`)
* Exécuter un script depuis le terminal

---

## 📘 Préparation

Lisez au préalable : 🔗 [**Introduction à
Python**](https://blog.stephane-robert.info/docs/developper/programmation/python/)

Assurez-vous que Python 3 est installé :

```bash
python3 --version
```

Vous devriez voir une version >= 3.10.

---

## 🛠️ Étapes du TP

### Etape 1. Se placer dans le bon dossier

Dans votre terminal, placez-vous dans le dossier du TP :

```bash
cd formation-base/00-Intro-Python
```

---

### Etape 2. Créer le fichier `main.py`

Créez le fichier :

```bash
touch main.py
```

Ouvrez-le dans votre éditeur de code :

```bash
nano main.py
# ou
code main.py
```

---

### Etape 3. Ajouter un message de bienvenue

Ajoutez ce code :

```python
print("Bienvenue dans ce premier programme Python !")
```

💡 **Exécutez maintenant le script :**

```bash
python3 main.py
```

Vous devez voir :

```bash
Bienvenue dans ce premier programme Python !
```

---

### Etape 4. Lire le prénom de l’utilisateur

Ajoutez cette ligne :

```python
prenom = input("Quel est ton prénom ? ")
```

Et modifiez la ligne précédente pour inclure le prénom :

```python
print(f"Bienvenue {prenom} !")
```

💡 **Exécutez à nouveau le script** et entrez votre prénom lorsqu’il vous le
demande.

---

### Etape 5. Lire l’année de naissance

Ajoutez ceci :

```python
annee_naissance = int(input("En quelle année es-tu né ? "))
```

💡 **Relancez le script** et testez la saisie d’une année (ex : 1990).

---

### Etape 6. Calculer l’âge

Ajoutez les lignes suivantes pour calculer l’âge :

```python
import datetime

annee_actuelle = datetime.datetime.now().year
age = annee_actuelle - annee_naissance
```

💡 **Exécutez le script** et vérifiez que le programme ne plante pas après
saisie.

---

### Etape 7. Vérifier l’année saisie

Ajoutez un contrôle simple :

```python
if age < 0:
    print("Tu viens du futur ? 😄")
    exit(1)
```

💡 **Lancez le script et entrez une année future** (ex : 2090) pour tester.

---

### Etape 8. Afficher le résultat final

Terminez avec une ligne d’affichage :

```python
print(f"Bonjour {prenom}, tu as {age} ans.")
```

💡 **Exécutez le script complet** et vérifiez que tout fonctionne comme attendu.

---

### Etape 9. Ajouter un shebang (optionnel)

Ajoutez cette ligne tout en haut du fichier :

```python
#!/usr/bin/env python3
```

Puis rendez le script exécutable :

```bash
chmod +x main.py
```

💡 Vous pouvez maintenant lancer le script directement :

```bash
./main.py
```

Normalement, vous devriez avoir le fichier `main.py` qui ressemble à ceci :

```python
#!/usr/bin/env python3
import datetime

print("Bienvenue dans ce premier programme Python !")
prenom = input("Quel est ton prénom ? ")
print(f"Bienvenue {prenom} !")
annee_naissance = int(input("En quelle année es-tu né ? "))
annee_actuelle = datetime.datetime.now().year
age = annee_actuelle - annee_naissance
if age < 0:
    print("Tu viens du futur ? 😄")
    exit(1)
print(f"Bonjour {prenom}, tu as {age} ans.")
```

---

## ✅ Ce que vous avez appris

* Comment lire et convertir des entrées utilisateur
* Comment utiliser des variables et faire des calculs
* Comment afficher des messages personnalisés
* Comment utiliser un module standard (`datetime`)
* Comment structurer et exécuter un script Python

---

## 🏁 Challenge : jeu de devinette

Un exercice complémentaire est disponible dans le dossier
[`challenge`](./challenge/README.md).

Vous développerez un petit **jeu interactif** pour deviner un nombre mystère
avec :

* Une boucle `while`
* Des conditions `if`
* Un compteur d’essais

---

## 🧰 Suite du parcours

Vous pouvez maintenant passer au TP suivant : [`01-Fichiers`](../01-Fichiers),
où vous apprendrez à manipuler des fichiers et des répertoires avec Python.

---

📚 Bon apprentissage et bonne automatisation avec Python !
