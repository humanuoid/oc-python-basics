"""
Calculatrice simple pour les opérations de base.

Ce programme demande deux nombres et une opération à l'utilisateur,
puis affiche le résultat avec gestion des erreurs.
"""


def main():
    """Fonction principale de la calculatrice."""
    # Récupération des entrées utilisateur
    nombre1 = input("Entrez un nombre : ")
    nombre2 = input("Entrez un deuxième nombre : ")

    # Validation et conversion avec try/except (plus robuste que isnumeric)
    try:
        nombre1 = float(nombre1)
        nombre2 = float(nombre2)
    except ValueError:
        print("Erreur : veuillez entrer des nombres valides.")
        raise SystemExit("Fin du programme")

    # Récupération de l'opération
    operation = input("Quelle opération ? (+, -, *, /) : ").strip()

    # Calcul selon l'opération choisie
    match operation:
        case "+":
            resultat = nombre1 + nombre2
        case "-":
            resultat = nombre1 - nombre2
        case "*":
            resultat = nombre1 * nombre2
        case "/":
            if nombre2 == 0:
                print("Erreur : impossible de diviser par zéro.")
                raise SystemExit("Fin du programme")
            resultat = round(nombre1 / nombre2, 2)
        case _:
            print(f"Erreur : opérateur '{operation}' non reconnu. Utilisez +, -, * ou /.")
            raise SystemExit("Fin du programme")

    # Affichage du résultat
    print(f"Résultat : {resultat}")


if __name__ == "__main__":
    main()
