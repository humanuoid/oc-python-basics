"""
Module principal - Extraction de produits depuis un fichier HTML.

Ce programme utilise BeautifulSoup pour parser un fichier HTML local,
extraire les informations des produits (nom, prix, description),
et convertir les prix de euros en dollars.

Structure du projet (créée avec uv) :
    p3c2/
    ├── pyproject.toml
    ├── resources/
    │   └── index.html
    └── src/
        └── p3c2/
            ├── __init__.py
            └── main.py (ce fichier)

Note sur le chemin du fichier HTML :
    On utilise une fonction pour trouver la racine du projet (où se trouve
    pyproject.toml) plutôt qu'un nombre fixe de .parent — c'est plus robuste
    si on déplace le fichier dans l'arborescence.
"""

from pathlib import Path
from typing import Optional

from bs4 import BeautifulSoup, Tag

# ============================================================
# CONSTANTES
# ============================================================
TAUX_CONVERSION_EUR_USD = 1.2  # Taux de change (simplifié)


def trouver_racine_projet(marqueur: str = "pyproject.toml") -> Path:
    """
    Trouve la racine du projet en remontant les dossiers.
    
    Cherche un fichier marqueur (pyproject.toml par défaut) en partant
    du répertoire de ce fichier et en remontant jusqu'à le trouver.
    
    Args:
        marqueur: Nom du fichier qui marque la racine du projet
        
    Returns:
        Chemin absolu vers la racine du projet
        
    Raises:
        FileNotFoundError: Si le marqueur n'est pas trouvé
        
    Examples:
        >>> racine = trouver_racine_projet()
        >>> (racine / "resources" / "index.html").exists()
        True
    """
    courant = Path(__file__).resolve().parent
    
    # Remonte jusqu'à trouver le marqueur ou atteindre la racine système
    for _ in range(20):  # Limite de sécurité
        if (courant / marqueur).exists():
            return courant
        if courant.parent == courant:  # Racine système atteinte
            break
        courant = courant.parent
    
    raise FileNotFoundError(
        f"Impossible de trouver la racine du projet (marqueur '{marqueur}' non trouvé). "
        f"Vérifie que tu lances le script depuis le projet."
    )


# Chemin vers le fichier HTML (robuste, trouve la racine du projet)
try:
    RACINE_PROJET = trouver_racine_projet()
    FICHIER_HTML = RACINE_PROJET / "resources" / "index.html"
except FileNotFoundError:
    # Fallback : chemin relatif au cwd (si lancé depuis la racine)
    FICHIER_HTML = Path("resources/index.html")


# ============================================================
# FONCTIONS UTILITAIRES
# ============================================================
def nettoyer_texte(texte: Optional[str], a_supprimer: str = "") -> str:
    """
    Nettoie un texte extrait du HTML.
    
    Args:
        texte: Le texte à nettoyer (peut être None)
        a_supprimer: Chaîne à supprimer du texte
        
    Returns:
        Le texte nettoyé, ou chaîne vide si None
        
    Examples:
        >>> nettoyer_texte("  Prix: 10€  ", "Prix:")
        '10€'
        >>> nettoyer_texte(None)
        ''
    """
    if texte is None:
        return ""
    texte = texte.strip()
    if a_supprimer:
        texte = texte.replace(a_supprimer, "")
    return texte.strip()


def extraire_prix_eur(element: Tag) -> Optional[float]:
    """
    Extrait et convertit le prix en euros depuis un élément HTML.
    
    Args:
        element: L'élément <li> contenant le produit
        
    Returns:
        Le prix en float, ou None si non trouvé ou invalide
        
    Examples:
        >>> # Avec <p class="price">Prix: 10€</p>
        >>> extraire_prix_eur(element)
        10.0
    """
    price_tag = element.select_one("p.price")
    if not price_tag or not price_tag.string:
        return None
    
    # Nettoie et convertit : "Prix: 10€" -> 10.0
    prix_str = nettoyer_texte(price_tag.string, "Prix:")
    prix_str = prix_str.replace("€", "").strip()
    
    try:
        return float(prix_str)
    except ValueError:
        return None


def convertir_prix(prix_eur: float, taux: float = TAUX_CONVERSION_EUR_USD) -> int:
    """
    Convertit un prix de EUR en USD.
    
    Args:
        prix_eur: Prix en euros
        taux: Taux de conversion (défaut: 1.2)
        
    Returns:
        Prix en dollars, arrondi à l'entier
        
    Examples:
        >>> convertir_prix(10)
        12
        >>> convertir_prix(20.5)
        25
        >>> convertir_prix(10, taux=1.5)
        15
    """
    return round(prix_eur * taux)


# ============================================================
# FONCTIONS D'EXTRACTION
# ============================================================
def extraire_infos_page(soup: BeautifulSoup) -> dict:
    """
    Extrait les informations générales de la page (titre, h1).
    
    Args:
        soup: L'objet BeautifulSoup contenant le HTML parsé
        
    Returns:
        Dictionnaire avec les clés 'titre_page' et 'titre_h1'
    """
    infos = {}
    
    # Titre de la page (<title>)
    if soup.title and soup.title.string:
        infos["titre_page"] = nettoyer_texte(soup.title.string)
    
    # Texte du premier h1
    h1 = soup.find("h1")
    if h1 and h1.string:
        infos["titre_h1"] = nettoyer_texte(h1.string)
    
    return infos


