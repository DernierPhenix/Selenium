from math import sqrt

# age = nbr2nbr1

# result = sqrt(age)
# print("le resultat : {}".format(result))

# Créer un programme qui représente une calculatrice et qui fera une addition, soustraction, 
# multiplication, division et la racine carrée
# Éxécuter le programme dans un fichier différent de celui dans lequel il est codé
nbr1 = int(input ("Entrer le 1er nombre : "))
nbr2 = int(input("Entrer le 2ème nombre : "))


def addition(nbr1, nbr2):
    print(f"J'additionne' {nbr1} à {nbr2}.")
    #resultat = nb1 - nbr2
    return nbr1 + nbr2

resultat = addition(nbr1, nbr2)
print(resultat)

def soustraction(nbr1, nbr2):
    print(f"Je soustrais {nbr1} à {nbr2}.")
    #resultat = nb1 - nbr2
    return nbr1 - nbr2

resultat = soustraction(nbr1, nbr2)
print(resultat)

def multiplication(nbr1, nbr2):
    print(f"Je multiplie {nbr1} à {nbr2}.")
    #resultat = nb1 - nbr2
    return nbr1 * nbr2

resultat = multiplication(nbr1, nbr2)
print(resultat)

def division(nbr1, nbr2):
    print(f"Je divise {nbr1} à {nbr2}.")
    #resultat = nb1 - nbr2
    return nbr1 / nbr2

resultat = division(nbr1, nbr2)
print(resultat)

def racine(nbr1):
    print(f"la racine carrrée de  {nbr1}")
    #resultat = nb1 - nbr2
    return nbr1 

resultat = sqrt(racine (nbr1))
print(resultat)