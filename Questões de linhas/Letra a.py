#Ler dez números e apresentar em uma lista
a =[]
for i in range(1,11):
    a.append(int(input("Digite o número:")))
print(a)
#reverte a ordem dos elementos da lista
a.reverse()
print(a)