fruits = {"pomme":"verte", "banane":"jaune", "orange":"orange"}

print(fruits.items())

fruits["kiwi"] = "vert"

print(fruits.items())

banana_color = fruits.get("banane")

print(banana_color)

fruits["pomme"] = "vert"

print(fruits.items())

del fruits["banane"]

print(fruits.items())
print(fruits.keys())
