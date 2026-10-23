def salaire_mensuel(salaire_annuel):
    salaire_mensuel = int(salaire_annuel) / 12

    return salaire_mensuel

def salaire_hebdomadaire(salaire_mensuel):
    salaire_hebdomadaire = int(salaire_mensuel) / 4

    return salaire_hebdomadaire

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    salaire_horaire = int(salaire_hebdomadaire) / int(heures_travaillees)

    return round(salaire_horaire, 2)

salaire_annuel = input("Saisir salaire annuel : ")
heures_travaillees = input("Nombre heures travaillées (hebdo) : ")

salaire_mensuel = salaire_mensuel(salaire_annuel)
salaire_hebdomadaire = salaire_hebdomadaire(salaire_mensuel)

print(f"Votre salaire horaire est de {salaire_horaire(salaire_hebdomadaire, heures_travaillees)}€")
