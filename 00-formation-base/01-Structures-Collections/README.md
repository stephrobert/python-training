# 01 - Structures de contrôle et collections en Python

Bienvenue dans ce second chapitre de la formation **Python pour administrateurs
systèmes**.

Ce TP vous guide dans la découverte des **structures de contrôle et collections** abordées dans le guide :
conditions, boucles, listes, tuples et dictionnaires pour créer des programmes plus dynamiques.

---

## 🎯 Objectifs

* Maîtriser les structures conditionnelles (if, elif, else)
* Utiliser les boucles for et while efficacement
* Manipuler les listes (création, modification, parcours)
* Comprendre les tuples et leur immutabilité
* Gérer les dictionnaires (clés-valeurs)
* Contrôler le flux avec break et continue
* Combiner ces concepts dans des programmes complets

---

## 📘 Préparation

Lisez au préalable : 🔗 [**Structures de contrôle et collections en Python**](https://blog.stephane-robert.info/docs/developper/programmation/python/structures-collections/)

Assurez-vous d'avoir terminé le TP précédent et que Python 3 est installé :

```bash
python3 --version
```

Vous devriez voir une version >= 3.10.

---

## 🛠️ Étapes du TP

### Etape 1. Créer la structure du projet

Dans votre terminal, placez-vous dans le dossier du TP :

```bash
cd 00-formation-base/01-Structures-Collections
```

Créez le fichier principal :

```bash
touch structures_collections.py
```

Ouvrez-le dans votre éditeur de code :

```bash
nano structures_collections.py
# ou
code structures_collections.py
```

---

### Etape 2. Ajouter l'en-tête et les conditions

Commencez par ajouter l'en-tête et explorer les conditions :

```python
#!/usr/bin/env python3
# Auteur : [Votre nom]
# Date : 2025-01-XX
# Description : Apprentissage des structures de contrôle et collections

print("=== Structures de contrôle et collections ===")

# === STRUCTURES CONDITIONNELLES ===
print("\n1. Instructions conditionnelles")

# Test simple avec if
age = 20
if age >= 18:
    print(f"Age {age} : Vous êtes majeur")
else:
    print(f"Age {age} : Vous êtes mineur")

# Test avec elif pour les notes
note = 85
print(f"\nNote : {note}")
if note >= 90:
    print("Mention : Excellent")
elif note >= 80:
    print("Mention : Très bien")
elif note >= 70:
    print("Mention : Bien")
elif note >= 60:
    print("Mention : Passable")
else:
    print("Mention : Insuffisant")
```

💡 **Exécutez et testez les conditions :**

```bash
python3 structures_collections.py
```

---

### Etape 3. Ajouter les conditions complexes

Ajoutez des conditions avec opérateurs logiques :

```python
# === CONDITIONS COMPLEXES ===
print("\n2. Conditions complexes")

age = 25
permis = True

print(f"Age: {age}, Permis: {permis}")
if age >= 18 and permis:
    print("✅ Vous pouvez conduire")
elif age >= 18 and not permis:
    print("⚠️ Vous devez passer le permis")
else:
    print("❌ Vous êtes trop jeune")

# Test avec plusieurs conditions
temperature = 22
saison = "été"

print(f"\nTempérature: {temperature}°C, Saison: {saison}")
if temperature > 25 and saison == "été":
    print("🌞 Parfait pour la plage !")
elif temperature > 15 or saison == "printemps":
    print("🌤️ Beau temps pour une promenade")
else:
    print("🏠 Mieux vaut rester à l'intérieur")
```

💡 **Observez comment les opérateurs and, or et not fonctionnent.**

---

### Etape 4. Découvrir les boucles for

Ajoutez les boucles for avec range() :

```python
# === BOUCLES FOR ===
print("\n3. Boucles for")

# Boucle simple avec range
print("Nombres de 0 à 4 :")
for i in range(5):
    print(f"  {i}")

# Boucle avec range personnalisé
print("\nNombres de 1 à 5 :")
for i in range(1, 6):
    print(f"  {i}")

# Boucle avec pas
print("\nNombres pairs de 0 à 10 :")
for i in range(0, 11, 2):
    print(f"  {i}")

# Boucle sur une chaîne
mot = "Python"
print(f"\nLettres de '{mot}' :")
for lettre in mot:
    print(f"  {lettre}")
```

💡 **Testez les différentes utilisations de range().**

---

### Etape 5. Explorer les boucles while

Ajoutez les boucles while et les instructions de contrôle :

```python
# === BOUCLES WHILE ===
print("\n4. Boucles while")

# Boucle while simple
print("Compteur avec while :")
compteur = 0
while compteur < 5:
    print(f"  Compteur: {compteur}")
    compteur += 1

# === CONTRÔLE DES BOUCLES ===
print("\n5. Contrôle des boucles (break, continue)")

# Utilisation de break
print("Recherche avec break (s'arrête à 5) :")
for i in range(10):
    if i == 5:
        print(f"  Trouvé {i}, on s'arrête !")
        break
    print(f"  {i}")

# Utilisation de continue
print("\nAffichage des nombres impairs avec continue :")
for i in range(10):
    if i % 2 == 0:  # Si pair, on passe au suivant
        continue
    print(f"  {i}")
```

💡 **Observez la différence entre break et continue.**

---

### Etape 6. Travailler avec les listes

Ajoutez la manipulation des listes :

```python
# === LISTES ===
print("\n6. Manipulation des listes")

# Création de listes
fruits = ["pomme", "banane", "orange"]
nombres = [1, 2, 3, 4, 5]
mixte = ["hello", 42, True, 3.14]

print(f"Fruits: {fruits}")
print(f"Nombres: {nombres}")
print(f"Mixte: {mixte}")

# Accès aux éléments
print(f"\nPremier fruit: {fruits[0]}")
print(f"Dernier fruit: {fruits[-1]}")
print(f"Deuxième nombre: {nombres[1]}")

# Modification des listes
fruits.append("kiwi")
print(f"Après ajout: {fruits}")

fruits[1] = "mangue"
print(f"Après modification: {fruits}")

fruits.remove("orange")
print(f"Après suppression: {fruits}")

# Parcours de liste
print("\nParcours des fruits :")
for i, fruit in enumerate(fruits):
    print(f"  {i}: {fruit}")
```

💡 **Expérimentez avec les méthodes des listes.**

---

### Etape 7. Explorer les tuples

Ajoutez les tuples et le déballage :

```python
# === TUPLES ===
print("\n7. Manipulation des tuples")

# Création de tuples
coordonnees = (10, 20)
couleurs = ("rouge", "vert", "bleu")
singleton = (42,)  # Attention à la virgule !

print(f"Coordonnées: {coordonnees}")
print(f"Couleurs: {couleurs}")
print(f"Singleton: {singleton}")

# Accès aux éléments
print(f"X: {coordonnees[0]}, Y: {coordonnees[1]}")

# Déballage de tuples
x, y = coordonnees
print(f"Après déballage - X: {x}, Y: {y}")

# Échange de variables
a = 5
b = 10
print(f"Avant échange - a: {a}, b: {b}")
a, b = b, a
print(f"Après échange - a: {a}, b: {b}")

# Parcours de tuple
print("Couleurs disponibles :")
for i, couleur in enumerate(couleurs):
    print(f"  {i}: {couleur}")
```

💡 **Notez l'immutabilité des tuples.**

---

### Etape 8. Gérer les dictionnaires

Ajoutez la manipulation des dictionnaires :

```python
# === DICTIONNAIRES ===
print("\n8. Manipulation des dictionnaires")

# Création de dictionnaires
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "age": 30,
    "ville": "Paris"
}

print(f"Personne: {personne}")

# Accès aux valeurs
print(f"Nom: {personne['nom']}")
print(f"Age: {personne.get('age')}")
print(f"Email: {personne.get('email', 'Non défini')}")

# Modification du dictionnaire
personne["age"] = 31
personne["email"] = "jean.dupont@email.com"
print(f"Après modification: {personne}")

# Parcours du dictionnaire
print("\nInformations complètes :")
for cle, valeur in personne.items():
    print(f"  {cle}: {valeur}")

# Clés et valeurs
print(f"\nClés: {list(personne.keys())}")
print(f"Valeurs: {list(personne.values())}")
```

💡 **Testez les différentes méthodes des dictionnaires.**

---

### Etape 9. Combiner les concepts

Créez un exemple qui combine tous les concepts :

```python
# === EXEMPLE COMPLET ===
print("\n9. Exemple complet : Gestion d'étudiants")

# Liste d'étudiants (dictionnaires dans une liste)
etudiants = [
    {"nom": "Alice", "notes": [15, 18, 16]},
    {"nom": "Bob", "notes": [12, 14, 13]},
    {"nom": "Charlie", "notes": [18, 19, 17]}
]

print("Analyse des résultats :")
for etudiant in etudiants:
    nom = etudiant["nom"]
    notes = etudiant["notes"]

    # Calcul de la moyenne
    moyenne = sum(notes) / len(notes)

    # Détermination de la mention
    if moyenne >= 16:
        mention = "Très bien"
    elif moyenne >= 14:
        mention = "Bien"
    elif moyenne >= 12:
        mention = "Assez bien"
    elif moyenne >= 10:
        mention = "Passable"
    else:
        mention = "Insuffisant"

    print(f"  {nom}: {notes} → Moyenne: {moyenne:.1f} ({mention})")
```

💡 **Observez comment tous les concepts se combinent.**

---

### Etape 10. Script complet final

Rendez le script exécutable et testez :

```bash
chmod +x structures_collections.py
./structures_collections.py
```

Votre script complet devrait ressembler à l'assemblage de tous les codes précédents.

---

## ✅ Ce que vous avez appris

* **Structures conditionnelles** : if/elif/else pour la prise de décision
* **Conditions complexes** : Opérateurs and, or, not
* **Boucles for** : Itération avec range() et sur des séquences
* **Boucles while** : Répétition basée sur une condition
* **Contrôle de flux** : break et continue pour maîtriser les boucles
* **Listes** : Collections modifiables et leurs méthodes
* **Tuples** : Collections immutables et déballage
* **Dictionnaires** : Structures clé-valeur et leurs méthodes
* **Combinaison** : Utilisation conjointe de tous ces concepts

---

## 🏁 Challenge : Menu interactif

Un exercice complémentaire est disponible dans le dossier [`challenge`](./challenge/README.md).

Vous développerez un **menu interactif** qui utilise tous les concepts vus :

* Boucle principale avec `while`
* Menu de choix avec `if/elif/else`
* Gestion d'une liste de tâches
* Parcours et modification de collections
* Gestion des erreurs de saisie

---

## 🧰 Suite du parcours

Vous pouvez maintenant passer au TP suivant : [**Fonctions en Python**](),
où vous apprendrez à organiser votre code en fonctions réutilisables.

---

📚 Bravo ! Vous maîtrisez maintenant les structures de contrôle et collections Python ! 🎉
