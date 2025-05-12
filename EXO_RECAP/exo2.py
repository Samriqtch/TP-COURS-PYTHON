# Fonction pour afficher les représentations d'un nombre
def afficher_representations(nombre):
    print(f"Représentation binaire : {bin(nombre)}")
    print(f"Représentation hexadécimale : {hex(nombre)}")
    print(f"Représentation octale : {oct(nombre)}")

# Exemple d'utilisation
nombre = int(input("Veuillez entrer un nombre entier : "))
afficher_representations(nombre)