# Dicionário para armazenar os pedidos por mesa
pedidos_mesas = {}

def adicionar_pedido(mesa, pedido):
    if mesa in pedidos_mesas:
        pedidos_mesas[mesa].extend(pedido)  # Adiciona os novos pedidos à mesa existente
    else:
        pedidos_mesas[mesa] = pedido  # Cria uma nova mesa com o pedido

def mostrar_pedido_mesa(mesa):
    if mesa in pedidos_mesas:
        return pedidos_mesas[mesa]
    else:
        return None  # Se não houver pedidos para a mesa
