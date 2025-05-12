# Programme principal

# Demander un entier à l'utilisateur
nombre = int(input("Veuillez entrer un entier : "))

# Vérification pair ou impair
if nombre % 2 == 0:
    print(f"{nombre} est pair.")
else:
    print(f"{nombre} est impair.")

# Vérification des multiples de 3, 5 ou 7
multiples = []
for diviseur in [3, 5, 7]:
    if nombre % diviseur == 0:
        multiples.append(diviseur)

if multiples:
    print(f"{nombre} est multiple de {', '.join(map(str, multiples))}.")
else:
    print(f"{nombre} n'est pas multiple de 3, 5 ou 7.")

# Vérification si le nombre est premier
if nombre < 2:
    print(f"{nombre} n'est pas un nombre premier.")
else:
    est_premier = True
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            est_premier = False
            break
    if est_premier:
        print(f"{nombre} est un nombre premier.")
    else:
        print(f"{nombre} n'est pas un nombre premier.")