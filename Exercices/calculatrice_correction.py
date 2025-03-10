from math import sqrt
 
def addition(a, b):
    return a + b
 
def soustraction(a, b):
    return a - b
 
def multiplication(a, b):
    return a * b
 
def division(a, b):
    if b == 0:
        raise ValueError("Impossible de diviser par zéro !")
    return a / b
 
def racine_carree(a: float) -> float:
    return sqrt(a)