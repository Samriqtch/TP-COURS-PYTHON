# Une fonction qui permet de vérifier si un nombre est premier ou non
def est_premier(N):
    if N < 2:
        return False
    for i in range(2, int(N**0.5) + 1):
        if N % i == 0:
            return False
    return True

# Validation de l'entrée utilisateur
try:
    N = int(input("Veuillez entrer un nombre : "))
    resultat = est_premier(N)
    if resultat:
        print(f"{N} est un nombre premier.")
    else:
        print(f"{N} n'est pas un nombre premier.")
except ValueError:
    print("Veuillez entrer un nombre entier valide.")