def extraire_produits(soup: BeautifulSoup) -> list[dict]:
    """
    Extrait tous les produits du HTML parsé.
    
    Args:
        soup: L'objet BeautifulSoup contenant le HTML parsé
        
    Returns:
        Liste de dictionnaires contenant les infos de chaque produit
        
    Structure d'un produit :
        {
            "nom": str,
            "prix_eur": str,    # Ex: "10€"
            "prix_usd": str,    # Ex: "$12"
            "description": str
        }
    """
    products = []
    
    # Sélectionne uniquement les <li> avec class "product" (plus précis)
    product_elements = soup.select("li.product")
    
    # Fallback : tous les <li> s'il n'y a pas de class "product"
    if not product_elements:
        product_elements = soup.find_all("li")
    
    for element in product_elements:
        # --- Extraction du nom (h2) ---
        h2 = element.find("h2")
        nom = nettoyer_texte(h2.string) if h2 else "Nom inconnu"
        
        # --- Extraction du prix ---
        prix_eur = extraire_prix_eur(element)
        prix_eur_str = f"{prix_eur}€" if prix_eur is not None else "Prix inconnu"
        
        # --- Conversion en USD ---
        if prix_eur is not None:
            prix_usd = convertir_prix(prix_eur)
            prix_usd_str = f"${prix_usd}"
        else:
            prix_usd_str = "N/A"
        
        # --- Extraction de la description ---
        # La description est généralement le dernier <p>
        paragraphs = element.find_all("p")
        description = ""
        if len(paragraphs) >= 2:
            # Dernier paragraphe = description
            description = nettoyer_texte(paragraphs[-1].string, "Description :")
        elif paragraphs:
            # Un seul paragraphe
            description = nettoyer_texte(paragraphs[0].string)
        
        # --- Création du dictionnaire produit ---
        product = {
            "nom": nom,
            "prix_eur": prix_eur_str,
            "prix_usd": prix_usd_str,
            "description": description,
        }
        
        products.append(product)
    
    return products


def lire_html(chemin: Path) -> Optional[BeautifulSoup]:
    """
    Lit un fichier HTML et retourne l'objet BeautifulSoup.
    
    Args:
        chemin: Chemin vers le fichier HTML
        
    Returns:
        Objet BeautifulSoup, ou None si erreur
    """
    try:
        with open(chemin, "r", encoding="utf-8") as file:
            contenu = file.read()
        return BeautifulSoup(contenu, "html.parser")
    except FileNotFoundError:
        print(f"❌ Erreur : le fichier '{chemin}' n'existe pas.")
        print(f"   Chemin recherché : {chemin.absolute()}")
        return None
    except PermissionError:
        print(f"❌ Erreur : permission refusée pour '{chemin}'.")
        return None
    except Exception as e:
        print(f"❌ Erreur lors de la lecture du fichier : {e}")
        return None


# ============================================================
# FONCTION D'AFFICHAGE
# ============================================================
def afficher_resultats(products: list[dict], infos_page: dict) -> None:
    """
    Affiche les résultats de l'extraction de manière formatée.
    
    Args:
        products: Liste des produits extraits
        infos_page: Informations générales de la page
    """
    # En-tête
    print("=" * 60)
    print("🔍 RÉSULTATS DE L'EXTRACTION")
    print("=" * 60)
    
    # Informations de la page
    print("\n📄 Informations de la page :")
    for cle, valeur in infos_page.items():
        print(f"   {cle}: {valeur}")
    
    # Produits
    print(f"\n📦 Produits trouvés : {len(products)}")
    print("-" * 60)
    
    for i, product in enumerate(products, 1):
        print(f"\n  Produit #{i}")
        print(f"    Nom         : {product['nom']}")
        print(f"    Prix (EUR)  : {product['prix_eur']}")
        print(f"    Prix (USD)  : {product['prix_usd']}")
        
        # Description tronquée si trop longue
        desc = product['description']
        if len(desc) > 60:
            desc = desc[:57] + "..."
        print(f"    Description : {desc}")
    
    print("\n" + "=" * 60)


# ============================================================
# FONCTION PRINCIPALE
# ============================================================
def main() -> None:
    """
    Fonction principale du programme.
    
    Lit le fichier HTML, extrait les produits et affiche les résultats.
    """
    print("🚀 Démarrage de l'extraction HTML...")
    print(f"📁 Fichier source : {FICHIER_HTML.name}")
    print()
    
    # Vérification que le fichier existe
    if not FICHIER_HTML.exists():
        print(f"❌ Erreur : le fichier '{FICHIER_HTML}' n'existe pas.")
        print(f"   Chemin absolu : {FICHIER_HTML.absolute()}")
        print("\n💡 Assure-toi de lancer le script depuis le bon répertoire,")
        print("   ou vérifie que le fichier resources/index.html existe.")
        raise SystemExit(1)
    
    # Lecture et parsing du HTML
    soup = lire_html(FICHIER_HTML)
    if soup is None:
        raise SystemExit("❌ Impossible de parser le fichier HTML.")
    
    # Extraction des données
    print("⚙️  Extraction en cours...")
    infos_page = extraire_infos_page(soup)
    products = extraire_produits(soup)
    
    # Affichage des résultats
    afficher_resultats(products, infos_page)
    
    print("\n✅ Extraction terminée avec succès !")


if __name__ == "__main__":
    main()
