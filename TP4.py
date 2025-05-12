import random
# boucle for avec range ()
"""
for i in range(5):
    print("iteration : ",i)
"""
# boucle for sur une liste
"""
fruits = ["pomme", "banane", "cerise"]
for fruit  in fruits:
     print(fruit)
"""
# boucle while simple
"""
compteur = 0
while compteur < 5:
    print("Compteur :",compteur)
    compteur += 1
"""
# boucle while avec break

"""
while True:
    reponse = input("Entrez 'quit' pour quitter ")
    if reponse == "quit":
        break
    print("vous avez entre : ",reponse)
"""
    
# boucle for avec continue
"""
for i in range (10):
    if i % 2 == 0:
        continue # passe à l'iteration suivante si i est pair
    print("Nombre impair : ",i)
"""
#####################################################################
    
#Exercice pratiques
#Exo 1

# un programme qui calcule la somme de nombre de 1 à 100

"""
compteur = 0
for i in range(101):
    compteur +=i
print("La somme des nombre de 1 a 100 = ",compteur)
"""
#  Exo2 Table de multiplication
#un programme qui demande a luser de saisir un nombre et affiche sa table de multiplication
"""
print("Table de multiplication")
nbre = int(input("Veuillez saisir un nombre "))
for i in range(12):
    resultat = 12*i
    print("12*",i,"= ",resultat)
 """   
#Exo 3 Jeu de devinette

"""
print("DEVINETTE!! NETTE")
nbre = random.randint(1,100)

ale = nbre

choix = int(input("Quel est votre choix: "))
while choix != ale:
    if choix < ale:
        print("Trop bas")
        choix  = int(input("Veuillez refaire un autre choix : "))
        
    else :
        print("Trop haut")
        choix  = int(input("Veuillez refaire un autre choix : "))
        
print("Bravo vous avez trouver !")

"""
# Nombre premier
#un programme qui demande a l user de saisir un nombre et verifie si ce nmbre est premier
"""
print("Trouver un nombre premier ")
nbre = int(input("Veuillez entrer un nombre : "))

if nbre < 2:
    print(f"{nbre} n'est pas un nombre premier.")
else:
    est_premier = True
    # Vérifie les diviseurs entre 2 et la racine carrée du nombre
    for i in range(2, int(nbre ** 0.5) + 1):
        if nbre % i == 0:
            est_premier = False
            break

    # Résultat
    if est_premier:
        print(f"{nbre} est un nombre premier.")
    else:
        print(f"{nbre} n'est pas un nombre premier.")
"""
#Exo 5 Boucle while avec validation
# un programme qui demande a user de saisir un mot de passe
# si il est correcte le programme affiche Autorise et s'arrete au cas contraire il continue
"""
print("PROGRAMME MOT DE PASSE")

while True:
    MP = input("Veuillez entrer votre mot de passe : ")
    if MP == "samson":
        break
    print("Mot de passe incorrecte")

print("Acces autorise")
"""
#Exo 6 Fizz buzz

# un programme qui affiche les nombres de 1 à 100

for i in range(100) :
    if i%3 == 0  and i%5  == 0 :
        print("FizzBuzz")
    if i%3 == 0 :
        print("Fizz")
    if i%5 == 0:
        print("Buzz")

           