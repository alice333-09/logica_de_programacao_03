lista_cardapio=[]
def carregar_cardapio():
    cardapio =[
        {"id": 1, "nome": "Hambúrguer", "preco": 12.50}, 
        {"id": 2, "nome": "Batata Frita", "preco": 7.00}, 
        {"id": 3, "nome": "Refrigerante", "preco": 5.00}
    ]
    lista_cardapio.extend(cardapio)
def exibir_cardapio():
    carregar_cardapio()
    return lista_cardapio
def buscar_item():
    iddgt = int(input("Digite o id do item que gostaria de pedir: "))
    for i in lista_cardapio:
        if i ["id"] == iddgt:
            print(i)