print('==========================================================================')
print('Bem-vindo ao restaurante Palace. Vá em frente, pode conferir o cardápio:')
print('==========================================================================')

import cardapio
import mesas  # Importa o módulo de mesas

# Conjunto para armazenar as mesas que já fizeram pedidos
mesas_usadas = set()

# Função para solicitar o pedido de uma mesa
def solicitar_pedido():
    mesa_numero = input("\nInforme o número da mesa em que você está agora (1 a 5) ou digite 'sair' para pular: ").strip().lower()

    # Verifica se o usuário deseja pular o pedido dessa mesa
    if mesa_numero == 'sair':
        print("\nVocê optou por pular o pedido dessa mesa.")
        return

    # Valida se a mesa está entre 1 e 5 e se já foi usada
    while True:
        try:
            if not (mesa_numero.isdigit() and 1 <= int(mesa_numero) <= 5):
                raise ValueError("Número de mesa inválido! Por favor, insira um número de mesa entre 1 e 5.")
            if mesa_numero in mesas_usadas:
                raise ValueError(f"A mesa {mesa_numero} já fez o pedido. Escolha outra mesa.")
            break
        except ValueError as e:
            print(e)
            mesa_numero = input("\nInforme o número da mesa em que você está agora (1 a 5) ou digite 'sair' para pular: ").strip().lower()

    # Adiciona a mesa ao conjunto de mesas que já fizeram pedidos
    mesas_usadas.add(mesa_numero)

    print(f"\n==========================================================================")
    print(f"Pedido para a Mesa {mesa_numero}")
    escolhas = input("Digite os números dos pratos pedidos, separados por vírgula: ").split(',')

    pratos_escolhidos = []
    total = 0
    pratos = cardapio.refeicoes + cardapio.sobremesas + cardapio.bebidas

    # Verifica as escolhas feitas
    for escolha in escolhas:
        escolha = escolha.strip()  # Remove espaços em branco
        try:
            if not (escolha.isdigit() and 1 <= int(escolha) <= len(pratos)):
                raise ValueError(f"Escolha inválida: {escolha}. Por favor, tente novamente.")
            prato = pratos[int(escolha) - 1]
            pratos_escolhidos.append(prato)
            total += prato['preço']
        except valor invalido as e:
            print(e)

    # Se houver pratos escolhidos, adiciona o pedido à mesa
    if pratos_escolhidos:
        mesas.adicionar_pedido(mesa_numero, pratos_escolhidos)  # Adiciona o pedido à mesa
        gorjeta = total * 0.10  # Calcula 10% de gorjeta
        print("\nVocê escolheu os seguintes pratos:")
        for prato in pratos_escolhidos:
            print(f"{prato['nome']} - R${prato['preço']:.2f}")
        print(f"\nTotal da conta (incluindo 10% de gorjeta): R${total + gorjeta:.2f}\n")
    else:
        print("\nNenhum prato válido foi escolhido.\n")

# Solicita o pedido de até 5 mesas, permitindo pular mesas sem encerrar o programa
for _ in range(5):
    solicitar_pedido()

# Pergunta se o usuário quer ver o pedido de uma mesa específica, mas apenas das mesas que já pediram
while mesas_usadas:
    ver_mesa = input("\nDeseja ver o pedido de uma mesa específica? (s/n): ").strip().lower()

    if ver_mesa == 's':
        print(f"As mesas que já fizeram pedidos são: {', '.join(mesas_usadas)}")
        mesa_para_ver = input("\nDigite o número da mesa que você deseja ver: ").strip()

        # Certifica-se de que a mesa escolhida fez um pedido
        while mesa_para_ver not in mesas_usadas:
            print(f"A mesa {mesa_para_ver} não fez um pedido. Escolha outra mesa.")
            mesa_para_ver = input("\nDigite o número da mesa que você deseja ver: ").strip()

        # Mostra o pedido da mesa selecionada
        pedido_da_mesa = mesas.mostrar_pedido_mesa(mesa_para_ver)

        if pedido_da_mesa:
            print(f"\nPedido da mesa {mesa_para_ver}:")
            for prato in pedido_da_mesa:
                print(f"{prato['nome']} - R${prato['preço']:.2f}")
        else:
            print(f"\nNão há pedidos registrados para a mesa {mesa_para_ver}.")
        
        # Pergunta se deseja ver outra mesa
        continuar = input("\nDeseja ver o pedido de outra mesa? (s/n): ").strip().lower()
        if continuar != 's':
            break
    else:
        print("\nObrigado por utilizar o nosso sistema!")
        break

if not mesas_usadas:
    print("\nNenhuma mesa fez pedidos.")
