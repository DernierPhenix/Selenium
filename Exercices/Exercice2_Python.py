# Faire le même exercice que le 1er mais le faire avec une fonction
# Créer un programme qui demande un prénom et un age et envoie des réponses souhaitées.
# Faire le calcul pour savoir combien d'années il faut pour atteindre 100 ans
# mettre un message d'erreur si l'age entrée n'est pas un nombre


# age = int(input("Quel est ton âge ? : "))
# 


def verification(prenom : str, age : int):
    age_restant = 100 - age
    if age < 18 :
        print(f"Tu es encore un padawan, {prenom} ! Il te reste {age_restant} ans avant d'avoir 100 ans")
    elif age < 40 :
        print(f"Tu es encore un padawan, {prenom} ! Il te reste {age_restant} ans avant d'avoir 100 ans")
    elif age <= 60 :
        print(f"Tu es encore un padawan, {prenom} ! Il te reste {age_restant} ans avant d'avoir 100 ans")
    else:
        print(f"Tu es encore un padawan, {prenom} ! Il te reste {age_restant} ans avant d'avoir 100 ans")
        
    return prenom, age

prenom = str(input("Quel est ton prénom ? : ")) 
   
try :
    age = int(input("Quel est ton âge ? : "))
    resultat = verification(prenom,age)
    print(resultat)
except:
    print("Il faut saisir un nombre!")



    

    

    






