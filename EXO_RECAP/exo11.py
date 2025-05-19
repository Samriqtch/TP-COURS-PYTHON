# Dictionnaire des produits : clé = nom du produit, valeur = {"quantite": int, "prix": float}
produits = {
    "pomme": {"quantite": 10, "prix": 5000},
    "banane": {"quantite": 5, "prix": 6000},
    "orange": {"quantite": 8, "prix": 10000}
}

def afficher_produits():
    print("Liste des produits :")
    for nom in produits:
        infos = produits[nom]
        print(f"{nom} - Quantité : {infos['quantite']}, Prix : {infos['prix']} ")

def ajouter_produit():
    nom = input("Nom du produit à ajouter : ")
    if nom in produits:
        print("Ce produit existe déjà.")
    else:
        quantite = int(input("Quantité : "))
        prix = float(input("Prix : "))
        produits[nom] = {"quantite": quantite, "prix": prix}
        print(f"{nom} ajouté.")

def supprimer_produit():
    nom = input("Nom du produit à supprimer : ")
    if nom in produits:
        del produits[nom]
        print(f"{nom} supprimé.")
    else:
        print("Produit non trouvé.")

def modifier_produit():
    nom = input("Nom du produit à modifier : ")
    if nom in produits:
        quantite = int(input(f"Nouvelle quantité pour {nom}  : "))
        prix = float(input(f"Nouveau prix pour {nom}  : "))
        produits[nom]["quantite"] = quantite
        produits[nom]["prix"] = prix
        print(f"{nom} mis à jour.")
    else:
        print("Produit non trouvé.")

while True:
    print("\nMenu :")
    print("1. Afficher la liste des produits")
    print("2. Ajouter un produit")
    print("3. Supprimer un produit")
    print("4. Modifier la quantité ou le prix d'un produit")
    print("5. Quitter le programme")

    choix = int(input("Veuillez faire un choix : "))

    if choix == 1:
        afficher_produits()
    elif choix == 2:
        ajouter_produit()
    elif choix == 3:
        supprimer_produit()
    elif choix == 4:
        modifier_produit()
    elif choix == 5:
        break
    else:
        print("Choix incorrect")
