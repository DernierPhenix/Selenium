from calculatrice_correction import *


def test_Addition():
    assert addition(3,2) == 5
def test_Addition_Failed():
    assert addition(-9,2) == 0

def test_Soustraction():
    assert soustraction(7,8) == -1
def test_Soustraction_Failed():
    assert soustraction(13,2) == 0

def test_Multiplication():
    assert multiplication(10,2) == 20
def test_Multiplication_Failed():
    assert multiplication(2,2) == 5

def test_Division():
    assert division(18,2) == 9
def test_Division_Failed():
    assert division(14,2) == 7


# Pour tester un fichier python on le nomme avec le mot "test" devant son nom
# On importe le fichier à tester avec "from "nom_de_fichier" import *"
# On crée des fonctions et on utilise le mot "assert" et on vérifie un égalité par ex