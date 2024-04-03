a=[]
n = int(input("Digite o número:"))
for i in range(1,11):
    a.append(n*i)
    print(f"{n} x {i} = {a[i-1]}")