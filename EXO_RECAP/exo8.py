# Liste d'entiers donnée
entiers = [10, 15, 20, 10, 25, 30, 15, 40, 50, 30]

# Calculer la moyenne de la liste
moyenne = sum(entiers) / len(entiers)

# Construire une nouvelle liste contenant uniquement les nombres :
# - Pairs
# - Supérieurs à la moyenne
# - Non présents plus d'une fois (sans doublons)
nouvelle_liste = [x for x in set(entiers) if x % 2 == 0 and x > moyenne]

# Afficher les résultats
print(f"Liste originale : {entiers}")
print(f"Moyenne : {moyenne:.2f}")
print(f"Nouvelle liste : {nouvelle_liste}")