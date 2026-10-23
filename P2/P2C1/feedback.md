# P2C1 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Calculatrice - Opérations de base (+, -, *, /)

Programme qui demande deux nombres et une opération à l'utilisateur, puis affiche le résultat.

---

## ✅ Analyse de ta solution

### Points forts
- ✅ **Utilisation de `match/case`** (Python 3.10+) — plus lisible et moderne que `if/elif`
- ✅ **Vérification des entrées** avec `isnumeric()` avant conversion
- ✅ **Gestion de la division par zéro**
- ✅ **Gestion des opérateurs inconnus**
- ✅ **Structure logique** : vérification → conversion → calcul → affichage

### Points à améliorer

| Problème | Impact | Solution |
|----------|--------|----------|
| Messages peu professionnels | Mauvaise expérience utilisateur | Messages clairs et respectueux |
| `isnumeric()` rejette les négatifs | `-5` n'est pas accepté | Utiliser `try/except` |
| Arrondi sans précision | `round(x)` au lieu de `round(x, 2)` | Spécifier 2 décimales |
| Pas de commentaires | Code moins maintenable | Ajouter des commentaires |

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Calculatrice simple pour les opérations de base.

Ce programme demande deux nombres et une opération à l'utilisateur,
puis affiche le résultat avec gestion des erreurs.
"""

def main():
    """Fonction principale de la calculatrice."""
    # Récupération des entrées utilisateur
    nombre1 = input("Entrez un nombre : ")
    nombre2 = input("Entrez un deuxième nombre : ")

    # Validation et conversion avec try/except (plus robuste que isnumeric)
    try:
        nombre1 = float(nombre1)
        nombre2 = float(nombre2)
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        raise SystemExit("Fin du programme")

    # Récupération de l'opération
    operation = input("Quelle opération ? (+, -, *, /) : ").strip()

    # Calcul selon l'opération choisie
    match operation:
        case "+":
            resultat = nombre1 + nombre2
        case "-":
            resultat = nombre1 - nombre2
        case "*":
            resultat = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                print("Erreur : impossible de diviser par zéro.")
                raise SystemExit("Fin du programme")
            resultat = round(nombre1 / nombre2, 2)
        case _:
            print(f"Erreur : opérateur '{operation}' non reconnu. Utilisez +, -, * ou /.")
            raise SystemExit("Fin du programme")

    # Affichage du résultat
    print(f"Résultat : {resultat}")


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Utilisation de `try/except` au lieu de `isnumeric()`
```python
# ❌ Ancienne version
if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

# ✅ Nouvelle version
try:
    nombre1 = float(nombre1)
    nombre2 = float(nombre2)
except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")
```

**Pourquoi ?**
- `isnumeric()` ne fonctionne pas avec les nombres négatifs (`-5`)
- `isnumeric()` ne fonctionne pas avec les décimaux (`5.5`)
- `try/except` est la méthode Python recommandée pour la validation
- `float()` accepte les entiers, négatifs et décimaux

### 2. Utilisation de `float()` au lieu de `int()`
```python
# ❌ Ancienne version
nombre1 = int(nombre1)

# ✅ Nouvelle version  
nombre1 = float(nombre1)
```

**Pourquoi ?**
- `int()` troncature les décimales (perte de précision)
- `float()` conserve la précision complète
- Pour une calculatrice, on veut gérer tous les types de nombres

### 3. Précision de l'arrondi
```python
# ❌ Ancienne version
resultat = round(nombre1 / nombre2)

# ✅ Nouvelle version
resultat = round(nombre1 / nombre2, 2)
```

**Pourquoi ?**
- `round(x)` arrondit à l'entier le plus proche
- `round(x, 2)` arrondit à 2 décimales (standard pour les calculs)

### 4. Messages d'erreur professionnels
```python
# ❌ Ancienne version
raise SystemExit("On peut pas diviser par 0 abruti !")
raise SystemExit("Opérateur inconnu, dommage !")

# ✅ Nouvelle version
print("Erreur : impossible de diviser par zéro.")
print(f"Erreur : opérateur '{operation}' non reconnu. Utilisez +, -, * ou /.")
```

**Pourquoi ?**
- Messages clairs et respectueux
- Indiquent exactement ce qui ne va pas
- Proposent une solution (quels opérateurs utiliser)

### 5. Structure avec `if __name__ == "__main__":`
```python
# ✅ Bonne pratique
if __name__ == "__main__":
    main()
```

**Pourquoi ?**
- Permet d'importer le module sans exécuter le code
- Sépare la logique de l'exécution
- Meilleure organisation du code

### 6. Utilisation de `.strip()`
```python
# ✅ Bonne pratique
operation = input("Quelle opération ? ").strip()
```

**Pourquoi ?**
- Supprime les espaces avant/après la saisie
- Évite les erreurs dues aux espaces accidentels

---

## 📊 Comparaison des comportements

| Entrée | Ta version | Version améliorée |
|--------|------------|-------------------|
| `5, 2, +` | ✅ 7 | ✅ 7 |
| `-5, 3, +` | ❌ Erreur | ✅ 2 |
| `5.5, 2.5, +` | ❌ Erreur | ✅ 8.0 |
| `5, 0, /` | ✅ Erreur | ✅ Erreur |
| `5, 2, %` | ✅ Erreur | ✅ Erreur |
| `abc, 2, +` | ✅ Erreur | ✅ Erreur |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Gestion des erreurs avec `try/except`
- [x] Utilisation de `float()` pour la précision
- [x] Arrondi à 2 décimales pour la division
- [x] Messages d'erreur clairs et professionnels
- [x] Structure avec fonction `main()`
- [x] `if __name__ == "__main__":` pour l'exécution
- [x] `.strip()` pour nettoyer les entrées
- [x] Docstring pour la fonction
- [x] Commentaires explicatifs

---

## 💬 Conseils pour aller plus loin

1. **Ajouter une boucle** pour permettre plusieurs calculs sans relancer le programme
2. **Gérer les opérations en majuscules** (`+`, `P`, `p`)
3. **Ajouter des tests unitaires** pour valider chaque fonction
4. **Utiliser `argparse`** pour accepter les arguments en ligne de commande
