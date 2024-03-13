A= float(input("primeiro lado: "))
B= float(input("segundo lado: "))
C= float(input("terceiro lado: "))
if A<B+C and B<A+C and C<A+B:
  if  A==B and B==C:
      print("triângulo equilátero")
  elif A==B or A==C or B==C:
      print("triângulo isósceles")
  else:
      print("triângulo escaleno")
else:
      print("os lados não formam um triâgulo")
