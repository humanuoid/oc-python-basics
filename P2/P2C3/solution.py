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
