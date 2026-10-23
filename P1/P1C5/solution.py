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
