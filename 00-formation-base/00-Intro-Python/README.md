# 00 - Introduction à Python - Les Fondamentaux

Bienvenue dans ce premier chapitre de la formation **Python pour administrateurs
systèmes**.

Ce TP vous guide dans la découverte des **fondamentaux de Python** abordés dans le guide :
variables, types de données, opérations de base et bonnes pratiques pour l'écriture de scripts.

---

## 🎯 Objectifs

* Maîtriser les variables et types de données de base
* Effectuer des opérations mathématiques et logiques
* Manipuler des chaînes de caractères
* Utiliser les commentaires pour documenter le code
* Appliquer les bonnes pratiques (shebang, structure de script)
* Exécuter un script depuis le terminal

---

## 📘 Préparation

Lisez au préalable : 🔗 [**Débuter avec Python - Les Fondamentaux**](https://www.stephane-robert.info/docs/developper/programmation/python/)

Assurez-vous que Python 3 est installé :

```bash
python3 --version
```

Vous devriez voir une version >= 3.10.

---

## 🛠️ Étapes du TP

### Etape 1. Créer la structure du projet

Dans votre terminal, placez-vous dans le dossier du TP :

```bash
cd 00-formation-base/00-Intro-Python
```

Créez le fichier principal :

```bash
touch fondamentaux.py
```

Ouvrez-le dans votre éditeur de code :

```bash
nano fondamentaux.py
# ou
code fondamentaux.py
```

---

### Etape 2. Ajouter l'en-tête du script avec bonnes pratiques

Commencez par ajouter le shebang et l'en-tête selon les bonnes pratiques :

```python
#!/usr/bin/env python3
# Auteur : [Votre nom]
# Date : 2025-01-XX
# Description : Script d'apprentissage des fondamentaux Python

# Bienvenue dans l'apprentissage des fondamentaux Python
print("=== Fondamentaux de Python ===")
```

💡 **Exécutez le script pour vérifier :**

```bash
python3 fondamentaux.py
```

---

### Etape 3. Explorer les variables et types de données

Ajoutez le code suivant pour expérimenter avec les types de base :

```python
# === VARIABLES ET TYPES DE DONNÉES ===
print("\n1. Variables et types de données")

# Déclaration de variables de différents types
nom = "Alice"  # Chaîne de caractères (str)
age = 30       # Entier (int)
taille = 1.75  # Flottant (float)
est_majeur = True  # Booléen (bool)

# Affichage des variables avec leur type
print(f"Nom: {nom} (type: {type(nom).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Taille: {taille} (type: {type(taille).__name__})")
print(f"Est majeur: {est_majeur} (type: {type(est_majeur).__name__})")
```

💡 **Exécutez et observez les différents types affichés.**

---

### Etape 4. Pratiquer les opérations mathématiques

Ajoutez des exemples d'opérations mathématiques :

```python
# === OPÉRATIONS MATHÉMATIQUES ===
print("\n2. Opérations mathématiques")

a = 10
b = 3

# Les opérations de base
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
modulo = a % b

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {addition}")
print(f"Soustraction: {a} - {b} = {soustraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division:.2f}")
print(f"Modulo: {a} % {b} = {modulo}")

# Priorités des opérations
resultat1 = 5 + 2 * 3
resultat2 = (5 + 2) * 3
print(f"\nPriorités: 5 + 2 * 3 = {resultat1}")
print(f"Avec parenthèses: (5 + 2) * 3 = {resultat2}")
```

💡 **Exécutez et vérifiez les calculs.**

---

### Etape 5. Manipulation de chaînes de caractères

Ajoutez les opérations sur les chaînes :

```python
# === MANIPULATION DE CHAÎNES ===
print("\n3. Manipulation de chaînes de caractères")

chaine1 = "Bonjour"
chaine2 = "Python"

# Opérations sur les chaînes
concatenation = chaine1 + ", " + chaine2
longueur = len(chaine1)
premier_caractere = chaine1[0]
sous_chaine = chaine2[0:3]

print(f"Chaîne 1: '{chaine1}'")
print(f"Chaîne 2: '{chaine2}'")
print(f"Concaténation: '{concatenation}'")
print(f"Longueur de '{chaine1}': {longueur}")
print(f"Premier caractère de '{chaine1}': '{premier_caractere}'")
print(f"Sous-chaîne '{chaine2}'[0:3]: '{sous_chaine}'")
```

💡 **Testez les manipulations de chaînes.**

---

### Etape 6. Opérations logiques

Ajoutez les opérateurs logiques :

```python
# === OPÉRATIONS LOGIQUES ===
print("\n4. Opérations logiques")

vrai = True
faux = False

# Opérateurs logiques
resultat_et = vrai and faux
resultat_ou = vrai or faux
resultat_non = not vrai

print(f"vrai = {vrai}, faux = {faux}")
print(f"vrai AND faux = {resultat_et}")
print(f"vrai OR faux = {resultat_ou}")
print(f"NOT vrai = {resultat_non}")

# Comparaisons
x = 10
y = 20
print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")
```

💡 **Observez les résultats des opérations logiques.**

---

### Etape 7. Conversions de types

Ajoutez les conversions entre types :

```python
# === CONVERSIONS DE TYPES ===
print("\n5. Conversions entre types")

# Conversion de chaîne vers nombre
nombre_texte = "123"
nombre_entier = int(nombre_texte)
nombre_flottant = float(nombre_texte)

print(f"Chaîne: '{nombre_texte}' -> Entier: {nombre_entier}")
print(f"Chaîne: '{nombre_texte}' -> Flottant: {nombre_flottant}")

# Conversion de nombre vers chaîne
age_num = 30
age_texte = str(age_num)
print(f"Entier: {age_num} -> Chaîne: '{age_texte}'")

# Conversion booléenne
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")
```

💡 **Testez les différentes conversions.**

---

### Etape 8. Rendre le script exécutable

Rendez votre script exécutable directement :

```bash
chmod +x fondamentaux.py
```

💡 **Testez l'exécution directe :**

```bash
./fondamentaux.py
```

---

### Etape 9. Script complet final

Votre script `fondamentaux.py` devrait ressembler à ceci :

```python
#!/usr/bin/env python3
# Auteur : [Votre nom]
# Date : 2025-01-XX
# Description : Script d'apprentissage des fondamentaux Python

# Bienvenue dans l'apprentissage des fondamentaux Python
print("=== Fondamentaux de Python ===")

# === VARIABLES ET TYPES DE DONNÉES ===
print("\n1. Variables et types de données")

# Déclaration de variables de différents types
nom = "Alice"  # Chaîne de caractères (str)
age = 30       # Entier (int)
taille = 1.75  # Flottant (float)
est_majeur = True  # Booléen (bool)

# Affichage des variables avec leur type
print(f"Nom: {nom} (type: {type(nom).__name__})")
print(f"Age: {age} (type: {type(age).__name__})")
print(f"Taille: {taille} (type: {type(taille).__name__})")
print(f"Est majeur: {est_majeur} (type: {type(est_majeur).__name__})")

# === OPÉRATIONS MATHÉMATIQUES ===
print("\n2. Opérations mathématiques")

a = 10
b = 3

# Les opérations de base
addition = a + b
soustraction = a - b
multiplication = a * b
division = a / b
modulo = a % b

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {addition}")
print(f"Soustraction: {a} - {b} = {soustraction}")
print(f"Multiplication: {a} * {b} = {multiplication}")
print(f"Division: {a} / {b} = {division:.2f}")
print(f"Modulo: {a} % {b} = {modulo}")

# Priorités des opérations
resultat1 = 5 + 2 * 3
resultat2 = (5 + 2) * 3
print(f"\nPriorités: 5 + 2 * 3 = {resultat1}")
print(f"Avec parenthèses: (5 + 2) * 3 = {resultat2}")

# === MANIPULATION DE CHAÎNES ===
print("\n3. Manipulation de chaînes de caractères")

chaine1 = "Bonjour"
chaine2 = "Python"

# Opérations sur les chaînes
concatenation = chaine1 + ", " + chaine2
longueur = len(chaine1)
premier_caractere = chaine1[0]
sous_chaine = chaine2[0:3]

print(f"Chaîne 1: '{chaine1}'")
print(f"Chaîne 2: '{chaine2}'")
print(f"Concaténation: '{concatenation}'")
print(f"Longueur de '{chaine1}': {longueur}")
print(f"Premier caractère de '{chaine1}': '{premier_caractere}'")
print(f"Sous-chaîne '{chaine2}'[0:3]: '{sous_chaine}'")

# === OPÉRATIONS LOGIQUES ===
print("\n4. Opérations logiques")

vrai = True
faux = False

# Opérateurs logiques
resultat_et = vrai and faux
resultat_ou = vrai or faux
resultat_non = not vrai

print(f"vrai = {vrai}, faux = {faux}")
print(f"vrai AND faux = {resultat_et}")
print(f"vrai OR faux = {resultat_ou}")
print(f"NOT vrai = {resultat_non}")

# Comparaisons
x = 10
y = 20
print(f"\nx = {x}, y = {y}")
print(f"x == y: {x == y}")
print(f"x < y: {x < y}")
print(f"x >= y: {x >= y}")

# === CONVERSIONS DE TYPES ===
print("\n5. Conversions entre types")

# Conversion de chaîne vers nombre
nombre_texte = "123"
nombre_entier = int(nombre_texte)
nombre_flottant = float(nombre_texte)

print(f"Chaîne: '{nombre_texte}' -> Entier: {nombre_entier}")
print(f"Chaîne: '{nombre_texte}' -> Flottant: {nombre_flottant}")

# Conversion de nombre vers chaîne
age_num = 30
age_texte = str(age_num)
print(f"Entier: {age_num} -> Chaîne: '{age_texte}'")

# Conversion booléenne
print(f"bool(1): {bool(1)}")
print(f"bool(0): {bool(0)}")
print(f"bool(''): {bool('')}")
print(f"bool('Hello'): {bool('Hello')}")

print("\n=== Fin du script ===")
```

---

## ✅ Ce que vous avez appris

* **Variables et types de données** : Création et manipulation des types de base (str, int, float, bool)
* **Opérations mathématiques** : Addition, soustraction, multiplication, division, modulo et priorités
* **Manipulation de chaînes** : Concaténation, longueur, indexation et découpage
* **Opérations logiques** : Utilisation des opérateurs and, or, not et comparaisons
* **Conversions de types** : Transformation entre différents types de données
* **Bonnes pratiques** : Shebang, commentaires et structure de script
* **Exécution de scripts** : Lancement depuis le terminal

---

## 🏁 Challenge : calculatrice simple

Un exercice complémentaire est disponible dans le dossier [`challenge`](./challenge/README.md).

Vous développerez une **jeu de devinette** qui utilise tous les concepts vus :

* Saisie utilisateur avec `input()`
* Boucles et conditions
* Conversion de types
* Affichage dynamique
* Affichage formaté des résultats

---

## 🧰 Suite du parcours

Vous pouvez maintenant passer au tp suivant : [**Structures de contrôle et collections**](),
où vous apprendrez les conditions, boucles et structures de données.

---

📚 Bon apprentissage et bonne découverte des fondamentaux Python !
