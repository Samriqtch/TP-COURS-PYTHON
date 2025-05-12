
entree = input("Veuillez entrer une série de températures séparées par des virgules : ")

temperatures = []
for temp in entree.split(","):
    temperatures.append(float(temp))

moyenne = sum(temperatures) / len(temperatures)

temp_max = max(temperatures)
temp_min = min(temperatures)

compteur = 0
for temp in temperatures:
    if temp > moyenne:
        compteur += 1

print(f"Température moyenne : {moyenne:.2f}")
print(f"Température maximale : {temp_max}")
print(f"Température minimale : {temp_min}")
print(f"Nombre de températures au-dessus de la moyenne : {compteur}")