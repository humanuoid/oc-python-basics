"""
Gestion de variables et f-strings - Version interactive.

Ce programme demande le nom et l'âge à l'utilisateur,
les affiche, puis calcule l'âge dans 15 ans.
"""


def main():
    """Fonction principale du programme."""
    # Demande des informations à l'utilisateur
    first_name = input("Quel est votre prénom ? ")
    
    # Récupération de l'âge avec conversion en entier et validation
    try:
        age = int(input("Quel est votre âge ? "))
    except ValueError:
        print("Erreur : veuillez entrer un nombre entier pour l'âge.")
        raise SystemExit("Fin du programme")
    
    # Affichage avec les données de l'utilisateur
    print(f"Bonjour, je m'appelle {first_name} et j'ai {age} ans.")
    
    # Calcul de l'âge dans 15 ans
    age_dans_15_ans = age + 15
    
    # Affichage du résultat
    print(f"Dans 15 ans, j'aurai {age_dans_15_ans} ans.")


if __name__ == "__main__":
    main()
