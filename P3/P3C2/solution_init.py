"""
Package p3c2 - Exercice de web scraping avec BeautifulSoup.

Ce package extrait des informations de produits depuis un fichier HTML
et convertit les prix de EUR en USD.

Utilisation :
    from p3c2 import extraire_produits, convertir_prix
    # ou
    python -m p3c2.main
"""

__version__ = "0.1.0"
__author__ = "HuManuOïd"

# Liste des symboles exportés quand on fait "from p3c2 import *"
__all__ = [
    "main",
    "extraire_produits",
    "extraire_infos_page",
    "convertir_prix",
    "lire_html",
]

# Optionnel : ré-exporter les fonctions principales pour faciliter l'import
# from .main import (
#     main,
#     extraire_produits,
#     extraire_infos_page,
#     convertir_prix,
#     lire_html,
# )
