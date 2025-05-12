# Demander un entier strictement positif
n = -1  # Initialisation avec une valeur négative pour entrer dans la boucle
while n <= 0:
    entree = input("Veuillez entrer un entier strictement positif : ")
    if entree.isdigit():  # Vérifie si l'entrée est un entier positif
        n = int(entree)
        if n <= 0:
            print("Le nombre doit être strictement positif.")
    else:
        print("Veuillez entrer un entier valide.")

# Afficher les termes de la suite de Syracuse
print(f"Suite de Syracuse pour n = {n} :")
while n != 1:
    print(n, end=" -> ")
    if n % 2 == 0:  # Si n est pair
        n = n // 2
    else:  # Si n est impair
        n = 3 * n + 1
print(n)  # Affiche le dernier terme (1)