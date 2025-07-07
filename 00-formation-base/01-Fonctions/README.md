# 01 - Fonctions Python 🐍

Bienvenue dans ce deuxième chapitre de la formation **Python pour
administrateurs systèmes**.

Ce TP te guide **pas à pas** pour maîtriser les fonctions Python : de la
définition la plus simple jusqu’à la récursion, en passant par les paramètres
avancés et les lambdas.

---

## 🎯 Objectifs pédagogiques

* Définir et appeler une fonction
* Manipuler les paramètres (positionnels, nommés, valeurs par défaut)
* Retourner des valeurs et documenter son code
* Utiliser `*args` et `**kwargs`
* Créer des lambdas et des fonctions imbriquées (closures)
* Ajouter des annotations de type et des docstrings claires
* Comprendre la récursivité
* Valider ses compétences grâce à un challenge automatisé

---

## 📘 Préparation

1. Lis la doc : 🔗 [**Fonctions
   en Python**](https://blog.stephane-robert.info/docs/developper/programmation/python/fonctions/)

---

## 🗂️ Créer l’arborescence du TP

Place-toi dans le dossier du TP :

```bash
cd 00-formation-base/02-Fonctions
```

Tu travailles désormais dans ce dossier.

---

## 🛠️ Étapes pas‑à‑pas

### Étape 1 – Créer `salutations.py` et afficher un message

1. **Crée** le fichier :

   ```bash
   touch salutations.py
   ```

2. **Ouvre**‑le dans ton éditeur préféré (VS Code, nano, vim…) :

   ```bash
   code salutations.py
   ```

3. **Écris** le code suivant :

   ```python
   #!/usr/bin/env python3

   def saluer():
       """Affiche un message de bienvenue."""
       print("Bonjour ! Bienvenue dans les fonctions.")

   if __name__ == "__main__":
       saluer()
   ```

   Ici `if __name__ == "__main__":` permet d’exécuter la fonction `saluer()`
   uniquement si le script est lancé directement, pas s’il est importé.

   Rends le script exécutable :

   ```bash
   chmod +x salutations.py
   ```

4. **Exécute** :

   ```bash
   ./salutations.py
   ```

   Tu dois voir : `Bonjour ! Bienvenue dans les fonctions.`

---

### Étape 2 – Ajouter des paramètres et une valeur par défaut

1. **Modifie la fonction** `saluer()` dans `salutations.py` avec ce contenu :

   ```python
   #!/usr/bin/env python3

   def saluer_personne(nom: str, titre: str = "cher visiteur") -> None:
       """Salue la personne avec un titre optionnel."""
       print(f"Bonjour, {titre} {nom} !")

   if __name__ == "__main__":
       saluer_personne("Alice")  # Appel sans titre
       saluer_personne("Bob", titre="Dr")  # Appel avec titre
   ```

2. **Teste** depuis le terminal :

   ```bash
   ./salutations.py
   ```

---

### Étape 3 – Valeur de retour et annotations de type

1. **Crée** le fichier :

   ```bash
   touch calculs.py
   ```

2. **Ajoute** une fonction d’addition :

   ```python
    #!/usr/bin/env python3

   def additionner(a: float, b: float) -> float:
       """Retourne la somme de deux nombres."""
       return a + b

   if __name__ == "__main__":
       print(additionner(2, 3))
   ```

   Rends le script exécutable :

   ```bash
   chmod +x calculs.py
   ```

3. **Exécute** :

   ```bash
   ./calculs.py
   ```

   Tu dois voir : `5.0`

---

### Étape 4 – `*args` et `**kwargs`

Dans `calculs.py`, ajopute les fonctions suivantes :

```python
def somme(*nombres: float) -> float:
    """Additionne un nombre arbitraire d’arguments."""
    return sum(nombres)

def afficher_infos(**infos) -> None:
    """Affiche les paires clé / valeur fournies."""
    for cle, valeur in infos.items():
        print(f"{cle} : {valeur}")


if __name__ == "__main__":
    print(additionner(2, 3))
    print(somme(1, 2, 3, 4))
    afficher_infos(nom="Alice", age=30, ville="Paris")

```

Teste :

```bash
./calculs.py
```

---

### Étape 5 – Les lambdas

1. **Crée** le fichier :

   ```bash
   touch lambdas.py
   ```

2. **Ajoute** :

   ```python
   #!/usr/bin/env python3
   multiplication = lambda x, y: x * y

   if __name__ == "__main__":
       print(multiplication(3, 4))          # 12
   ```

3. **Teste le** :

   ```bash
   python3 lambdas.py
   ```

---

### Étape 6 – Fonctions imbriquées (closures)

1. **Crée** le fichier :

   ```bash
   touch closures.py
   ```

2. **Ajoute** :

   ```python
   #!/usr/bin/env python3

   def create_multiplier(facteur: float) -> callable:
       """Retourne une fonction qui multiplie par un facteur donné."""
       def multiplier(x: float) -> float:
           return x * facteur
       return multiplier

   if __name__ == "__main__":
       double = create_multiplier(2)
       print(double(5))  # 10
   ```

3. **Teste le** :

   ```bash
   python3 closures.py
   ```

---

### Étape 7 – Récursivité

1. **Réouvre** `calculs.py` et ajoute :

   ```python

   def factorielle(n: int) -> int:
       """Calcule n! récursivement."""
       if n == 0:
           return 1
       return n * factorielle(n - 1)

    if __name__ == "__main__":
        print(additionner(2, 3))
        print(somme(1, 2, 3, 4))
        afficher_infos(nom="Alice", age=30, ville="Paris")
        print(factorielle(5))  # 120
   ```

   Ici, `factorielle(0)` retourne 1, et pour `n > 0`, elle appelle
   récursivement `factorielle(n - 1)`.

2. **Teste** :

   ```bash
   ./calculs.py
   ```

---

## ✅ Récapitulatif

Tu as appris à :

* Définir et appeler des fonctions
* Utiliser des paramètres positionnels et nommés
* Gérer les valeurs par défaut
* Retourner des valeurs et documenter avec des annotations de type
* Utiliser `*args` et `**kwargs`
* Créer des fonctions anonymes (lambdas) et imbriquées (closures)
* Comprendre la récursivité

---

## 🏁 Challenge final – Calcul du prix d’un repas

Vous êtes prêt pour le [challenge final](challenge/README.md) ! 🎉

---

## 🧰 Suite du parcours

Passe au TP suivant [`03-Collections`](../03-Collections) pour explorer listes,
tuples et dictionnaires.

---

📚 Bon apprentissage et bonne automatisation ! 🚀
