# Fonction pour calculer la moyenne des éléments d'une liste
def calculer_moyenne(liste):
    if not liste:  # Vérifie si la liste est vide
        return 0
    return sum(liste) / len(liste)

# Fonction pour valider et convertir une entrée utilisateur en liste de nombres
def convertir_en_liste(entree):
    liste = entree.split()  # Divise la chaîne en une liste
    for element in liste:
        if not element.replace('.', '', 1).isdigit():  # Vérifie si chaque élément est un nombre
            print(f"'{element}' n'est pas un nombre valide.")
            return None
    return [float(x) for x in liste]  # Convertit les éléments en float

# Programme principal
entree = input("Veuillez entrer une liste de nombres séparés par des espaces : ")
liste = convertir_en_liste(entree)



def calculer_moyenne_sans_sum_len_sans_verif(liste):
    somme = 0
    nb_elements = 0
    for element in liste:
        somme += element
        nb_elements += 1
    return somme / nb_elements


