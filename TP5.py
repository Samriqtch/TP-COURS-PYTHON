# Creation et acces a une liste
"""
fruits = ["pomme","banane","cerise"]
print(fruits[1]) # Affiche banane qui est la position 1 selon / 0 1 2
"""
# Modification d une liste
"""
fruits = ["Pomme","banane","cerise"]
fruits[1] = "Kiwi"
print(fruits) # Affiche pomme kiwi la nouvelle valeur et ensuite cerise
"""
#Ajout d un nouvel element dana la liste
"""
fruits = ["pomme","cerise","banane"]
fruits.append("orange")
print(fruits)
"""
#Suppresion d'element
"""
fruits = ["pomme","banane","cerise"]
fruits.remove("banane")
print(fruits)  # affiche pomme et cerise et donne aussi dans l affiche une idee de la position qui a ete supprimer
"""

# Parcourir une liste avec une boucle for
"""
fruits = ["samson","beau","vilain"]
for fruit in fruits: # fruit ici est un indice
    print(fruit)
"""    
# Utilisation de len et de sort
"""
nombres = [1,2,5,8,7]
print(len(nombres))
nombres.sort()
print(nombres)
"""

# EXERCICE PRATIQUES

#Somme des elements d une liste

"""
compteur = 0
vil = [1,5,45,85]
for il in vil:
    compteur+=il
print(compteur)
"""

# Recherche dun element
"""
kel = [2,5,8,45,562,32,78,785]
ju = int(input("Veuillez saisir un nombre: "))

if ju in kel:
    print(ju," Votre nombre se trouve dans la liste")
else:
    print("Votre element n est pas dans la liste")

"""

#Suppresion des doublons

"""
kel = ["bi","bi","ba","bp","bp","bp","bx","bi","bi","bi"]

kel_sans = list(set(kel))
print(f"Liste sans doublons: {kel_sans}")
"""

# Fusion de deux listes
"""
sam = [2,5,8,87]
son = [52,63,89,9]
new_samson = sam + son
print(new_samson)
"""

#inversion d une liste
"""
sam = [2,5,8,87]
sam.reverse()
print(sam)

"""
""" """
#Liste de listes  matrice
"""
kel = [2,5,78,9,3,5,9,3,5]
matrice = [kel[i:i+3] for i in range(0, len(kel), 3)]
for ligne in matrice:
    print(ligne)
"""
def recherche_element():
    kel = [2, 5, 8, 45, 562, 32, 78, 785]
    ju = int(input("Veuillez saisir un nombre : "))
    if ju in kel:
        print(f"{ju} se trouve dans la liste.")
    else:
        print(f"{ju} ne se trouve pas dans la liste.")
recherche_element()

