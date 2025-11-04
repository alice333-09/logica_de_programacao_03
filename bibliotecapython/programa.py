
from tabulate import tabulate
from funcoes import *

ListaLivros = []
status = ["Disponivel", "Emprestado"]

while True:
    print("1 - Adicionar Livro")
    print("2 - Exibir livros")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("0 - Sair")


    dgt = int(input("Digite uma opcao: "))


    if dgt == 1:
        adicionar_livro(ListaLivros, status)

    elif dgt == 2:
        exibir_livros(ListaLivros)

    elif dgt == 3:
        emprestar_livro(ListaLivros, status)

    elif dgt == 4:
        devolver_livro(ListaLivros, status)
            
    elif dgt == 0:
        print("Saindo do programa.")
        break

    else:
        print("Opcao invalida.")
        