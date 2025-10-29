from operacoes import *
while True:
    print(" 1 - Soma ")
    print(" 2 - Subtrção ")
    print(" 3 - Multiplicação ")
    print(" 4 - Divisão ")
    print(" 0 - Sair ")
    opcE = input(" Escolha uma das opções: ")
    if opcE == "1":
        x = int(input(" Digite o primeiro número da soma: "))
        y = int(input(" Digite o seundo número da soma: "))
        z = (soma(x,y))
        print(f"A soma: {x} + {y} é igual a {z}")
    if opcE == "2":
        x = int(input(" Digite o primeiro número da subtração : "))
        y = int(input(" Digite o seundo número da subtração : "))
        z = (subtração(x,y))
        print(f"A subtração: {x} - {y} é igual a {z}")
    if opcE == "3":
        x = int(input("Digite o primeiro número da multiplicação :"))
        y = int(input("Digite o seundo número da multiplicação : "))
        z = (multiplicação(x,y))
        print(f"A multiplicação: {x} x {y} é igual a {z}")
    if opcE == "4":
        x = int(input("Digite o primeiro número da divisão:"))
        y = int(input("Digite o seundo número da divisão: "))
        z = (divisão(x,y))
        print(f"A divisão: {x} % {y} é igual a {z}")
    if opcE == "0":
        break