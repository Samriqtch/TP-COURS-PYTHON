# Fonction pour calculer le factorielle 
# Ecrire une fonction qui te permet de calculer le factorielle d'un nombre entier positif n.
# Le factorielle d'un nombre n est le produit de tous les entiers positifs inférieurs ou égaux à n.
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)
resultat = factorielle(5)
print(factorielle(10))