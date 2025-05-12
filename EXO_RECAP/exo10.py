def analyse_texte(chaine):
    # Compter le nombre de mots
    mots = chaine.split()
    nombre_de_mots = len(mots)
    
    # Compter le nombre de phrases (finissant par ., ?, !)
    nombre_de_phrases = sum(1 for char in chaine if char in ".?!")
    
    # Trouver le mot le plus long
    mot_le_plus_long = max(mots, key=len) if mots else ""
    
    return nombre_de_mots, nombre_de_phrases, mot_le_plus_long

# Exemple d'utilisation
texte = input("Veuillez entrer un texte : ")
nombre_de_mots, nombre_de_phrases, mot_le_plus_long = analyse_texte(texte)

print(f"Nombre de mots : {nombre_de_mots}")
print(f"Nombre de phrases : {nombre_de_phrases}")
print(f"Mot le plus long : {mot_le_plus_long}")