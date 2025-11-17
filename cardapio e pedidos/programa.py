from tabulate import tabulate
from funcao import * 

while True:
    print("1 - Ver Cardapio")
    print("2 - Adicionar item ao pedido")
    print("3 - Ver pedido")
    print("4 - Remover Item")
    print("0 - Finalizar")
    op = input("Digite uma opção: ")
    match op:
        case "1":
            exibir_cardapio()
        case "2":
            adicionar_pedido()
        case "3":
            exibir_pedido()
        case "4":
            remover_item()
        case "0":
            print("Saindo do programa. . .")
            break
        case _:
            print("Opção inválida.")