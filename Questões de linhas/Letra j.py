a = []
b = []
for i in range(5):
    a.append(int(input("digite um numero: ")))
    somatorio=1
    for j in range(1,i+1):
        somatorio+=j
    b.append(somatorio)
print(a)
print(b)