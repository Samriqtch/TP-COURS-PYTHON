#Exercice 1
# Un algo qui permet de calculer la surface et la circonférence d'un cercle
# et l utilisateur doit saisir le rayon
"""
print("Bonjour et bienvenue dans notre programme!")
S = float
C = float
Pi = 3.14
R = float(input("Veuillez entrer un rayon : "))
C = 2*Pi*R
S = Pi*pow(R,2)
print("La circonference de votre cercle est : ",round(C,2))
print("la surface de votre cercle est : ",round(S,2))
"""
#Exercice 2
# Algorithme qui demande à un user de saisir un temps en secnde
# et affiche ce temps en valeur de jours heures, minutes et secondes
"""
print("Bienvenu dans mon programme")
T = int(input("Veuillez entrer un temps en seconde"))
Jour = T//86400
Reste = T%86400
Heure = Reste/3600
Reste2 = Reste%3600
Min = Reste2//60
Sec = Reste2%60

print("Votre temps saisi correspont à",round(Jour,0)," Jours ",round(Heure,0)," Heure ",round(Min,0)," min ",Sec," Seconde ")
"""
#Exercice 3
#Un programme qui demande a l'utilisateur son age et affiche son année de naissance

print("Bienvenue dans le programme qui calcule votre annee de naissance")
Age = int(input("Veuillez me donner votre age: "))

Annee_Naiss = 2025-Age

print("Ah vous êtes donc né en : ",Annee_Naiss," Ravie de le savoir !")