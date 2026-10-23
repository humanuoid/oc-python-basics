"""
Manipulation de listes en Python.

Ce programme démontre les opérations de base sur les listes :
création, ajout, suppression, modification, longueur et tri.
"""


def afficher_liste(fruits: list, message: str) -> None:
    """
    Affiche une liste avec un message descriptif.
    
    Args:
        fruits: La liste à afficher
        message: Message à afficher avant la liste
    """
    print(f"{message}")
    print(f"  Liste : {fruits}")
    print(f"  Longueur : {len(fruits)} éléments")
    print()


def main():
    """Fonction principale du programme."""
    print("=" * 50)
    print("MANIPULATION DE LISTES - DÉMONSTRATION")
    print("=" * 50)
    print()
    
    # ============================================================
    # ÉTAPE 1 : CRÉATION DE LA LISTE
    # ============================================================
    # Une liste est une collection ordonnée et modifiable
    # Les index commencent à 0 (pas à 1 !)
    fruits = ["pomme", "banane", "orange"]
    afficher_liste(fruits, "1. Création de la liste initiale :")
    
    # ============================================================
    # ÉTAPE 2 : AJOUT D'UN ÉLÉMENT (append)
    # ============================================================
    # append() ajoute un élément à la FIN de la liste
    fruits.append("kiwi")
    afficher_liste(fruits, "2. Après ajout de 'kiwi' (append) :")
    
    # ============================================================
    # ÉTAPE 3 : SUPPRESSION D'UN ÉLÉMENT (remove)
    # ============================================================
    # remove() supprime la PREMIÈRE occurrence de la valeur
    # Vérification préalable pour éviter les erreurs
    fruit_a_supprimer = "orange"
    if fruit_a_supprimer in fruits:
        fruits.remove(fruit_a_supprimer)
        afficher_liste(fruits, f"3. Après suppression de '{fruit_a_supprimer}' (remove) :")
    else:
        print(f"'{fruit_a_supprimer}' n'est pas dans la liste !")
    
    # ============================================================
    # ÉTAPE 4 : MODIFICATION D'UN ÉLÉMENT PAR INDEX
    # ============================================================
    # Les index commencent à 0 : fruits[0] = "pomme"
    # fruits[1] = deuxième élément = "banane"
    index_a_modifier = 1
    ancienne_valeur = fruits[index_a_modifier]
    nouvelle_valeur = "ananas"
    fruits[index_a_modifier] = nouvelle_valeur
    print(f"4. Modification de l'index {index_a_modifier} :")
    print(f"   '{ancienne_valeur}' -> '{nouvelle_valeur}'")
    afficher_liste(fruits, "   Résultat :")
    
    # ============================================================
    # ÉTAPE 5 : OBTENIR LA LONGUEUR (len)
    # ============================================================
    # len() retourne le nombre d'éléments dans la liste
    nombre_fruits = len(fruits)
    print(f"5. Longueur de la liste (len) : {nombre_fruits} éléments")
    print()
    
    # ============================================================
    # ÉTAPE 6 : TRI DE LA LISTE (sort)
    # ============================================================
    # sort() modifie la liste EN PLACE (elle est modifiée directement)
    # Pour une copie triée sans modifier l'originale : sorted(fruits)
    print("6. Avant tri :", fruits)
    fruits.sort()  # Tri alphabétique croissant
    print("   Après tri (sort) :", fruits)
    print()
    
    # ============================================================
    # RÉSULTAT FINAL
    # ============================================================
    afficher_liste(fruits, "RÉSULTAT FINAL :")
    
    # ============================================================
    # MÉTHODES UTILES SUPPLÉMENTAIRES
    # ============================================================
    print("=" * 50)
    print("AUTRES MÉTHODES UTILES")
    print("=" * 50)
    
    # insert() : insère à un index précis
    fruits.insert(0, "fraise")
    print(f"insert(0, 'fraise') : {fruits}")
    fruits.remove("fraise")  # On enlève pour la suite
    
    # pop() : supprime et retourne le dernier élément
    dernier = fruits.pop()
    print(f"pop() retourne '{dernier}' : {fruits}")
    fruits.append(dernier)  # On remet
    
    # index() : trouve l'index d'une valeur
    pos = fruits.index("ananas")
    print(f"index('ananas') = {pos}")
    
    # count() : compte les occurrences
    print(f"count('pomme') = {fruits.count('pomme')}")
    
    # reverse() : inverse l'ordre
    fruits_copy = fruits.copy()
    fruits_copy.reverse()
    print(f"reverse() : {fruits_copy}")
    
    # sorted() : retourne une nouvelle liste triée
    fruits_trie = sorted(fruits, reverse=True)  # Ordre décroissant
    print(f"sorted(reverse=True) : {fruits_trie}")


if __name__ == "__main__":
    main()
