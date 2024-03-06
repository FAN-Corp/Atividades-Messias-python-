print("-------Questão 1-------")
n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda nota:"))
n3 = float(input("Terceira nota:"))
n4 = float(input("Quarta nota:"))
M = (n1 + n2 + n3 + n4) / 4 
if M >= 7:
  print("Aprovado com média:", M, "Parabéns!!!")
else:
  print("Reprovado com média:", M, "O aluno fará a prova final no dia xx/xx/xx. \n ... \n ... \n ... \n ------Dia da prova final------")
  nf = float(input("Nota da prova final:"))
  mf = (M + nf) / 2 
  if mf >= 7:
    print("média da prova final:", mf, "\nAprovado prova final. Parabéns!")
  else:
    print("média da prova final:", mf, "\nReprovado. Boa sorte na próxima!") 