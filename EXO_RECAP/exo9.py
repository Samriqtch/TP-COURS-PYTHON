import random
import string

def generer_mdp(longueur):
    if longueur < 1:
        return "La longueur doit être supérieure à 0."
    
    # Combinaison de lettres, chiffres et caractères spéciaux
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    # Générer un mot de passe aléatoire
    mot_de_passe = ''.join(random.choice(caracteres) for _ in range(longueur))
    return mot_de_passe

# Exemple d'utilisation
longueur = int(input("Veuillez entrer la longueur du mot de passe : "))
mot_de_passe = generer_mdp(longueur)
print(f"Mot de passe généré : {mot_de_passe}")