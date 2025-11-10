from tabulate import tabulate
from funcoes import *
while True:
        print("Menu de Opções:")
        print("1 - Registrar nova viagem")
        print("2 - Exibir todas as viagens")
        print("3 - Buscar viagens por motorista")
        print("4 - Exibir viagem mais cara")
        print("5 - Mostrar média geral de consumo")
        print("0 - Sair")
    
        op = int(input("Digite uma opção: "))

        match op:
            case 1:
                registrar_viagem(listaViagens)
            case 2:
                exibir_viagens(listaViagens)
            case 3:
                buscar_motorista(listaViagens)
            case 4:
                viagem_mais_cara(listaViagens)
            case 5:
                  media_consumo(listaViagens)
            case 0:
                break
            case _:
                print("Opção inválida.")
    