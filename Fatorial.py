fatorial = 1
contador = 1
n = float(input("número:"))
while contador<= n:
    fatorial *= contador
    contador += 1
print("O fatorial de", n, "é:", fatorial)