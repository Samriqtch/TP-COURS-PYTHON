#Exercice 1
#un programme qui declare trois variables , un entier , un flottant , une chaine de caractere
# et affiche ses variables ainsi que leur type

"""
P = 34
F = 32.658
C = "Samson"

print("Bienvenu dans le progremme")
print("le type de vos variables sont")
print(" la variable P est de type",type(P)," F est de type ",type(F)," C est de type ",type(C))

"""
#Exo 2
#un programme qui creer une liste contenant au moins 5 élément s de votre chois et ajouter un nouvel élément
# un nouvel élément à la liste et affichez les

"""
New_List = [2,5,6,8] # definition d'un tableau 
New_List.append(52) # Ajout d'un nouveau élément dans le tableau 

print(New_List)

"""

#Exo 3
#Declaration dun tuple contenant trois valeurs differentes et
# essayer de modifier l'un des éléments ensuite observer et expliquer le resusltat

"""
New_tuple = (11,25,56)
#reconversion du tuple en liste
New_list = list(New_tuple)
New_list[2]=52 # modification de la valeur à la position 2 
New_tuple = tuple(New_list) #reconversion de la liste en tuple

print(New_tuple) # Affichage de la nouvelle tuple

"""
#Exo 4
# Créer un dictionnaire representant une personne avec les clés nom , age et ville;
# modifier la valeur associé à la clé ville et afficher le dictionnaire mise à jour

"""
Pers = { "nom":"Samson","age":24,"ville":"Lomé"} # definition d'un dictionnaire
print("Voici les valeurs du dictionnaire creer : ")
print(Pers)
#modification
Pers["ville"]="Kara" # pour modifier les valeurs d'un clé d'un dictionnaire 
print(" Les nouvelles valeurs du dictionnaires sont :")
print(Pers)

"""
#Exo5
# un programme qui demande à un utilisatue son prenom et son age
# puis affiche une phrase contenant ces informations

"""
print("Bonjour et bienvenu dans le programme info")

Prenom = str(input("Veuillez entrer votre prenom svp : "))

Age = int(input(" Veuillez maintenant saisir votre age : "))

print("Ravie de te rencontrer "+Prenom+" j'espère que tu vas bien, je vois que tu as :",Age," ans, c est bien")

"""

#Exo6
# déclarez deux nombre et appliquer sur eux toutes les opérations arithmétiques vues dans cet atelier
#afficher ensuite les resultat
"""
Nb = 56
Nb2 = 34

Add = Nb + Nb2 # operation d'addition
Sous = Nb - Nb2 # operation de soustraction
Multi = Nb * Nb2 # Operation de multiplication
Div = Nb / Nb2 # operation de division
Div_Ent = Nb // Nb2 # pour afficher la division entiere
Mod = Nb % Nb2 # pour afficher le reste d'un division
Expo = Nb ** Nb2

print("Voici les resulats de toutes les opearations arithmetique :")
print(Add)
print(Sous)
print(Multi)
print(Div)
print(Div_Ent)
print(Mod)
print(Expo)

"""
#Exo7
# expérimentez avec les operations logiques and, or et not
# en declarant des variables booléennes et en affichant le resultat des expressions logique

Bi = 0
Bo = 1
print(Bi and Bo)
print(Bi or Bo)
print(not Bo) # affiche false

#Exo 8
#Effectuer différentes conversion de type :
# convertisseer un entier en chaine , une chaine en flottant et une liste en tuple
# ensuite afficher le resultat après la conversion
 
Ent = 200
Chai = " Samson "
Lis = [23,25,58,89]
Tup = (12,25,54)
print(Ent)
print(Chai)
print(Lis)
print(Tup)

# conversion et affichage

Ent = str(Ent)

print (Ent)

