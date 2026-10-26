# P3C3 — Feedback et Solution Idéale

## 📋 Contexte
**Exercice :** Pipeline ETL (Extract, Transform, Load) avec CSV

Lire un fichier CSV (`input.csv`), calculer le salaire (heures × 15€/h), et écrire le résultat dans `output.csv`.

**Objectifs pédagogiques :**
- Lire un fichier CSV avec `csv.DictReader`
- Transformer les données (calcul de salaire)
- Écrire un fichier CSV avec `csv.DictWriter` ou `csv.writer`
- Organiser le code en pipeline ETL (Extract → Transform → Load)
- Valider le résultat avec des tests

---

## 📝 Ta solution

```python
from pathlib import Path
import csv

def extract(file_name):
    file = Path(__file__).parent / file_name

    with open(file, 'r') as file_csv:
        reader = csv.DictReader(file_csv, delimiter=',')
        return list(reader)


def main():
    header = ['nom', 'salaire']
    file_name = Path(__file__).parent / 'output.csv'

    with open(file_name, 'w') as file_csv:
        writer = csv.writer(file_csv, delimiter=',')
        writer.writerow(header)

        for person in extract('input.csv'):
            line = [person.get('nom'), int(person.get('heures_travaillees')) * 15]
            
            writer.writerow(line)

if __name__ == "__main__":
    main()
```

**Résultat :** ✅ **Tous les tests passent !**
```
nom,salaire
Pierre Durand,540
Paul Dupont,615
Edouard Gentil,600
```

---

## ✅ Analyse de ta solution

### 🌟 Points forts

| Aspect | Appréciation |
|--------|--------------|
| **Tests passent** | ✅ 100% fonctionnel — les calculs sont corrects |
| **`list(reader)`** | ⭐⭐⭐ Excellent ! Tu as bien retenu la leçon sur les itérateurs |
| **`Path` pour les chemins** | ⭐⭐⭐ Chemins robustes basés sur `__file__` |
| **`with open()`** | ⭐⭐⭐ Gestion correcte du contexte (fermeture auto) |
| **Code concis** | ⭐⭐⭐ 27 lignes, direct et lisible |
| **Structure `main()`** | ⭐⭐⭐ Bonne séparation logique/exécution |

### ⚠️ Points à améliorer

| Problème | Impact | Solution |
|----------|--------|----------|
| **Tout dans `main()`** | Moins modulaire, difficile à tester | Séparer en ETL (Extract, Transform, Load) |
| **`person.get()`** | Retourne `None` si clé absente → plante | Utiliser `person['clé']` avec vérification |
| **`csv.writer`** | Écriture manuelle de listes | `csv.DictWriter` plus robuste et lisible |
| **Pas de docstrings** | Documentation manquante | Ajouter des docstrings |
| **Pas de typage** | Moins de clarté | Annotations de type |
| **Pas de gestion d'erreurs** | Plante si fichier absent ou données invalides | `try/except` + validation |
| **`int(person.get(...))`** | Plante si `None` ou non numérique | Vérifier avant conversion |

---

## 📊 Comparaison : Ta version vs Correction

| Critère | Ta version | Correction officielle | Gagnant |
|---------|-----------|----------------------|---------|
| **Tests passent** | ✅ Oui | ✅ Oui | Égalité |
| **Architecture ETL** | ❌ Tout dans `main()` | ✅ 3 fonctions séparées | 🏆 Correction |
| **Modularité** | ⭐⭐ Faible | ⭐⭐⭐⭐ Forte | 🏆 Correction |
| **`list(reader)`** | ✅ Oui (pythonique) | ❌ Boucle manuelle | 🏆 Toi |
| **`Path` pour chemins** | ✅ Oui (robuste) | ❌ Chemins relatifs | 🏆 Toi |
| **`csv.DictWriter`** | ❌ `csv.writer` | ✅ `DictWriter` | 🏆 Correction |
| **Paramètres par défaut** | ❌ Non | ✅ `filename="input.csv"` | 🏆 Correction |
| **Lisibilité** | ⭐⭐⭐⭐ Bonne | ⭐⭐⭐ Bonne | 🏆 Toi |
| **Concision** | ⭐⭐⭐⭐⭐ 27 lignes | ⭐⭐⭐ 39 lignes | 🏆 Toi |

