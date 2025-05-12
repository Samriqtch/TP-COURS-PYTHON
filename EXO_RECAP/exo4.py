# Code PIN fixé dans le programme
code_pin_correct = "1234"
essais_restants = 3

# Boucle pour demander le code PIN
while essais_restants > 0:
    code_pin = input("Veuillez entrer votre code PIN : ")
    if code_pin == code_pin_correct:
        print("Accès autorisé.")
        break
    else:
        essais_restants -= 1
        print(f"Code PIN incorrect. Il vous reste {essais_restants} essai(s).")

# Si les essais sont épuisés
if essais_restants == 0:
    print("Accès interdit.")