# P1C5 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Types de variables - Découverte des types de données

Créer des variables de différents types et afficher leurs types avec `type()`.

**Objectifs pédagogiques :**
- Comprendre les 4 types de base : `str`, `int`, `float`, `bool`
- Utiliser la fonction `type()` pour identifier le type d'une variable
- Comprendre la différence entre types numériques (`int` vs `float`)
- Manipuler des variables de différents types

---

## 📝 Énoncé actuel

```python
name = "Emmanuel"
age = 36
size = 1.70
is_student = True

print(f"Nom: {name}")
print(f"Âge: {age}")
print(f"Taille: {size}")
print(f"Est étudiant: {is_student}")

print(f"Type nom: {type(name)}")
print(f"Type âge: {type(age)}")
print(f"Type taille: {type(size)}")
print(f"Type est étudiant: {type(is_student)}")
```

**Ce qui est demandé :**
1. Créer 4 variables de types différents (str, int, float, bool)
2. Afficher les valeurs de ces variables
3. Afficher les types de ces variables avec `type()`

---

## ✅ Analyse de la solution de base

### Points positifs
- ✅ Les 4 types de base sont représentés
- ✅ Utilisation correcte de `type()`
- ✅ Affichage clair avec f-strings
- ✅ Bonne séparation valeurs / types

### Points à améliorer

| Aspect | Problème | Solution |
|--------|----------|----------|
| Convention de nommage | `name` trop générique | `first_name` plus explicite |
| Accents dans les f-strings | `Âge` avec accent | Éviter ou gérer correctement l'encodage |
| Répétition du print | Beaucoup de lignes similaires | Utiliser une fonction |
| Pas de commentaires | Non documenté | Ajouter des commentaires sur les types |
| Pas de conversion | Ne montre pas les conversions | Montrer `int()`, `float()`, `str()`, `bool()` |
| Pas de docstring | Non documenté | Ajouter une docstring |

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Découverte des types de variables en Python.

Ce programme crée des variables de différents types (str, int, float, bool),
affiche leurs valeurs et leurs types avec la fonction type().
"""


def afficher_info(variable, description: str) -> None:
    """
    Affiche la valeur et le type d'une variable.
    
    Args:
        variable: La variable à inspecter
        description: Description de la variable
    """
    print(f"{description}")
    print(f"  Valeur : {variable}")
    print(f"  Type   : {type(variable).__name__}")
    print()


def main():
    """Fonction principale du programme."""
    # ============================================================
    # CRÉATION DES VARIABLES DE DIFFÉRENTS TYPES
    # ============================================================
    
    # str (string) : chaîne de caractères, texte
    first_name = "Emmanuel"
    
    # int (integer) : nombre entier
    age = 36
    
    # float : nombre décimal (à virgule flottante)
    size = 1.70
    
    # bool (boolean) : valeur booléenne (True ou False)
    is_student = True
    
    # ============================================================
    # AFFICHAGE DES VALEURS ET DES TYPES
    # ============================================================
    
    print("=" * 50)
    print("INFORMATIONS PERSONNELLES")
    print("=" * 50)
    print()
    
    # Affichage des valeurs
    afficher_info(first_name, "Nom")
    afficher_info(age, "Age")
    afficher_info(size, "Taille (m)")
    afficher_info(is_student, "Etudiant")
    
    # ============================================================
    # CONVERSIONS DE TYPES (CASTING)
    # ============================================================
    
    print("=" * 50)
    print("CONVERSIONS DE TYPES")
    print("=" * 50)
    
    # int -> float
    age_as_float = float(age)
    print(f"int -> float : {age} devient {age_as_float} ({type(age_as_float).__name__})")
    
    # float -> int (attention : perte de précision !)
    size_as_int = int(size)
    print(f"float -> int : {size} devient {size_as_int} ({type(size_as_int).__name__})")
    
    # int -> str
    age_as_str = str(age)
    print(f"int -> str   : {age} devient '{age_as_str}' ({type(age_as_str).__name__})")
    
    # str -> int (si la chaîne contient un nombre)
    nombre_str = "42"
    nombre_int = int(nombre_str)
    print(f"str -> int   : '{nombre_str}' devient {nombre_int} ({type(nombre_int).__name__})")


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Fonction réutilisable pour l'affichage
```python
# ❌ Répétition de code
print(f"Type nom: {type(name)}")
print(f"Type âge: {type(age)}")

# ✅ Fonction réutilisable
def afficher_info(variable, description: str) -> None:
    print(f"{description}")
    print(f"  Valeur : {variable}")
    print(f"  Type   : {type(variable).__name__}")
```

**Pourquoi ?**
- **DRY** (Don't Repeat Yourself) : pas de code dupliqué
- Plus facile à modifier
- Plus lisible

### 2. Utilisation de `type(variable).__name__`
```python
# ❌ Affiche <class 'str'>
print(type(name))

# ✅ Affiche juste 'str'
print(type(name).__name__)
```

**Pourquoi ?**
- `type(name)` retourne `<class 'str'>`
- `.__name__` extrait juste le nom du type : `'str'`
- Plus propre et lisible

### 3. Démonstration des conversions de types
```python
# int -> float
age_as_float = float(age)

# float -> int (perte de précision !)
size_as_int = int(size)

# int -> str
age_as_str = str(age)

# str -> int
nombre_int = int("42")
```

**Pourquoi ?**
- Montre les 4 fonctions de conversion essentielles
- Illustre la perte de précision (`float` → `int`)
- Pédagogique pour comprendre les types

### 4. Typage avec annotations
```python
def afficher_info(variable, description: str) -> None:
    pass
```

**Pourquoi ?**
- Indique les types attendus
- Aide les outils de vérification (mypy)
- Meilleure documentation

---

## 📊 Tableau récapitulatif des types

| Type Python | Exemple | Description | Conversion |
|-------------|---------|-------------|------------|
| `str` | `"Emmanuel"` | Chaîne de caractères | `str(x)` |
| `int` | `36` | Nombre entier | `int(x)` |
| `float` | `1.70` | Nombre décimal | `float(x)` |
| `bool` | `True` / `False` | Valeur booléenne | `bool(x)` |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Convention de nommage explicite
- [x] Fonction réutilisable (DRY)
- [x] Utilisation de `type().__name__` pour l'affichage propre
- [x] Démonstration des conversions de types
- [x] Typage avec annotations
- [x] Docstring pour le module et les fonctions
- [x] Commentaires explicatifs
- [x] Structure avec `main()`
- [x] `if __name__ == "__main__":` pour l'exécution

---

## 💬 Pour aller plus loin

1. **Version interactive** avec `input()` et validation
2. **Vérifier le type** avec `isinstance()` au lieu de `type()`
3. **Gérer les grands nombres** avec des séparateurs (`1_000_000`)
4. **Utiliser `decimal`** pour les calculs financiers précis
5. **Créer des types personnalisés** avec des classes

```python
# isinstance() est souvent préférable à type()
age = 36
if isinstance(age, int):
    print("C'est un entier !")

# Grands nombres lisibles
salaire = 1_500_000  # 1 500 000
print(f"Salaire : {salaire:,} €")  # Affiche : 1,500,000 €
```