**Verdict :** Ta solution est **fonctionnelle et élégante** (surtout `list(reader)` et `Path`), mais la correction a une **meilleure architecture** (séparation ETL). La version idéale combine les deux !

---

## 💎 Solution Idéale avec Bonnes Pratiques

Cette version combine **tes bonnes pratiques** (`list(reader)`, `Path`) avec **l'architecture ETL** de la correction.

```python
"""
Pipeline ETL - Traitement de salaires depuis un fichier CSV.

Ce programme :
1. EXTRACT : Lit les données depuis input.csv
2. TRANSFORM : Calcule le salaire (heures travaillées × 15€/h)
3. LOAD : Écrit le résultat dans output.csv

Architecture ETL (Extract, Transform, Load) pour une meilleure
modularité, testabilité et maintenabilité.
"""

from pathlib import Path
from typing import List, Dict, Any
import csv

# ============================================================
# CONSTANTES
# ============================================================
TAUX_HORAIRE = 15  # € par heure travaillée

# Chemins basés sur l'emplacement de ce fichier (robuste)
DOSSIER = Path(__file__).parent
FICHIER_ENTREE = DOSSIER / "input.csv"
FICHIER_SORTIE = DOSSIER / "output.csv"

# Champs attendus dans le CSV d'entrée et de sortie
CHAMPS_ENTREE = ["nom", "heures_travaillees"]
CHAMPS_SORTIE = ["nom", "salaire"]


# ============================================================
# FONCTION 1 : EXTRACT (Extraction)
# ============================================================
def extract(file_path: Path = FICHIER_ENTREE) -> List[Dict[str, str]]:
    """
    Extrait les données d'un fichier CSV.
    
    Lit le fichier CSV et retourne une liste de dictionnaires,
    un dictionnaire par ligne (grâce à csv.DictReader).
    
    Args:
        file_path: Chemin vers le fichier CSV d'entrée
        
    Returns:
        Liste de dictionnaires contenant les données brutes
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si les champs requis sont manquants
        
    Example:
        >>> data = extract()
        >>> data[0]
        {'nom': 'Pierre Durand', 'heures_travaillees': '36'}
    """
    # Vérification que le fichier existe
    if not file_path.exists():
        raise FileNotFoundError(f"Fichier d'entrée non trouvé : {file_path}")
    
    with open(file_path, 'r', encoding='utf-8', newline='') as file_csv:
        reader = csv.DictReader(file_csv, delimiter=',')
        
        # Vérification que les champs requis sont présents
        if reader.fieldnames is None:
            raise ValueError("Le fichier CSV est vide ou mal formé")
        
        champs_manquants = set(CHAMPS_ENTREE) - set(reader.fieldnames)
        if champs_manquants:
            raise ValueError(
                f"Champs manquants dans le CSV : {champs_manquants}. "
                f"Attendu : {CHAMPS_ENTREE}"
            )
        
        # list() convertit l'itérateur en liste (pythonique)
        return list(reader)


# ============================================================
# FONCTION 2 : TRANSFORM (Transformation)
# ============================================================
def transform(data: List[Dict[str, str]], taux: int = TAUX_HORAIRE) -> List[Dict[str, Any]]:
    """
    Transforme les données brutes en données calculées.
    
    Calcule le salaire pour chaque personne :
        salaire = heures_travaillees × taux_horaire
    
    Args:
        data: Liste de dictionnaires avec les données brutes
        taux: Taux horaire en €/heure (défaut: 15)
        
    Returns:
        Liste de dictionnaires avec nom et salaire calculé
        
    Raises:
        KeyError: Si un champ requis est manquant
        ValueError: Si les heures ne sont pas un nombre valide
        
    Example:
        >>> data = [{'nom': 'Pierre', 'heures_travaillees': '36'}]
        >>> transform(data)
        [{'nom': 'Pierre', 'salaire': 540}]
    """
    resultat = []
    
    for person in data:
        try:
            # Accès direct avec [] (lève KeyError si absent)
            nom = person["nom"]
            heures_str = person["heures_travaillees"]
            
            # Conversion avec vérification
            heures = int(heures_str)
            if heures < 0:
                raise ValueError(f"Heures négatives pour {nom} : {heures}")
            
            # Calcul du salaire
            salaire = heures * taux
            
            resultat.append({
                "nom": nom,
                "salaire": salaire
            })
            
        except KeyError as e:
            raise KeyError(f"Champ manquant dans les données : {e}")
        except ValueError as e:
            raise ValueError(f"Donnée invalide pour {person.get('nom', 'inconnu')} : {e}")
    
    return resultat


# ============================================================
# FONCTION 3 : LOAD (Chargement)
# ============================================================
def load(data: List[Dict[str, Any]], file_path: Path = FICHIER_SORTIE) -> None:
    """
    Écrit les données dans un fichier CSV.
    
    Utilise csv.DictWriter pour une écriture robuste basée sur
    les noms de champs (plus sûr que csv.writer avec des listes).
    
    Args:
        data: Liste de dictionnaires à écrire
        file_path: Chemin vers le fichier CSV de sortie
        
    Raises:
        IOError: Si le fichier ne peut pas être écrit
        
    Example:
        >>> data = [{'nom': 'Pierre', 'salaire': 540}]
        >>> load(data, Path('test.csv'))
    """
    if not data:
        print("⚠️  Aucune donnée à écrire")
        return
    
    try:
        with open(file_path, 'w', encoding='utf-8', newline='') as file_csv:
            # DictWriter : écriture basée sur les noms de champs
            writer = csv.DictWriter(file_csv, fieldnames=CHAMPS_SORTIE, delimiter=',')
            
            # Écrit l'en-tête
            writer.writeheader()
            
            # Écrit chaque ligne
            writer.writerows(data)
            
        print(f"✅ {len(data)} lignes écrites dans {file_path.name}")
        
    except IOError as e:
        raise IOError(f"Erreur lors de l'écriture de {file_path} : {e}")


# ============================================================
# FONCTION PRINCIPALE (Orchestration ETL)
# ============================================================
def main() -> None:
    """
    Fonction principale - Orchestration du pipeline ETL.
    
    Exécute les 3 étapes :
    1. Extract : lecture de input.csv
    2. Transform : calcul des salaires
    3. Load : écriture dans output.csv
    """
    print("🚀 Démarrage du pipeline ETL...")
    print(f"📁 Entrée : {FICHIER_ENTREE.name}")
    print(f"📁 Sortie : {FICHIER_SORTIE.name}")
    print(f"💰 Taux horaire : {TAUX_HORAIRE}€/h")
    print()
    
    try:
        # ÉTAPE 1 : EXTRACT
        print("1️⃣  EXTRACT - Lecture des données...")
        data_brut = extract(FICHIER_ENTREE)
        print(f"   → {len(data_brut)} lignes lues")
        
        # ÉTAPE 2 : TRANSFORM
        print("2️⃣  TRANSFORM - Calcul des salaires...")
        data_transformed = transform(data_brut, TAUX_HORAIRE)
        print(f"   → {len(data_transformed)} salaires calculés")
        
        # ÉTAPE 3 : LOAD
        print("3️⃣  LOAD - Écriture du fichier...")
        load(data_transformed, FICHIER_SORTIE)
        
        print()
        print("✅ Pipeline ETL terminé avec succès !")
        
        # Affichage du résultat
        print()
        print("📊 Résultat :")
        for person in data_transformed:
            print(f"   {person['nom']}: {person['salaire']}€")
            
    except FileNotFoundError as e:
        print(f"❌ Erreur : {e}")
        raise SystemExit(1)
    except (KeyError, ValueError) as e:
        print(f"❌ Erreur de données : {e}")
        raise SystemExit(1)
    except IOError as e:
        print(f"❌ Erreur d'écriture : {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
```

