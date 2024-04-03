a=[]
par=0
impar=0
for i in range(10):
    a.append(int(input( "digite um numero: ")))
    if a[i]%2==0:
       par+=1
    else:
        impar+=1
print(f"quantidade de numerps pares: {par}")
print(f"quantidade de numerps impares: {impar}")