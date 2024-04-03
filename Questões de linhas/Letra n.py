a=[]
for i in range(10):
    a.append(float(input(f"Digite a {i+1}º temperatura em graus celcius:")))
a.sort()
print("A menor temperatura é:", a[0])
print("A maior temperatura é:", a[9])
print("A média das temperaturas é:", sum(a)/10)