---

## 🔍 Explications des améliorations

### 1. Architecture ETL (Extract, Transform, Load)

```python
# ❌ Ta version : tout dans main() (moins modulaire)
def main():
    # Extract
    data = extract('input.csv')
    # Transform + Load mélangés
    with open('output.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['nom', 'salaire'])
        for person in data:
            writer.writerow([person['nom'], int(person['heures']) * 15])

# ✅ Version idéale : 3 fonctions séparées (modulaire, testable)
def extract(file_path) -> List[Dict]: ...
def transform(data, taux) -> List[Dict]: ...
def load(data, file_path) -> None: ...
```

**Pourquoi ?**
- **Séparation des responsabilités** : chaque fonction fait une seule chose
- **Testabilité** : chaque étape peut être testée indépendamment
- **Réutilisabilité** : on peut changer le taux, le fichier, etc.
- **Maintenabilité** : plus facile à modifier et déboguer
- **Lisibilité** : le pipeline est clair (ETL)

### 2. `csv.DictWriter` vs `csv.writer`

```python
# ❌ Ta version : csv.writer (listes manuelles)
writer = csv.writer(file_csv)
writer.writerow(['nom', 'salaire'])  # En-tête manuel
for person in data:
    writer.writerow([person['nom'], person['salaire']])  # Liste manuelle

# ✅ Version idéale : csv.DictWriter (dictionnaires)
writer = csv.DictWriter(file_csv, fieldnames=['nom', 'salaire'])
writer.writeheader()  # En-tête automatique
writer.writerows(data)  # Écrit tous les dicts d'un coup
```

