def nombre_paire(limite):
    return [i for i in range(0,limite+1) if i%2 == 0]

print(nombre_paire(10))