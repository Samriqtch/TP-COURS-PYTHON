def calculer_moy(liste):
    somme = 0
    nb_elements = 0
    for element in liste:
        somme += element
        nb_elements += 1
    return somme / nb_elements


liste = [1, 2, 3, 4, 5]

print(calculer_moy(liste))
