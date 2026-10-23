nombre1 = input("Entre ton premier: ")
nombre2 = input("Entre ton deuxième chiffre: ")

if nombre1.isnumeric() and nombre2.isnumeric():
    nombre1 = int(nombre1)
    nombre2 = int(nombre2)

    operation = input("Quel opération ? (+ / * -)")

    match operation:
        case "+":
            resultat = nombre1 + nombre2
        case "/":
            if nombre2 != 0:
                resultat = round(nombre1 / nombre2)
            else:
                raise SystemExit("On peut pas diviser par 0 abruti !")
        case "*":
            resultat = nombre1 * nombre2
        case "-":
            resultat = nombre1 - nombre2
        case _:
            raise SystemExit("Opérateur inconnu, dommage !")

    print(f"resultat : {resultat}")
else:
    raise SystemExit("Fin du programme")
