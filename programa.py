#Programa que simula um restaurante do ponto de vista de um cliente (que vai fzer pdidos) e um garçom (que vai guardar o resultados e apresentar os preços).#
print('==========================================================================')
print('Bem-vindo ao restaurante Palace. Vá em frente, pode conferir o cardápio:')
print('==========================================================================')

import cardapio 

# Solicita as escolhas do usuário, separadas por vírgula
escolhas = input("==========================================================================\nDigite os números dos pratos que você deseja, separados por vírgula: ").split(',')

pratos_escolhidos = []
total = 0
pratos = cardapio.refeicoes + cardapio.sobremesas + cardapio.bebidas

# Verifica as escolhas feitas
for escolha in escolhas:
    escolha = escolha.strip()  # Remove espaços em branco
    if escolha.isdigit() and 1 <= int(escolha) <= len(pratos):
        prato = pratos[int(escolha) - 1]
        pratos_escolhidos.append(prato)
        total += prato['preço']
    else:
        print(f"\nEscolha inválida: {escolha}. Por favor, tente novamente.")

# Exibe os pratos escolhidos e o total da conta
if pratos_escolhidos:
    gorjeta = total * 0.10  # Calcula 10% de gorjeta
    print("\nVocê escolheu os seguintes pratos:")
    for prato in pratos_escolhidos:
        print(f"{prato['nome']} - R${prato['preço']:.2f}")
    print(f"\nTotal da conta (incluindo 10% de gorjeta): R${total + gorjeta:.2f}")
else:
    print("\nNenhum prato válido foi escolhido.")
