
# Challenge — Liste de courses interactive

Bienvenue dans ce challenge Python !

---

## 🎯 Objectif

Créer un programme en ligne de commande qui permet à l'utilisateur de gérer une **liste de courses** simple.

---

## 📝 Consignes

Votre programme doit permettre :

* D'**ajouter** un article à la liste
* D'**afficher** tous les articles de la liste
* De **supprimer** un article par son numéro
* De **quitter** le programme

---

## ✅ Critères attendus

* Utilisation d'une **liste** pour stocker les articles
* Menu principal avec une boucle `while`
* Utilisation de `input()` pour la saisie utilisateur
* Affichage clair et numéroté des articles
* Gestion des cas où la liste est vide
* Code commenté et lisible

---

## 🔧 Fichier à créer

Créez un fichier `liste_courses.py` dans ce dossier :

```bash
cd challenge
touch liste_courses.py
```

---

## ▶️ Exemple d'exécution attendue

```bash
=== Liste de courses ===

1. Ajouter un article
2. Afficher la liste
3. Supprimer un article
4. Quitter

Votre choix : 1
Nom de l'article : Pommes
✅ Article ajouté !

Votre choix : 2

=== Articles ===
1. Pommes

Votre choix : 3
Numéro de l'article à supprimer : 1
✅ Article supprimé !

Votre choix : 4
👋 Au revoir !
```

---

## 💡 Conseils

* Utilisez une liste vide au départ : `courses = []`
* Pour afficher les articles, utilisez une boucle `for` avec `enumerate()`
* Pour supprimer, vérifiez que le numéro existe avant d'utiliser `pop()`
* Affichez un message si la liste est vide

---

## Validation automatique

Testez votre script avec différentes opérations :

```bash
python3 liste_courses.py
```

---

📚 Bon courage et amusez-vous avec la programmation Python ! 🥕
