# Programme pour évaluer une expression mathématique

# Demander à l'utilisateur de saisir une expression mathématique
"""
expression = input("Veuillez entrer une expression mathématique : ")

try:
    # Évaluer l'expression
    resultat = eval(expression)
    
    # Afficher le résultat et son type
    print(f"Le résultat de l'évaluation est : {resultat}")
    print(f"Le type du résultat est : {type(resultat).__name__}")
except Exception as e:
    # Gérer les erreurs d'évaluation
    print(f"Erreur lors de l'évaluation de l'expression : {e}")
"""

#une deuxième methode 

chaine1 = input("Veuillez entrer une expression mathématique de votre choix : ")

resultat =eval(chaine1)

print("le resultat de votre opération est : ",resultat)
print("votre resultat est de type : ",type(resultat))