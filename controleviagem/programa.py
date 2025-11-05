from tabulate import tabulate
from funcoes import *

while True:
        print("\nMenu de Opções:")
        print("1 - Registrar nova viagem")
        print("2 - Exibir todas as viagens")
        print("3 - Buscar viagens por motorista")
        print("4 - Exibir viagem mais cara")
        print("5 - Mostrar média geral de consumo")
        print("0 - Sair")
        
        op = int(input("Digite uma opção: "))
        if op == 1:
            registrar_viagem(listaViagens)
        if op == 2:
            exibir_viagens(listaViagens)
        if op == 3:
             buscar_motorista(listaViagens)