**Pourquoi ?**
- `DictWriter` est plus **robuste** (moins d'erreurs d'ordre)
- Les données sont des **dictionnaires** (cohérent avec DictReader)
- `writerows()` écrit tout en une ligne
- L'en-tête est géré automatiquement

### 3. `list(reader)` (que tu as déjà !)

```python
# ✅ Ta bonne pratique (à garder !)
return list(reader)  # Convertit l'itérateur en liste
```

**Pourquoi ?**
- Plus concis que la boucle `for`
- Pythonique
- On l'a vu ensemble : c'est la meilleure façon !

### 4. `Path` pour les chemins (que tu as déjà !)

```python
# ✅ Ta bonne pratique (à garder !)
DOSSIER = Path(__file__).parent
FICHIER_ENTREE = DOSSIER / "input.csv"
FICHIER_SORTIE = DOSSIER / "output.csv"
```

**Pourquoi ?**
- Fonctionne depuis n'importe quel répertoire
- Robuste
- Standard moderne Python

### 5. Accès direct `person["clé"]` vs `person.get("clé")`

```python
# ❌ Ta version : get() retourne None si absent
nom = person.get('nom')  # None si 'nom' n'existe pas
heures = person.get('heures_travaillees')  # None si absent
salaire = int(heures) * 15  # 💥 Plante si heures est None !

# ✅ Version idéale : accès direct avec vérification
nom = person["nom"]  # Lève KeyError si absent (clair !)
heures_str = person["heures_travaillees"]
try:
    heures = int(heures_str)
except ValueError:
    raise ValueError(f"Heures invalides pour {nom} : {heures_str}")
```

**Pourquoi ?**
- `get()` masque les erreurs (retourne `None` silencieusement)
- `[]` lève une exception claire si la clé est absente
- Mieux vaut un crash explicite qu'un comportement silencieux

### 6. Gestion d'erreurs complète

```python
# ✅ Version idéale : try/except à chaque étape
try:
    data_brut = extract(FICHIER_ENTREE)
except FileNotFoundError:
    print("❌ Fichier input.csv non trouvé")
    raise SystemExit(1)

try:
    heures = int(person["heures_travaillees"])
except ValueError:
    raise ValueError(f"Heures invalides : {person['heures_travaillees']}")
```

**Pourquoi ?**
- Messages d'erreur clairs pour l'utilisateur
- Évite les crashs inattendus
- Facile à déboguer

### 7. Typage avec annotations

