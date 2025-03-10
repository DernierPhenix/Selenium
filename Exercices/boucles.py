# En se basant sur les exos 1-2, ajouter dans le programme une commande qui permet de relancer 
# la question sur l'âge tant  que l'utilisateur ne fournit pas un nombre

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

age_non_defini = True #on definit une variable à True

while age_non_defini:
    try :
        age = int(input("Quel est ton âge ? : ")) #age est un integer et on pose la question

        age_non_defini = False #Si age_non_défini est à false alors on va vers except

        resultat = verification(prenom,age)
        print(resultat)

    except:
        print("Il faut saisir un nombre!")



