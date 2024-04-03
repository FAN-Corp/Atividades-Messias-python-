a = []
b = []
c = []
for i in range(5):
     a.append(int(input(f"Digite o {i + 1} elemento de número A:")))
     b.append(int(input(f"Digite o {i + 1} elemento de número B:")))
     c.append(a[i] -b[i])
print(c)