```python
# ✅ Version idéale : typage complet
def extract(file_path: Path = FICHIER_ENTREE) -> List[Dict[str, str]]: ...
def transform(data: List[Dict[str, str]], taux: int = TAUX_HORAIRE) -> List[Dict[str, Any]]: ...
def load(data: List[Dict[str, Any]], file_path: Path = FICHIER_SORTIE) -> None: ...
```

**Pourquoi ?**
- Clarté sur les types attendus/retournés
- Aide les outils de vérification (mypy)
- Documentation intégrée

### 8. Docstrings complètes

```python
# ✅ Version idéale : docstring pour chaque fonction
def extract(file_path: Path = FICHIER_ENTREE) -> List[Dict[str, str]]:
    """
    Extrait les données d'un fichier CSV.
    
    Args:
        file_path: Chemin vers le fichier CSV d'entrée
        
    Returns:
        Liste de dictionnaires contenant les données brutes
        
    Raises:
        FileNotFoundError: Si le fichier n'existe pas
        ValueError: Si les champs requis sont manquants
        
    Example:
        >>> data = extract()
        >>> data[0]
        {'nom': 'Pierre Durand', 'heures_travaillees': '36'}
    """
```

**Pourquoi ?**
- Documentation accessible via `help(extract)`
- Explique le but, les paramètres, les retours, les erreurs
- Exemples d'utilisation (doctests)

### 9. Constantes pour les valeurs magiques

```python
# ❌ Ta version : valeur en dur
salaire = int(person.get('heures_travaillees')) * 15  # 15 = magique ?

# ✅ Version idéale : constante nommée
TAUX_HORAIRE = 15  # €/heure — nom explicite
salaire = heures * TAUX_HORAIRE
```

**Pourquoi ?**
- Le code s'explique de lui-même
- Facile à modifier (changer le taux en un seul endroit)
- Évite les "nombres magiques"

---

## 📊 Architecture ETL expliquée

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   EXTRACT   │ ──→ │  TRANSFORM  │ ──→ │    LOAD     │
│             │     │             │     │             │
│ input.csv   │     │  Calcul     │     │ output.csv  │
│ → List[Dict]│     │  salaire    │     │ ← List[Dict]│
└─────────────┘     └─────────────┘     └─────────────┘
     Lecture          Transformation        Écriture
```

**Avantages de cette architecture :**

| Avantage | Explication |
|----------|-------------|
| **Modularité** | Chaque étape est indépendante |
| **Testabilité** | On peut tester chaque fonction séparément |
| **Réutilisabilité** | `transform()` peut être réutilisée ailleurs |
| **Maintenabilité** | Facile à modifier une étape sans toucher les autres |
| **Lisibilité** | Le pipeline est clair et documenté |
| **Débogage** | Facile d'identifier où est le problème |

---

## 🎯 Checklist des bonnes pratiques appliquées

- [x] Architecture ETL (Extract, Transform, Load séparés)
- [x] `list(reader)` pour convertir l'itérateur (ta bonne pratique)
- [x] `Path` pour les chemins robustes (ta bonne pratique)
- [x] `csv.DictWriter` pour l'écriture (plus robuste que `csv.writer`)
- [x] `writerows()` pour écrire en une ligne
- [x] Accès direct `dict["clé"]` avec gestion d'erreurs
- [x] Gestion d'erreurs complète (`try/except`)
- [x] Validation des données (champs requis, valeurs négatives)
- [x] Typage avec annotations (`List`, `Dict`, `Path`, `Any`)
- [x] Docstrings complètes (Args, Returns, Raises, Example)
- [x] Constantes pour les valeurs magiques (`TAUX_HORAIRE`)
- [x] Paramètres par défaut (`file_path: Path = FICHIER_ENTREE`)
- [x] Structure avec `main()` et `if __name__ == "__main__"`
- [x] Messages d'affichage clairs et structurés
- [x] `encoding='utf-8'` et `newline=''` (bonnes pratiques CSV)

---

## 💬 Pour aller plus loin

### 1. Tests unitaires avec pytest
```python
# test_main.py
import pytest
from pathlib import Path
from main import extract, transform, load, TAUX_HORAIRE

