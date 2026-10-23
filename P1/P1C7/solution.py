"""
Manipulation de dictionnaires en Python.

Ce programme démontre les opérations de base sur les dictionnaires :
création, ajout, accès, modification, suppression et vues (keys, values, items).
"""


def afficher_dictionnaire(fruits: dict, message: str) -> None:
    """
    Affiche un dictionnaire de manière formatée.
    
    Args:
        fruits: Le dictionnaire à afficher
        message: Message à afficher avant le dictionnaire
    """
    print(f"{message}")
    print(f"  Nombre d'éléments : {len(fruits)}")
    print("  Contenu :")
    for fruit, couleur in fruits.items():
        print(f"    - {fruit:10} -> {couleur}")
    print()


def main():
    """Fonction principale du programme."""
    print("=" * 50)
    print("MANIPULATION DE DICTIONNAIRES - DÉMONSTRATION")
    print("=" * 50)
    print()
    
    # ============================================================
    # ÉTAPE 1 : CRÉATION DU DICTIONNAIRE
    # ============================================================
    # Un dictionnaire stocke des paires clé-valeur
    # Syntaxe : {clé1: valeur1, clé2: valeur2, ...}
    # Les clés doivent être IMMUABLES (str, int, tuple)
    fruits = {
        "pomme": "verte",
        "banane": "jaune",
        "orange": "orange"
    }
    afficher_dictionnaire(fruits, "1. Création du dictionnaire initial :")
    
    # ============================================================
    # ÉTAPE 2 : AJOUT D'UNE NOUVELLE PAIRE CLÉ-VALEUR
    # ============================================================
    # fruits["kiwi"] = "vert" ajoute ou modifie une entrée
    fruits["kiwi"] = "vert"
    afficher_dictionnaire(fruits, "2. Après ajout de 'kiwi': 'vert' :")
    
    # ============================================================
    # ÉTAPE 3 : ACCÈS À UNE VALEUR (plusieurs méthodes)
    # ============================================================
    print("3. Accès à la couleur de 'banane' :")
    
    # Méthode 1 : avec [] (lève KeyError si la clé n'existe pas)
    try:
        couleur_banane = fruits["banane"]
        print(f"   fruits['banane'] = '{couleur_banane}'")
    except KeyError:
        print("   Clé 'banane' non trouvée !")
    
    # Méthode 2 : avec get() (retourne None si la clé n'existe pas)
    couleur_banane = fruits.get("banane")
    print(f"   fruits.get('banane') = '{couleur_banane}'")
    
    # Méthode 3 : avec get() et valeur par défaut
    couleur_mangue = fruits.get("mangue", "couleur inconnue")
    print(f"   fruits.get('mangue', 'couleur inconnue') = '{couleur_mangue}'")
    print()
    
    # ============================================================
    # ÉTAPE 4 : MODIFICATION D'UNE VALEUR EXISTANTE
    # ============================================================
    # Même syntaxe que l'ajout : si la clé existe, la valeur est modifiée
    ancienne_couleur = fruits["pomme"]
    fruits["pomme"] = "rouge"  # La pomme devient rouge
    print(f"4. Modification de 'pomme' : '{ancienne_couleur}' -> '{fruits['pomme']}'")
    afficher_dictionnaire(fruits, "   Résultat :")
    
    # ============================================================
    # ÉTAPE 5 : SUPPRESSION D'UNE PAIRE (plusieurs méthodes)
    # ============================================================
    print("5. Suppression de 'banane' :")
    
    # Méthode 1 : del (lève KeyError si la clé n'existe pas)
    cle_a_supprimer = "banane"
    if cle_a_supprimer in fruits:
        del fruits[cle_a_supprimer]
        print(f"   del fruits['{cle_a_supprimer}'] effectué")
    else:
        print(f"   '{cle_a_supprimer}' n'existe pas dans le dictionnaire")
    
    # Méthode 2 : pop() (retourne la valeur supprimée, lève KeyError si absente)
    # valeur = fruits.pop("banane", None)  # None si la clé n'existe pas
    
    # Méthode 3 : popitem() (supprime et retourne la DERNIÈRE paire insérée)
    # Note : depuis Python 3.7, les dictionnaires conservent l'ordre d'insertion
    
    afficher_dictionnaire(fruits, "   Après suppression :")
    
    # ============================================================
    # ÉTAPE 6 : LES TROIS VUES D'UN DICTIONNAIRE
    # ============================================================
    print("6. Les trois vues d'un dictionnaire :")
    print(f"   keys()   : {list(fruits.keys())}")
    print(f"   values() : {list(fruits.values())}")
    print(f"   items()  : {list(fruits.items())}")
    print()
    
    # ============================================================
    # RÉSULTAT FINAL
    # ============================================================
    afficher_dictionnaire(fruits, "RÉSULTAT FINAL :")
    
    # ============================================================
    # MÉTHODES UTILES SUPPLÉMENTAIRES
    # ============================================================
    print("=" * 50)
    print("AUTRES MÉTHODES UTILES")
    print("=" * 50)
    
    # in : vérifie si une clé existe
    print(f"'kiwi' in fruits : {'kiwi' in fruits}")
    print(f"'mangue' in fruits : {'mangue' in fruits}")
    
    # update() : fusionne deux dictionnaires
    nouveaux_fruits = {"mangue": "orange", "pasteque": "rouge"}
    fruits.update(nouveaux_fruits)
    print(f"Après update() : {len(fruits)} fruits")
    
    # setdefault() : ajoute une clé si elle n'existe pas
    fruits.setdefault("cerise", "rouge")
    print(f"setdefault('cerise', 'rouge') : {fruits.get('cerise')}")
    
    # clear() : vide le dictionnaire
    # fruits.clear()  # Attention, supprime tout !
    
    # copy() : crée une copie superficielle
    fruits_copy = fruits.copy()
    print(f"Copie créée : {len(fruits_copy)} fruits")
    
    # ============================================================
    # DICTIONNAIRE AVEC DIFFÉRENTS TYPES DE CLÉS
    # ============================================================
    print()
    print("=" * 50)
    print("CLÉS DE DIFFÉRENTS TYPES")
    print("=" * 50)
    
    # Les clés peuvent être str, int, tuple (mais PAS list ou dict !)
    personne = {
        "nom": "Dupont",
        "prenom": "Jean",
        42: "age",           # int comme clé
        ("ville", "code"): ("Paris", 75001)  # tuple comme clé
    }
    print(f"Dictionnaire mixte : {personne}")


if __name__ == "__main__":
    main()
