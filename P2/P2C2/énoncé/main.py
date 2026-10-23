nombres = input("Saisir nombres séparés par une virgule: ")

nombres_list = nombres.split(",")

resultat = 0

for nombre in nombres_list:
    resultat += int(nombre)

print(resultat)

avg = round(resultat / len(nombres_list))

print(avg)

count_avg = 0

for nombre in nombres_list:
    if int(nombre) > avg:
        count_avg += 1

print(count_avg)
