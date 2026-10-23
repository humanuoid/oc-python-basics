"""
Module d'opérations mathématiques de base.

Ce module fournit des fonctions pour effectuer les quatre opérations
arithmétiques fondamentales : addition, soustraction, multiplication
et division.

Auteur : [Ton nom]
Date : 2026
"""

from typing import Union

# Type alias pour les nombres acceptés (int ou float)
Nombre = Union[int, float]


def addition(a: Nombre, b: Nombre) -> Nombre:
    """
    Calcule la somme de deux nombres.
    
    Args:
        a: Premier nombre (entier ou décimal)
        b: Deuxième nombre (entier ou décimal)
        
    Returns:
        La somme de a et b
        
    Examples:
        >>> addition(3, 5)
        8
        >>> addition(2.5, 1.5)
        4.0
    """
    return a + b


def soustraction(a: Nombre, b: Nombre) -> Nombre:
    """
    Calcule la différence entre deux nombres.
    
    Args:
        a: Premier nombre (minuende)
        b: Deuxième nombre (diminuende)
        
    Returns:
        La différence a - b
        
    Examples:
        >>> soustraction(10, 3)
        7
        >>> soustraction(5.5, 2.0)
        3.5
    """
    return a - b


def multiplication(a: Nombre, b: Nombre) -> Nombre:
    """
    Calcule le produit de deux nombres.
    
    Args:
        a: Premier nombre (multiplicande)
        b: Deuxième nombre (multiplicateur)
        
    Returns:
        Le produit de a et b
        
    Examples:
        >>> multiplication(8, 2)
        16
        >>> multiplication(2.5, 4)
        10.0
    """
    return a * b


def division(a: Nombre, b: Nombre) -> float:
    """
    Calcule le quotient de deux nombres.
    
    Args:
        a: Numérateur (nombre à diviser)
        b: Dénominateur (nombre par lequel on divise)
        
    Returns:
        Le quotient a / b (toujours un float)
        
    Raises:
        ValueError: Si b est égal à zéro (division par zéro impossible)
        
    Examples:
        >>> division(10, 2)
        5.0
        >>> division(7, 2)
        3.5
        >>> division(5, 0)
        Traceback (most recent call last):
        ...
        ValueError: La division par zéro est impossible.
    """
    if b == 0:
        raise ValueError("La division par zéro est impossible.")
    return a / b


# ============================================================
# Tests rapides (exécutés seulement si le module est lancé directement)
# ============================================================
if __name__ == "__main__":
    # Tests simples pour vérifier que le module fonctionne
    print("Tests du module operations :")
    print(f"  addition(3, 5) = {addition(3, 5)}")
    print(f"  soustraction(10, 3) = {soustraction(10, 3)}")
    print(f"  multiplication(8, 2) = {multiplication(8, 2)}")
    print(f"  division(10, 2) = {division(10, 2)}")
    
    # Test de la gestion d'erreur
    try:
        division(5, 0)
    except ValueError as e:
        print(f"  division(5, 0) -> Erreur capturée : {e}")
