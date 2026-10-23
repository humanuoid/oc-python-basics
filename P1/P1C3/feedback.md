# P1C3 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Introduction à Python - Premier programme

Premier contact avec Python : afficher un message et effectuer un calcul simple.

**Objectifs pédagogiques :**
- Utiliser la fonction `print()`
- Comprendre l'ordre des opérations (priorité des opérateurs)
- Stocker le résultat d'un calcul dans une variable

---

## 📝 Énoncé actuel

```python
print("J'apprends Python !")

res = 17 + 35 * 2

print(res)
```

**Ce qui est demandé :**
1. Afficher le message "J'apprends Python !"
2. Calculer `17 + 35 * 2` et stocker le résultat dans une variable
3. Afficher ce résultat

---

## ✅ Analyse de la solution de base

### Points positifs
- ✅ Utilisation correcte de `print()`
- ✅ Ordre des opérations respecté (`*` avant `+`)
- ✅ Variable nommée de manière explicite (`res`)
- ✅ Calcul stocké avant affichage

### Points à améliorer

| Aspect | Problème | Solution |
|--------|----------|----------|
| Nom de variable | `res` est trop générique | Nom plus explicite (`resultat`) |
| Calcul direct | Pas d'affichage du calcul lui-même | Afficher l'opération et le résultat |
| Pas de commentaires | Code non documenté | Ajouter des commentaires explicatifs |
| Pas de vérification | Pas de contrôle du résultat | Ajouter un commentaire avec le résultat attendu |

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Mon premier programme Python.

Ce programme affiche un message de bienvenue et effectue un calcul
pour comprendre l'ordre des opérations (priorité de la multiplication).
"""


def main():
    """Fonction principale du programme."""
    # Affichage du message de bienvenue
    print("J'apprends Python !")
    
    # Calcul avec priorité des opérateurs
    # Ordre : parenthèses > exposants > * et / > + et -
    # Ici : 35 * 2 = 70, puis 17 + 70 = 87
    resultat = 17 + 35 * 2
    
    # Affichage du résultat
    print(f"Le résultat de 17 + 35 * 2 est : {resultat}")
    
    # Vérification : le résultat doit être 87
    # Si on avait écrit (17 + 35) * 2, le résultat serait 104


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Nom de variable explicite
```python
# ❌ Moins clair
res = 17 + 35 * 2

# ✅ Plus explicite
resultat = 17 + 35 * 2
```

**Pourquoi ?**
- Un nom de variable clair facilite la lecture
- `res` pourrait signifier "résultat", "réseau", "réservé"...
- `resultat` ne laisse aucun doute

### 2. Affichage explicite avec f-string
```python
# ❌ Moins informatif
print(res)

# ✅ Plus clair
print(f"Le résultat de 17 + 35 * 2 est : {resultat}")
```

**Pourquoi ?**
- L'utilisateur voit exactement ce qui a été calculé
- Plus pédagogique et compréhensible

### 3. Documentation avec docstring
```python
"""
Mon premier programme Python.

Ce programme affiche un message de bienvenue et effectue un calcul
pour comprendre l'ordre des opérations (priorité de la multiplication).
"""
```

**Pourquoi ?**
- Explique le but du programme
- Aide les autres développeurs (et soi-même plus tard)
- Bonne pratique dès le début

### 4. Structure avec fonction main()
```python
def main():
    # Code principal ici
    pass

if __name__ == "__main__":
    main()
```

**Pourquoi ?**
- Bonne habitude à prendre dès le début
- Facilite les tests et la réutilisation
- Sépare la logique de l'exécution

### 5. Commentaires explicatifs
```python
# Ordre : parenthèses > exposants > * et / > + et -
# Ici : 35 * 2 = 70, puis 17 + 70 = 87
```

**Pourquoi ?**
- Explique le raisonnement
- Rappelle les règles de priorité
- Aide à comprendre pourquoi le résultat est 87 et pas 104

---

## 📊 Comprendre l'ordre des opérations

| Expression | Calcul étape par étape | Résultat |
|------------|------------------------|----------|
| `17 + 35 * 2` | `35 * 2 = 70` → `17 + 70` | **87** ✅ |
| `(17 + 35) * 2` | `17 + 35 = 52` → `52 * 2` | **104** |

**Règle PEMDAS/BODMAS :**
- **P**arentheses / **B**rackets
- **E**xposants / **O**rders
- **M**ultiplication et **D**ivision (gauche à droite)
- **A**ddition et **S**oustraction (gauche à droite)

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Nom de variable explicite
- [x] Docstring pour le module
- [x] Docstring pour la fonction
- [x] Commentaires explicatifs
- [x] Structure avec `main()`
- [x] `if __name__ == "__main__":` pour l'exécution
- [x] Affichage informatif avec f-string
- [x] Explication de l'ordre des opérations

---

## 💬 Pour aller plus loin

1. **Demander des valeurs à l'utilisateur** avec `input()`
2. **Faire plusieurs calculs** et les comparer
3. **Utiliser des variables** pour stocker les nombres avant de calculer
4. **Afficher les étapes intermédiaires** du calcul

```python
# Version interactive
a = float(input("Entrez un nombre : "))
b = float(input("Entrez un autre nombre : "))
print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")
```