def test_extract():
    data = extract(Path("input.csv"))
    assert len(data) == 3
    assert data[0]["nom"] == "Pierre Durand"

def test_transform():
    data = [{"nom": "Test", "heures_travaillees": "10"}]
    result = transform(data)
    assert result[0]["salaire"] == 150

def test_transform_taux_personnalise():
    data = [{"nom": "Test", "heures_travaillees": "10"}]
    result = transform(data, taux=20)
    assert result[0]["salaire"] == 200

def test_load(tmp_path):
    data = [{"nom": "Test", "salaire": 150}]
    output = tmp_path / "test.csv"
    load(data, output)
    assert output.exists()
    content = output.read_text()
    assert "nom,salaire" in content
    assert "Test,150" in content
```

### 2. Traitement de gros fichiers (streaming)
```python
# Pour les très gros fichiers, ne pas tout charger en mémoire
def process_large_csv(input_path, output_path, taux=15):
    """Traite un gros CSV ligne par ligne (streaming)."""
    with open(input_path, 'r') as f_in, open(output_path, 'w', newline='') as f_out:
        reader = csv.DictReader(f_in)
        writer = csv.DictWriter(f_out, fieldnames=['nom', 'salaire'])
        writer.writeheader()
        
        for row in reader:  # Traite ligne par ligne (économie mémoire)
            salaire = int(row['heures_travaillees']) * taux
            writer.writerow({'nom': row['nom'], 'salaire': salaire})
```

### 3. Configuration externe (fichier JSON/YAML)
```python
# config.json
# {
#   "taux_horaire": 15,
#   "fichier_entree": "input.csv",
#   "fichier_sortie": "output.csv"
# }

import json

def load_config(config_path="config.json"):
    with open(config_path) as f:
        return json.load(f)

config = load_config()
TAUX_HORAIRE = config["taux_horaire"]
```

### 4. Logging professionnel
```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

logger.info("Démarrage du pipeline ETL")
logger.debug(f"Lecture de {FICHIER_ENTREE}")
logger.warning("Taux horaire modifié")
logger.error("Fichier non trouvé")
```

### 5. Interface en ligne de commande (argparse)
```python
import argparse

def main():
    parser = argparse.ArgumentParser(description="Pipeline ETL salaires")
    parser.add_argument("--input", "-i", default="input.csv", help="Fichier d'entrée")
    parser.add_argument("--output", "-o", default="output.csv", help="Fichier de sortie")
    parser.add_argument("--taux", "-t", type=int, default=15, help="Taux horaire (€/h)")
    args = parser.parse_args()
    
    # Utilise args.input, args.output, args.taux
```

---

## 🏆 Félicitations !

Tu as terminé le **dernier exercice** du cours ! 🎉

### Bilan de ta progression :

| Partie | Exercices | Concepts clés |
|--------|-----------|---------------|
| **P1** | 5 exercices | Bases Python, variables, types, listes, dictionnaires |
| **P2** | 3 exercices | Structures de contrôle, fonctions, calculs |
| **P3** | 3 exercices | Modules, web scraping, ETL (CSV) |

### Ce que tu as appris :

1. **Les bases** : variables, types, structures de données
2. **La logique** : conditions, boucles, fonctions
3. **L'organisation** : modules, packages, structure de projet
4. **Le monde réel** : web scraping, traitement de fichiers CSV
5. **Les bonnes pratiques** : typage, docstrings, gestion d'erreurs, tests

### Ta solution P3C3 :

✅ **Fonctionnelle** — tous les tests passent
✅ **Moderne** — `list(reader)`, `Path`, structure `main()`
✅ **Concis** — 27 lignes, direct et lisible
⚠️ **À améliorer** — architecture ETL pour plus de modularité

**Bravo pour ce parcours !** 🚀 Tu as fait du très bon travail, notamment sur P3C2 avec la structure de projet moderne (`uv`, `pyproject.toml`).

---

*Fin du cours "Apprenez les bases du langage Python" — OpenClassrooms*
