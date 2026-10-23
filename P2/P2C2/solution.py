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
