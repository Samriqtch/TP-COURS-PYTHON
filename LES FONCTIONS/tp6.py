import math

def resoudre_equation_degre_2(a, b, c):
    delta = math.pow(b, 2) - 4 * a * c  # Utilisation de math.pow pour b^2
    if delta < 0:
        return "L'équation n'a pas de solution réelle"
    elif delta == 0:
        return -b / (2 * a)
    else:
        sol1 = (-b + math.sqrt(delta)) / (2 * a)  # Utilisation de math.sqrt pour √delta
        sol2 = (-b - math.sqrt(delta)) / (2 * a)
        return sol1, sol2

# Exemple d'utilisation
a = 1
b = -3
c = 2
solutions = resoudre_equation_degre_2(a, b, c)
print(solutions)