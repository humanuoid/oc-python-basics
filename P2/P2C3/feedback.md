# P2C3 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Calcul de salaire horaire

Programme qui calcule le salaire horaire à partir du salaire annuel et du nombre d'heures travaillées par semaine.

Étapes :
1. Salaire annuel → Salaire mensuel (÷ 12)
2. Salaire mensuel → Salaire hebdomadaire (÷ 4)
3. Salaire hebdomadaire + Heures → Salaire horaire (÷ heures)

---

## ✅ Analyse de ta solution

### Points forts
- ✅ **Bonne décomposition en 3 fonctions** : claire et logique
- ✅ **Structure modulaire** : chaque fonction a une seule responsabilité
- ✅ **Arrondi à 2 décimales** pour le salaire horaire
- ✅ **Affichage correct** du résultat final

### ❌ Problèmes critiques

| Problème | Impact | Solution |
|----------|--------|----------|
| **`int()` au lieu de `float()`** | Perte de précision majeure | Utiliser `float()` |
| Pas de vérification heures = 0 | Division par zéro possible | Ajouter validation |
| Pas de gestion d'erreur | Plante sur entrée invalide | `try/except` |
| Variables globales | Moins maintenable | Utiliser `main()` |
| Pas de docstrings | Moins documenté | Ajouter docstrings |

---

## 🔴 Impact de `int()` vs `float()`

### Exemple concret :

```python
# Avec ta version (int)
salaire_annuel = "48000.50"  # 48 000,50 €
salaire_mensuel = int(salaire_annuel) / 12  # = 4000.0 (perte de 0.50 €)

# Avec la version corrigée (float)
salaire_annuel = float("48000.50")  # = 48000.50
salaire_mensuel = salaire_annuel / 12  # = 4000.4166... (précision conservée)
```

**Perte financière** :
- Mensuel : perte de 0,50 € / 12 = 0,0417 €
- Hebdomadaire : 0,0417 € / 4 = 0,0104 €
- Horaire (35h) : 0,0104 € / 35 = **0,0003 €/h**

C'est peu sur un exemple, mais sur des montants plus importants ou pour des calculs financiers professionnels, la perte de précision peut devenir significative.

---

## 💎 Solution Idéale avec Bonnes Pratiques

```python
"""
Calcul de salaire horaire.

Ce programme calcule le salaire horaire à partir du salaire annuel
et du nombre d'heures travaillées par semaine.
"""

def salaire_mensuel(salaire_annuel: float) -> float:
    """
    Calcule le salaire mensuel à partir du salaire annuel.
    
    Args:
        salaire_annuel: Salaire annuel brut (en euros)
        
    Returns:
        Salaire mensuel brut (en euros)
        
    Example:
        >>> salaire_mensuel(48000)
        4000.0
    """
    return salaire_annuel / 12


def salaire_hebdomadaire(salaire_mensuel: float) -> float:
    """
    Calcule le salaire hebdomadaire en supposant 4 semaines par mois.
    
    Args:
        salaire_mensuel: Salaire mensuel brut (en euros)
        
    Returns:
        Salaire hebdomadaire brut (en euros)
        
    Note:
        Cette approximation (4 semaines/mois) est courante mais
        peut varier selon les conventions de l'entreprise.
        
    Example:
        >>> salaire_hebdomadaire(4000)
        1000.0
    """
    return salaire_mensuel / 4


def salaire_horaire(salaire_hebdomadaire: float, heures_travaillees: float) -> float:
    """
    Calcule le salaire horaire.
    
    Args:
        salaire_hebdomadaire: Salaire hebdomadaire brut (en euros)
        heures_travaillees: Nombre d'heures travaillées par semaine
        
    Returns:
        Salaire horaire brut (en euros, arrondi à 2 décimales)
        
    Raises:
        ValueError: Si heures_travaillees est égal à 0
        
    Example:
        >>> salaire_horaire(1000, 35)
        28.57
    """
    if heures_travaillees == 0:
        raise ValueError("Le nombre d'heures travaillées ne peut pas être zéro.")
    
    return round(salaire_hebdomadaire / heures_travaillees, 2)


def main():
    """Fonction principale."""
    print("=== Calculateur de salaire horaire ===\n")
    
    # Récupération des entrées utilisateur avec validation
    try:
        salaire_annuel = float(input("Salaire annuel (€) : "))
        heures_travaillees = float(input("Heures travaillées par semaine : "))
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        raise SystemExit(1)
    
    # Calculs
    mensuel = salaire_mensuel(salaire_annuel)
    hebdomadaire = salaire_hebdomadaire(mensuel)
    horaire = salaire_horaire(hebdomadaire, heures_travaillees)
    
    # Affichage des résultats intermédiaires et final
    print(f"\n--- Résultats ---")
    print(f"Salaire mensuel : {mensuel:.2f} €")
    print(f"Salaire hebdomadaire : {hebdomadaire:.2f} €")
    print(f"Salaire horaire : {horaire:.2f} €")


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Utilisation de `float()` au lieu de `int()`
```python
# ❌ Ancienne version
def salaire_mensuel(salaire_annuel):
    salaire_mensuel = int(salaire_annuel) / 12  # ❌ Perte de précision
    return salaire_mensuel

