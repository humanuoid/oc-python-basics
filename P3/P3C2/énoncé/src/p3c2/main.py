import requests
from bs4 import BeautifulSoup


with open("resources/index.html", "r") as file:
   soup = BeautifulSoup(file.read(), 'html.parser')

extract_products = soup.find_all("li")

products = []

for extract_product in extract_products:
   product = {}
   product['Nom du produit'] = extract_product.h2.string
   product['Prix en EUR'] = extract_product.select("p.price")[0].string.replace('Prix: ', '')
   price = round(float(product['Prix en EUR'].replace("€", "")) * 1.2)
   product['Prix en USD'] = f"${price}"
   product['Description'] = extract_product.select("p")[1].string.replace('Description : ', '')

   products.append(product)


print(products)
