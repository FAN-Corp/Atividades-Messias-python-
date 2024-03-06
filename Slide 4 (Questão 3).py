a = float(input("a:"))
b = float(input("b:"))
c = float(input("c:"))
d = b**2 + (4 * a * c) 
r1 = ((-b) + d**(1/2))/2
r2 = ((-b) - d**(1/2))/2
if d > 0:
  print("O delta 'd' é maior que zero. Portanto terá duas raizes diferentes,são essas:", r1, "e", r2)
if d == 0:
    print("O delta 'd' é maior que zero. Portanto terá duas raizes iguais, são essas:", r1, "e", r2)
if d < 0:
  print("O delta 'd' é menor que zero. Portanto não tem raizes em R.")
