def addition(a:float, b:float) -> float:
    return a + b

def soustraction(a:float, b:float) -> float:
    return a - b

def multiplication(a:float, b:float) -> float:
    return a * b

def division(a:float, b:float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        print("La division par zéro est impossible.")
