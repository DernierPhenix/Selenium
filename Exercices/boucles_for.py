# for x in serie:
    # code à répéter

# Écrire un programme qui affichera la table de pultiplication d'un nombre
# L'affichage doit contenir toutes les multiplications allant jusqu'à 10

nb = int(input("Entrer un nombre : "))

for i in range(0,11):
    print(f"{nb} * {i} = {nb*i}")