# ✅ Nouvelle version
def salaire_mensuel(salaire_annuel: float) -> float:
    return salaire_annuel / 12  # ✅ Précision conservée
```

**Pourquoi ?**
- `int()` **troncature** les décimales (perte de données)
- `float()` **conserve** la précision complète
- Pour les calculs financiers, la précision est cruciale

### 2. Validation des heures travaillées
```python
# ✅ Nouvelle version
def salaire_horaire(salaire_hebdomadaire: float, heures_travaillees: float) -> float:
    if heures_travaillees == 0:
        raise ValueError("Le nombre d'heures travaillées ne peut pas être zéro.")
    return round(salaire_hebdomadaire / heures_travaillees, 2)
```

**Pourquoi ?**
- Empêche la division par zéro
- Message d'erreur clair et explicite
- Meilleure robustesse du code

### 3. Gestion des erreurs avec `try/except`
```python
# ✅ Nouvelle version
try:
    salaire_annuel = float(input("Salaire annuel (€) : "))
    heures_travaillees = float(input("Heures travaillées par semaine : "))
except ValueError:
    print("Erreur : veuillez entrer des nombres valides.")
    raise SystemExit(1)
```

**Pourquoi ?**
- Gère les entrées invalides (`"abc"`, `"50000€"`)
- Message d'erreur utile pour l'utilisateur
- Empêche le programme de planter

### 4. Typage avec annotations
```python
# ✅ Bonne pratique
def salaire_mensuel(salaire_annuel: float) -> float:
    pass
```

**Pourquoi ?**
- **Clarté** : indique clairement les types attendus
- **Validation** : les outils comme `mypy` peuvent vérifier
- **Documentation** : fait partie de la documentation de la fonction

### 5. Docstrings complètes
```python
# ✅ Bonne pratique
def salaire_mensuel(salaire_annuel: float) -> float:
    """
    Calcule le salaire mensuel à partir du salaire annuel.
    
    Args:
        salaire_annuel: Salaire annuel brut (en euros)
        
    Returns:
        Salaire mensuel brut (en euros)
        
    Example:
        >>> salaire_mensuel(48000)
        4000.0
    """
    return salaire_annuel / 12
```

**Pourquoi ?**
- **Documentation intégrée** : accessible via `help()`
- **Exemples** : montrent comment utiliser la fonction
- **Clarté** : explique le but et les paramètres

### 6. Structure avec `main()` et `if __name__ == "__main__":`
```python
# ✅ Bonne pratique
def main():
    # Logique principale ici
    pass

if __name__ == "__main__":
    main()
```

**Pourquoi ?**
- **Importable** : le module peut être importé sans exécuter le code
- **Organisé** : séparation claire entre logique et exécution
- **Testable** : les fonctions peuvent être testées indépendamment

### 7. Affichage des résultats intermédiaires
```python
# ✅ Nouvelle version
print(f"Salaire mensuel : {mensuel:.2f} €")
print(f"Salaire hebdomadaire : {hebdomadaire:.2f} €")
print(f"Salaire horaire : {horaire:.2f} €")
```

**Pourquoi ?**
- **Transparence** : l'utilisateur voit toutes les étapes
- **Vérification** : permet de vérifier les calculs intermédiaires
- **Pédagogique** : montre le processus complet

---

## 📊 Comparaison des comportements

| Entrée | Ta version | Version améliorée |
|--------|------------|-------------------|
| `48000, 35` | ⚠️ 28.57 € (perte de précision si décimales) | ✅ 28.57 € (précision complète) |
| `48000.50, 35` | ❌ 28.57 € (perte de 0.50 €) | ✅ 28.57 € (précision conservée) |
| `48000, 0` | ❌ Division par zéro | ✅ Message d'erreur |
| `"abc", 35` | ❌ Plante | ✅ Message d'erreur |
| `48000, "abc"` | ❌ Plante | ✅ Message d'erreur |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Utilisation de `float()` au lieu de `int()`
- [x] Validation des heures travaillées (≠ 0)
- [x] Gestion des erreurs avec `try/except`
- [x] Typage avec annotations
- [x] Docstrings complètes avec exemples
- [x] Structure avec `main()` et `if __name__ == "__main__":`
- [x] Messages d'erreur clairs
- [x] Affichage des résultats intermédiaires
- [x] Arrondi à 2 décimales pour l'affichage
- [x] Formatage des nombres avec `:.2f`

---

## 💬 Conseils pour aller plus loin

1. **Gérer les conventions** : permettre de configurer le nombre de semaines/mois
2. **Ajouter les cotisations** : calculer le salaire net à partir du brut
3. **Gérer les primes** : ajouter des primes mensuelles/annuelles
4. **Historique** : sauvegarder les calculs précédents
5. **Interface graphique** : utiliser `tkinter` pour une interface visuelle
6. **Tests unitaires** : valider chaque fonction avec `unittest` ou `pytest`
7. **Calculs inverses** : salaire horaire → salaire annuel
8. **Gestion des arrondis** : permettre de configurer le nombre de décimales
