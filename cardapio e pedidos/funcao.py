from tabulate import tabulate

Cardapio = []
Pedido = []

def carregar_cardapio():
    produto1 = {"ID": 1, "Nome": "Pizza", "PREÇO": 30}
    produto2 = {"ID": 2, "Nome": "Refrigerante", "PREÇO": 5}
    produto3 = {"ID": 3, "Nome": "Hambúrguer", "PREÇO": 12.5}
    Cardapio.extend([produto1, produto2, produto3])

def exibir_cardapio():
    if Cardapio:
        print(tabulate(Cardapio, headers="keys", tablefmt="grid"))
    else:
        print("Cardápio vazio. Carregando...")
        carregar_cardapio()
        print(tabulate(Cardapio, headers="keys", tablefmt="grid"))

def adicionar_pedido():
    id = int(input("Digite o id do item: ")) - 1
    qtd = int(input("Digite a quantidade: "))
    total = Cardapio[id]["PREÇO"] * qtd
    pedidocliente = {
        "Item": Cardapio[id]["Nome"],
        "Quantidade": qtd,
        "Total": total
    }
    Pedido.append(pedidocliente)

def exibir_pedido():
    lista_vazia = []
    if Pedido == lista_vazia:
        print("Não tem nenhum pedido feito.")
    print(tabulate(Pedido, headers="keys", tablefmt="grid"))
def remover_item():
    id = int(input("Digite o id do item: ")) - 1
    Pedido.remove(Pedido[id])
    print("Removido com sucesso!")