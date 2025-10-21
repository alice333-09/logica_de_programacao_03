from funções import *

while True:
    print("1- Cadastar alunos e notas")
    print("2- Exibir relatório")
    print("0- Sair")

    dgt = input("Escolha uma das opções: ")

    if dgt == "1":
        nomalu = input("Digite o nome do aluno: ")
        for i in range(4):
            nt = []
            nt.append(int(input("Digite as nota do aluno: ")))
        print(f"{nomalu} foi cadastrado.")

    
           


    


