a,b,c=[],[],[]
cont=0
print("========Inserindo numeros da lista a========")
while cont<6:
    n = (int(input("Digite um número par:")))
    if n%2==0:
        a.append(n)
        cont+=1
    else:
        print("Número impar")
        
cont=0
print("========Inserindo numeros da lista b========")
while cont<6:
    n = (int(input("Digite um número impar:")))
    if n%2!=0:
        a.append(n)
        cont+=1
    else:
        print("Número par")
c=a+b
print(c)