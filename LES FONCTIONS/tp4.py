def inverse(chaine):
    return chaine[::-1]
chaine = input("Entrez une chaîne de caractères : ")
resultat = inverse(chaine)
print("La chaîne inversée est :", resultat)

# autre proposition
def inverse_sans_fonction_inverse(chaine):
    resultat = ""
    for i in range(len(chaine)-1, -1, -1):
        resultat += chaine[i]
    return resultat

chaine = "Samson"

print(inverse_sans_fonction_inverse(chaine))



# Proposition 3
def inverse_en_liste(chaine):
    liste = list(chaine)
    liste.reverse()
    return "".join(liste)

chaine = "Samson"

print(inverse_en_liste(chaine))

#autre proposition
def inverse_ch(chaine):
    resulat=""
    for c in chaine:
        resulat=c+resulat
    return resulat
print(inverse_ch("Samson"))


