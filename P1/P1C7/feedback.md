# P1C7 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Dictionnaires - Manipulation de dictionnaires en Python

Découvrir les dictionnaires : création, ajout, accès, modification, suppression, clés.

**Objectifs pédagogiques :**
- Créer un dictionnaire (paires clé-valeur)
- Accéder à une valeur par sa clé
- Ajouter une nouvelle paire clé-valeur
- Modifier une valeur existante
- Supprimer une paire avec `del`
- Afficher les clés, valeurs et items
- Utiliser la méthode `get()` pour un accès sécurisé

---

## 📝 Énoncé actuel

```python
fruits = {"pomme":"verte", "banane":"jaune", "orange":"orange"}

print(fruits.items())

fruits["kiwi"] = "vert"

print(fruits.items())

banana_color = fruits.get("banane")

print(banana_color)

fruits["pomme"] = "vert"

print(fruits.items())

del fruits["banane"]

print(fruits.items())
print(fruits.keys())
```

**Ce qui est demandé :**
1. Créer un dictionnaire fruit → couleur
2. Afficher les items (paires clé-valeur)
3. Ajouter "kiwi": "vert"
4. Récupérer la couleur de "banane" avec `get()`
5. Modifier la couleur de "pomme" en "vert"
6. Supprimer "banane" avec `del`
7. Afficher les items et les clés restantes

---

## ✅ Analyse de la solution de base

### Points positifs
- ✅ Toutes les opérations de base sont présentes
- ✅ Utilisation correcte de `get()` pour l'accès sécurisé
- ✅ Ordre logique des opérations
- ✅ Affichage des différents états du dictionnaire

### Points à améliorer

| Aspect | Problème | Solution |
|--------|----------|----------|
| Affichage brut | `print(fruits.items())` peu lisible | Formater l'affichage des items |
| `get()` vs `[]` | Ne montre pas la différence | Expliquer `get()` avec valeur par défaut |
| Suppression | `del` peut échouer si clé absente | Vérifier avec `in` ou utiliser `pop()` |
| Pas de commentaires | Non documenté | Ajouter des commentaires étape par étape |
| Pas de docstring | Non documenté | Ajouter une docstring |
| Pas de `values()` | Ne montre pas toutes les vues | Démontrer `keys()`, `values()`, `items()` |
| Pas de structure | Code linéaire | Encapsuler dans `main()` |

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Manipulation de dictionnaires en Python.

