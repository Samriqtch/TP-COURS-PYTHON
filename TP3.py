import random 

## Calculatrice simple
## exemple 
"""
nbr1 = float(input("Veuillez entrer un nombre :"))
nbr2 = float(input("Veuillez entrer le deuxieme nombre : "))
operation = input("Quel type d operation souhaiter vous faire : (+, - , / , *) ")

if operation == "+" :
    resultat = nbr1 + nbr2
elif operation == "-" :
    resultat = nbr1 - nbr2
elif operation == "*":
    resultat = nbr1 * nbr2
elif operation == "/":
    if nbr2 != 0 :
        resultat = nbr1 / nbr2
    else :
        resultat = " Erreur,impossible de diviser par zero "
else :
    resulat  = "operation non reconnue "
    
print(f"resultat : {resultat}")
"""


#Exercice pratiques
#Exo1
# un programme qui demande a l utilisateur de saisir un nombre et affiche si le nombre est pair ou impair

"""

print("Voici un programme une verifie si un nombre est pair ou impair")
nombre = int(input("Veuillez entrer un nombre pour la verification: "))

if nombre%2 == 0 :
    resultat = " le nombre est pair"
else :
    resultat = " le nombre est impair"
print(f"Votre nombre : {resultat}")

"""
#Exo2
# un programme qui demande à utilisateur son age et affiche si vos etes mineur makeur ou senior
"""
print("Bienvenue dans le programme  de validation d age ")

Age = int(input("Quel est votre age svp ? :"))

if Age < 18:
    resultat = " Ah, vous êtes encore un mineur"
elif Age > 18 and Age < 65 :
    resultat = " Ah , Vous êtes majeur, vous grandissez c est bien"
elif Age > 65  :
    resultat  = " Wep ,vous êtes un senior , un vieux mogo haha"
print(f"Mon programme vous dit  : {resultat}")
"""

#Exo3
# un programme  qui dmande à un user de saisir une note entre 0 et 20 et affiche sa mention
"""
print("Programme de calcul de note")
note = int(input("Quel est votre note : "))

while True :
    note = 0
    note = int(input("Veuillez refaire la saisie : "))
    if note >=0 and note < 20 :
        break
    print("Votre nombre n'est pas correcte ")

if note < 10 :
    resultat = " Echec"
elif note >= 10 and note < 12 :
    resultat = "Passable "
elif note >= 12 and note < 14 :
    resultat  = "Assez bien"
elif note >= 14 and note < 16 :
    resultat = " Bien"
elif note >= 16 and note < 20 :
    resultat = " Tres bien "
print(f" Votre note est un : {resultat}")
"""
#Exo 4
# Jeu de devinette
# un programme qui génère un nombre aléatoire entre 1 et 10 et demande à lutilisateur de deviner ce nombre le programme doit afficher
# soit trop bas soit trop haut soit bravo sgnifiant qu'il a trouver
#random.randint permet de génerer des nombres aleatoire

print("Bienvenue dans ce programme de devinette ")
print(" Ce programme est un programme qui génerer des nombre entier entre 1 et 10")
print(" Je vais donc vous demandez le nombre choisi ")

nbre = random.randint(1,10)

ale = nbre

choix = int(input(" Alors quel est votre choix : "))

while choix != ale :
    if choix < ale :
        resultat = " Trop bas "
        print(resultat)
        choix  = int(input("Veuillez refaire un autre choix : "))
        
    else :
        resultat = " Trop haut "
        print(resultat)
        choix  = int(input("Veuillez refaire un autre choix : "))
         
resultat = " Bravo"
print(resultat) 

