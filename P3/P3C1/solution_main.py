"""
Programme principal - Calculatrice modulaire.

Ce programme importe les fonctions du module `operations` et les utilise
pour effectuer des calculs simples. Il démontre comment organiser son code
en modules réutilisables.
"""

# ============================================================
# IMPORTS
# ============================================================
# Méthode 1 : import du module entier (recommandée pour éviter les conflits)
import operations

# Méthode 2 : import de fonctions spécifiques (aussi valide)
# from operations import addition, multiplication

# Méthode 3 : import avec alias
# import operations as ops


def main() -> None:
    """
    Fonction principale du programme.
    
    Effectue une addition et une multiplication en utilisant
    les fonctions du module operations.
    """
    print("=" * 50)
    print("CALCULATRICE MODULAIRE")
    print("=" * 50)
    print()
    
    # ============================================================
    # OPÉRATION 1 : ADDITION
    # ============================================================
    a, b = 3, 5
    resultat_addition = operations.addition(a, b)
    print(f"Addition : {a} + {b} = {resultat_addition}")
    
    # ============================================================
    # OPÉRATION 2 : MULTIPLICATION
    # ============================================================
    c, d = 8, 2
    resultat_multiplication = operations.multiplication(c, d)
    print(f"Multiplication : {c} * {d} = {resultat_multiplication}")
    
    # ============================================================
    # BONUS : AUTRES OPÉRATIONS DISPONIBLES
    # ============================================================
    print()
    print("--- Autres opérations disponibles ---")
    print(f"Soustraction : {a} - {b} = {operations.soustraction(a, b)}")
    print(f"Division : {c} / {d} = {operations.division(c, d)}")
    
    # Démonstration de la gestion d'erreur
    print()
    print("--- Test de la gestion d'erreur ---")
    try:
        operations.division(10, 0)
    except ValueError as e:
        print(f"Division par zéro interceptée : {e}")
    
    print()
    print("=" * 50)
    print("Calculs terminés avec succès !")
    print("=" * 50)


if __name__ == "__main__":
    main()