Ce programme démontre les opérations de base sur les dictionnaires :
création, ajout, accès, modification, suppression et vues (keys, values, items).
"""


def afficher_dictionnaire(fruits: dict, message: str) -> None:
    """
    Affiche un dictionnaire de manière formatée.
    
    Args:
        fruits: Le dictionnaire à afficher
        message: Message à afficher avant le dictionnaire
    """
    print(f"{message}")
    print(f"  Nombre d'éléments : {len(fruits)}")
    print("  Contenu :")
    for fruit, couleur in fruits.items():
        print(f"    - {fruit:10} -> {couleur}")
    print()


def main():
    """Fonction principale du programme."""
    print("=" * 50)
    print("MANIPULATION DE DICTIONNAIRES - DÉMONSTRATION")
    print("=" * 50)
    print()
    
    # ============================================================
    # ÉTAPE 1 : CRÉATION DU DICTIONNAIRE
    # ============================================================
    # Un dictionnaire stocke des paires clé-valeur
    # Syntaxe : {clé1: valeur1, clé2: valeur2, ...}
    # Les clés doivent être IMMUABLES (str, int, tuple)
    fruits = {
        "pomme": "verte",
        "banane": "jaune",
        "orange": "orange"
    }
    afficher_dictionnaire(fruits, "1. Création du dictionnaire initial :")
    
    # ============================================================
    # ÉTAPE 2 : AJOUT D'UNE NOUVELLE PAIRE CLÉ-VALEUR
    # ============================================================
    # fruits["kiwi"] = "vert" ajoute ou modifie une entrée
    fruits["kiwi"] = "vert"
    afficher_dictionnaire(fruits, "2. Après ajout de 'kiwi': 'vert' :")
    
    # ============================================================
    # ÉTAPE 3 : ACCÈS À UNE VALEUR (plusieurs méthodes)
    # ============================================================
    print("3. Accès à la couleur de 'banane' :")
    
    # Méthode 1 : avec [] (lève KeyError si la clé n'existe pas)
    try:
        couleur_banane = fruits["banane"]
        print(f"   fruits['banane'] = '{couleur_banane}'")
    except KeyError:
        print("   Clé 'banane' non trouvée !")
    
    # Méthode 2 : avec get() (retourne None si la clé n'existe pas)
    couleur_banane = fruits.get("banane")
    print(f"   fruits.get('banane') = '{couleur_banane}'")
    
    # Méthode 3 : avec get() et valeur par défaut
    couleur_mangue = fruits.get("mangue", "couleur inconnue")
    print(f"   fruits.get('mangue', 'couleur inconnue') = '{couleur_mangue}'")
    print()
    
    # ============================================================
    # ÉTAPE 4 : MODIFICATION D'UNE VALEUR EXISTANTE
    # ============================================================
    # Même syntaxe que l'ajout : si la clé existe, la valeur est modifiée
    ancienne_couleur = fruits["pomme"]
    fruits["pomme"] = "rouge"  # La pomme devient rouge
    print(f"4. Modification de 'pomme' : '{ancienne_couleur}' -> '{fruits['pomme']}'")
    afficher_dictionnaire(fruits, "   Résultat :")
    
    # ============================================================
    # ÉTAPE 5 : SUPPRESSION D'UNE PAIRE (plusieurs méthodes)
    # ============================================================
    print("5. Suppression de 'banane' :")
    
    # Méthode 1 : del (lève KeyError si la clé n'existe pas)
    cle_a_supprimer = "banane"
    if cle_a_supprimer in fruits:
        del fruits[cle_a_supprimer]
        print(f"   del fruits['{cle_a_supprimer}'] effectué")
    else:
        print(f"   '{cle_a_supprimer}' n'existe pas dans le dictionnaire")
    
    # Méthode 2 : pop() (retourne la valeur supprimée, lève KeyError si absente)
    # valeur = fruits.pop("banane", None)  # None si la clé n'existe pas
    
    # Méthode 3 : popitem() (supprime et retourne la DERNIÈRE paire insérée)
    # Note : depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion
    
    afficher_dictionnaire(fruits, "   Après suppression :")
    
    # ============================================================
    # ÉTAPE 6 : LES TROIS VUES D'UN DICTIONNAIRE
    # ============================================================
    print("6. Les trois vues d'un dictionnaire :")
    print(f"   keys()   : {list(fruits.keys())}")
    print(f"   values() : {list(fruits.values())}")
    print(f"   items()  : {list(fruits.items())}")
    print()
    
    # ============================================================
    # RÉSULTAT FINAL
    # ============================================================
    afficher_dictionnaire(fruits, "RÉSULTAT FINAL :")
    
    # ============================================================
    # MÉTHODES UTILES SUPPLÉMENTAIRES
    # ============================================================
    print("=" * 50)
    print("AUTRES MÉTHODES UTILES")
    print("=" * 50)
    
    # in : vérifie si une clé existe
    print(f"'kiwi' in fruits : {'kiwi' in fruits}")
    print(f"'mangue' in fruits : {'mangue' in fruits}")
    
    # update() : fusionne deux dictionnaires
    nouveaux_fruits = {"mangue": "orange", "pasteque": "rouge"}
    fruits.update(nouveaux_fruits)
    print(f"Après update() : {len(fruits)} fruits")
    
    # setdefault() : ajoute une clé si elle n'existe pas
    fruits.setdefault("cerise", "rouge")
    print(f"setdefault('cerise', 'rouge') : {fruits.get('cerise')}")
    
    # clear() : vide le dictionnaire
    # fruits.clear()  # Attention, supprime tout !
    
    # copy() : crée une copie superficielle
    fruits_copy = fruits.copy()
    print(f"Copie créée : {len(fruits_copy)} fruits")
    
    # ============================================================
    # DICTIONNAIRE AVEC DIFFÉRENTS TYPES DE CLÉS
    # ============================================================
    print()
    print("=" * 50)
    print("CLÉS DE DIFFÉRENTS TYPES")
    print("=" * 50)
    
    # Les clés peuvent être str, int, tuple (mais PAS list ou dict !)
    personne = {
        "nom": "Dupont",
        "prenom": "Jean",
        42: "age",           # int comme clé
        ("ville", "code"): ("Paris", 75001)  # tuple comme clé
    }
    print(f"Dictionnaire mixte : {personne}")


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Fonction d'affichage formatée
```python
# ❌ Affichage brut peu lisible
print(fruits.items())  # dict_items([('pomme', 'verte'), ...])

# ✅ Affichage formaté et clair
def afficher_dictionnaire(fruits: dict, message: str) -> None:
    print(f"{message}")
    for fruit, couleur in fruits.items():
        print(f"    - {fruit:10} -> {couleur}")
```

**Pourquoi ?**
- `dict_items([...])` est peu lisible
- Format clair et structuré
- Facilite la compréhension

### 2. Différence entre `[]` et `get()`
```python
# Accès direct avec [] : lève KeyError si la clé n'existe pas
couleur = fruits["banane"]

# Accès sécurisé avec get() : retourne None si la clé n'existe pas
couleur = fruits.get("banane")

# get() avec valeur par défaut
couleur = fruits.get("mangue", "inconnue")
```

**Pourquoi ?**
- `[]` est plus rapide mais risqué
- `get()` est plus sûr pour les clés incertaines
- Valeur par défaut évite les `None` inattendus

### 3. Vérification avant suppression
```python
# ❌ del peut échouer
 del fruits["banane"]  # KeyError si absent

# ✅ Vérification avec 'in'
if "banane" in fruits:
    del fruits["banane"]

# ✅ Alternative : pop() avec valeur par défaut
valeur = fruits.pop("banane", None)
```

**Pourquoi ?**
- `del` lève `KeyError` si la clé n'existe pas
- `in` vérifie la présence avant l'action
- `pop()` avec défaut est encore plus sûr

### 4. Les trois vues d'un dictionnaire
```python
fruits.keys()    # Vue des clés : dict_keys(['pomme', 'banane', ...])
fruits.values()  # Vue des valeurs : dict_values(['verte', 'jaune', ...])
fruits.items()   # Vue des paires : dict_items([('pomme', 'verte'), ...])
```

**Pourquoi ?**
- Permet d'accéder séparément aux clés, valeurs ou les deux
- `items()` est idéal pour les boucles : `for k, v in d.items()`
- `keys()` implicite dans `for k in d:` et `if k in d`

### 5. Ordre d'insertion (Python 3.7+)
```python
# Depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion
fruits = {"pomme": "verte", "banane": "jaune"}
# L'ordre est garanti : pomme d'abord, puis banane
```

**Pourquoi ?**
- Avant Python 3.7, l'ordre n'était pas garanti
- Maintenant, c'est une feature officielle
- Utile pour l'affichage et la logique métier

### 6. Clés de différents types
```python
# Les clés doivent être IMMUABLES
personne = {
    "nom": "Dupont",           # str
    42: "age",                  # int
    ("ville", "code"): "Paris"  # tuple
}
# ❌ Interdit : [1, 2]: "valeur"  # list comme clé -> TypeError
```

**Pourquoi ?**
- Les dictionnaires utilisent un hash des clés
- Seuls les objets immuables ont un hash stable
- `list` et `dict` sont mutables → interdits comme clés

---

## 📊 Récapitulatif des méthodes de dictionnaire

| Méthode | Description | Retourne |
|---------|-------------|----------|
| `d[key]` | Accès à la valeur (KeyError si absent) | La valeur |
| `d.get(key, defaut)` | Accès sécurisé | La valeur ou le défaut |
| `d[key] = val` | Ajout ou modification | - |
| `del d[key]` | Suppression (KeyError si absent) | - |
| `d.pop(key, defaut)` | Suppression sécurisée | La valeur supprimée |
| `d.popitem()` | Supprime la dernière paire | Le tuple (clé, valeur) |
| `d.keys()` | Vue des clés | `dict_keys` |
| `d.values()` | Vue des valeurs | `dict_values` |
| `d.items()` | Vue des paires | `dict_items` |
| `d.update(other)` | Fusionne avec un autre dict | `None` |
| `d.setdefault(key, val)` | Ajoute si absent | La valeur |
| `d.clear()` | Vide le dictionnaire | `None` |
| `d.copy()` | Copie superficielle | Nouveau dict |
| `key in d` | Teste la présence d'une clé | `bool` |
| `len(d)` | Nombre de paires | `int` |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Fonction d'affichage formatée (DRY)
- [x] Démonstration `[]` vs `get()` avec défaut
- [x] Vérification avant `del`
- [x] Démonstration des 3 vues (`keys`, `values`, `items`)
- [x] Mention de l'ordre d'insertion (Python 3.7+)
- [x] Démonstration des clés de différents types
- [x] Typage avec annotations
- [x] Docstring pour le module et les fonctions
- [x] Structure avec `main()`
- [x] `if __name__ == "__main__":` pour l'exécution
- [x] Messages d'affichage clairs et structurés

---

## 💬 Pour aller plus loin

1. **Compréhensions de dictionnaire** : `{k: v*2 for k, v in d.items()}`
2. **Dictionnaires imbriqués** : structures de données complexes
3. **defaultdict** : dictionnaire avec valeur par défaut automatique
4. **OrderedDict** : dictionnaire ordonné (avant Python 3.7)
5. **Counter** : compte les occurrences (collections)
6. **JSON** : sérialiser/désérialiser des dictionnaires

```python
# Exemples avancés
from collections import defaultdict, Counter

# Compréhension de dictionnaire
carres = {x: x**2 for x in range(5)}
print(carres)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# defaultdict : valeur par défaut automatique
notes = defaultdict(list)
notes["math"].append(15)
notes["math"].append(12)
print(notes)  # defaultdict(<class 'list'>, {'math': [15, 12]})

# Counter : compte les occurrences
mots = ["pomme", "banane", "pomme", "kiwi", "banane", "pomme"]
compteur = Counter(mots)
print(compteur)  # Counter({'pomme': 3, 'banane': 2, 'kiwi': 1})

# Dictionnaire imbriqué
personne = {
    "nom": "Dupont",
    "prenom": "Jean",
    "adresses": [
        {"type": "domicile", "ville": "Paris"},
        {"type": "travail", "ville": "Lyon"}
    ]
}
print(personne["adresses"][0]["ville"])  # "Paris"

# Fusion de dictionnaires (Python 3.9+)
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2  # {'a': 1, 'b': 3, 'c': 4}
print(d3)
```
