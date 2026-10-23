# P2C2 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Statistiques sur une liste de nombres

Programme qui demande une liste de nombres séparés par des virgules, puis calcule :
- La somme des nombres
- La moyenne
- Le nombre de valeurs supérieures à la moyenne
- Le nombre de valeurs paires

---

## ✅ Analyse de ta solution

### Points forts
- ✅ **Calcul correct de la somme** (150 pour 10,20,30,40,50)
- ✅ **Calcul correct de la moyenne** (30)
- ✅ **Compte correct des nombres > moyenne** (2 nombres : 40, 50)
- ✅ **Utilisation de boucles `for`** appropriées
- ✅ **Structure logique** : saisie → calcul → affichage

### Points à améliorer

| Problème | Impact | Solution |
|----------|--------|----------|
| Conversion répétée | Inefficace, lent | Convertir une fois en liste |
| Pas de gestion des espaces | `"10, 20"` plante | Utiliser `.strip()` |
| Pas de validation | `"abc"` plante | Utiliser `try/except` |
| Partie manquante | Incomplet | Ajouter le compte des pairs |
| Pas de commentaires | Moins maintenable | Ajouter des commentaires |

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Statistiques sur une liste de nombres.

Ce programme calcule la somme, la moyenne, le nombre de valeurs
supérieures à la moyenne et le nombre de valeurs paires.
"""

def calculer_statistiques(nombres: list[float]) -> dict:
    """
    Calcule les statistiques d'une liste de nombres.
    
    Args:
        nombres: Liste de nombres (float ou int)
        
    Returns:
        Dictionnaire contenant:
        - somme: La somme des nombres
        - moyenne: La moyenne
        - superieurs_moyenne: Nombre de valeurs > moyenne
        - pairs: Nombre de valeurs paires
    """
    somme = sum(nombres)
    moyenne = somme / len(nombres)
    
    # Compter les nombres supérieurs à la moyenne
    superieurs_moyenne = sum(1 for n in nombres if n > moyenne)
    
    # Compter les nombres pairs
    pairs = sum(1 for n in nombres if n % 2 == 0)
    
    return {
        "somme": somme,
        "moyenne": moyenne,
        "superieurs_moyenne": superieurs_moyenne,
        "pairs": pairs
    }


def afficher_resultats(statistiques: dict) -> None:
    """Affiche les résultats des calculs statistiques."""
    print(f"Somme des nombres : {statistiques['somme']}")
    print(f"Moyenne : {statistiques['moyenne']:.2f}")
    print(f"Nombres > moyenne : {statistiques['superieurs_moyenne']}")
    print(f"Nombres pairs : {statistiques['pairs']}")


def main():
    """Fonction principale."""
    # Récupération de la saisie utilisateur
    saisie = input("Saisissez des nombres séparés par des virgules : ")
    
    # Conversion en liste de float avec nettoyage et validation
    try:
        # Split, strip chaque élément, conversion en float
        nombres = [float(n.strip()) for n in saisie.split(",")]
    except ValueError:
        print("Erreur : veuillez entrer uniquement des nombres valides.")
        raise SystemExit("Fin du programme")
    
    # Vérification que la liste n'est pas vide
    if not nombres:
        print("Erreur : veuillez entrer au moins un nombre.")
        raise SystemExit("Fin du programme")
    
    # Affichage de la liste pour vérification
    print(f"Liste des nombres : {nombres}")
    
    # Calcul des statistiques
    stats = calculer_statistiques(nombres)
    
    # Affichage des résultats
    afficher_resultats(stats)


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Conversion unique avec compréhension de liste
```python
# ❌ Ancienne version - Conversion répétée
nombres_list = nombres.split(",")
resultat = 0
for nombre in nombres_list:
    resultat += int(nombre)  # Conversion ici

avg = round(resultat / len(nombres_list))
count_avg = 0
for nombre in nombres_list:
    if int(nombre) > avg:  # Conversion à nouveau ici !
        count_avg += 1

# ✅ Nouvelle version - Conversion une seule fois
nombres = [float(n.strip()) for n in saisie.split(",")]
somme = sum(nombres)  # sum() est plus pythonique
moyenne = somme / len(nombres)
superieurs = sum(1 for n in nombres if n > moyenne)  # Compréhension
```

**Pourquoi ?**
- Évite de convertir chaque élément plusieurs fois
- Plus efficace (O(n) au lieu de O(2n))
- Plus lisible avec les compréhensions de liste
- `sum()` est une fonction built-in optimisée

### 2. Gestion des espaces avec `.strip()`
```python
# ❌ Ancienne version
nombres = input("Saisir nombres séparés par une virgule: ")
nombres_list = nombres.split(",")
# Si l'utilisateur entre "10, 20, 30", int(" 20") échoue

# ✅ Nouvelle version
nombres = [float(n.strip()) for n in saisie.split(",")]
# strip() supprime les espaces avant/après chaque nombre
```

**Pourquoi ?**
- Accepte les entrées avec espaces : `"10, 20, 30"`
- Plus tolérant pour l'utilisateur
- Meilleure expérience utilisateur

### 3. Validation avec `try/except`
```python
# ✅ Bonne pratique
try:
    nombres = [float(n.strip()) for n in saisie.split(",")]
except ValueError:
    print("Erreur : veuillez entrer uniquement des nombres valides.")
    raise SystemExit("Fin du programme")
```

**Pourquoi ?**
- Gère les entrées invalides (`"abc"`, `"10,abc"`)
- Message d'erreur clair
- Empêche le programme de planter

### 4. Calcul des nombres pairs
```python
# ✅ Ajout de la fonctionnalité manquante
pairs = sum(1 for n in nombres if n % 2 == 0)
```

**Pourquoi ?**
- La correction officielle inclut ce calcul
- Complète l'exercice
- Utilisation d'une compréhension pour compter

### 5. Décomposition en fonctions
```python
# ✅ Bonne pratique
calculer_statistiques()  # Logique de calcul
afficher_resultats()    # Logique d'affichage
main()                  # Orchestration
```

**Pourquoi ?**
- **Séparation des responsabilités** : chaque fonction fait une seule chose
- **Réutilisabilité** : `calculer_statistiques()` peut être réutilisée
- **Testabilité** : chaque fonction peut être testée indépendamment
- **Lisibilité** : code plus organisé et plus facile à comprendre

### 6. Typage avec annotations
```python
# ✅ Bonne pratique
def calculer_statistiques(nombres: list[float]) -> dict:
    pass
```

**Pourquoi ?**
- **Clarté** : indique le type attendu et retourné
- **Validation** : les outils de linting (mypy) peuvent vérifier
- **Documentation** : aide à comprendre le code

### 7. Utilisation de `sum()` et compréhensions
```python
# ❌ Ancienne version
resultat = 0
for nombre in nombres_list:
    resultat += int(nombre)

# ✅ Nouvelle version
somme = sum(nombres)
```

**Pourquoi ?**
- `sum()` est une fonction built-in optimisée
- Plus concis et plus lisible
- Plus "pythonique"

---

## 📊 Comparaison des comportements

| Entrée | Ta version | Version améliorée |
|--------|------------|-------------------|
| `"10,20,30,40,50"` | ✅ 150, 30, 2 | ✅ 150, 30, 2, 2 pairs |
| `"10, 20, 30"` | ❌ Erreur | ✅ 60, 20, 0, 2 pairs |
| `"abc"` | ❌ Plante | ✅ Message d'erreur |
| `""` (vide) | ❌ Plante | ✅ Message d'erreur |
| `"10,20,abc"` | ❌ Plante | ✅ Message d'erreur |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Conversion unique des entrées
- [x] Gestion des espaces avec `.strip()`
- [x] Validation avec `try/except`
- [x] Ajout du calcul des nombres pairs
- [x] Décomposition en fonctions
- [x] Typage avec annotations
- [x] Utilisation de `sum()` et compréhensions
- [x] `if __name__ == "__main__":` pour l'exécution
- [x] Docstrings pour toutes les fonctions
- [x] Messages d'erreur clairs
- [x] Affichage de la liste pour vérification

---

## 💬 Conseils pour aller plus loin

1. **Ajouter une validation** : vérifier que tous les nombres sont positifs si besoin
2. **Gérer les doublons** : compter les occurrences uniques
3. **Calculer d'autres statistiques** : médiane, mode, écart-type
4. **Utiliser `statistics`** : module standard pour les statistiques
5. **Ajouter des tests unitaires** : valider chaque fonction
6. **Lire depuis un fichier** : accepter une liste de nombres depuis un fichier CSV
