"""
Mon premier programme Python.

Ce programme affiche un message de bienvenue et effectue un calcul
pour comprendre l'ordre des opérations (priorité de la multiplication).
"""


def main():
    """Fonction principale du programme."""
    # Affichage du message de bienvenue
    print("J'apprends Python !")
    
    # Calcul avec priorité des opérateurs
    # Ordre : parenthèses > exposants > * et / > + et -
    # Ici : 35 * 2 = 70, puis 17 + 70 = 87
    resultat = 17 + 35 * 2
    
    # Affichage du résultat
    print(f"Le résultat de 17 + 35 * 2 est : {resultat}")
    
    # Vérification : le résultat doit être 87
    # Si on avait écrit (17 + 35) * 2, le résultat serait 104


if __name__ == "__main__":
    main()
