inventaire = {}


def ajouterunproduit():
    def ajouter_produit(nom,quantite):
        inventaire[nom] = quantite
    nb_produits = int(input("Combien de produits voulez-vous ajouter ? "))
    for _ in range(nb_produits):
        nom = input("Entrez le nom du produit : ")
        quantite = int(input(f"Entrez la quantité pour {nom} : "))
        ajouter_produit(nom, quantite)

def supprimer_produit(nom):
    if nom in inventaire :
        del inventaire [nom]
def produit_max():
    return max(inventaire,key=inventaire.get)
#

def superieur(nb):
    for nom, quantite in inventaire.items():
        if quantite > nb:
            print(f"{nom} : {quantite}")

"""print("Inventaire :",inventaire) 

print("Inventaire après suppression :",supprimer_produit("o"),inventaire)
print("Produit avec la quantité maximale :", produit_max())
print("Produits avec une quantité supérieure à 10 :")
superieur()"""
def afficher_max():
    print("Produit avec la quantité maximale :", produit_max())
while True:
    print("\nMenu :")
    print("0. Ajouter un produit")
    print("1. Supprimer un produit")
    print("2. Modifier un produit")
    print("3. Rechercher un produit")
    print("4. Afficher l'inventaire")
    print("5. Afficher le produit avec la quantité maximale")
    print("6. Afficher les produits avec une quantité supérieure à X")
    print("7. Quitter")
    choix = int(input("Votre choix ? "))
    if choix == 7:
        break
    elif choix == 0:
        ajouterunproduit()
    elif choix == 1:
        nom = input("Entrez le nom du produit à supprimer : ")
        supprimer_produit(nom)
    elif choix == 2:
        nom = input("Entrez le nom du produit à modifier : ")
        if nom in inventaire:
            quantite = int(input(f"Entrez la nouvelle quantité pour {nom} : "))
            inventaire[nom] = quantite
        else:
            print("Ce produit n'existe pas")
    elif choix == 3:
        nom = input("Entrez le nom du produit à rechercher : ")
        if nom in inventaire:
            print(f"{nom} : {inventaire[nom]}")
        else:
            print("Ce produit n'existe pas")
    elif choix == 4:
        print("Inventaire :",inventaire)
    elif choix == 5:
        afficher_max()
    elif choix == 6:
        nb = int(input("Entrez le nombre : "))
        print(f"Produits avec une quantité supérieure à {nb} :")
        superieur(nb)
    else:
        print("Erreur, choix invalide")
