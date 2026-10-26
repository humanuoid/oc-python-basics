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
