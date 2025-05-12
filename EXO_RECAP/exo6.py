# Demander à l'utilisateur le nombre de lignes à afficher
n = int(input("Veuillez entrer le nombre de lignes du triangle de Pascal à afficher : "))

triangle = []
for i in range(n):
    
    ligne = [1]
    if i > 0:
      
        for j in range(1, i):
            ligne.append(triangle[i-1][j-1] + triangle[i-1][j])
        ligne.append(1)
    triangle.append(ligne)
print("Triangle de Pascal :")
for ligne in triangle:
    print(ligne)