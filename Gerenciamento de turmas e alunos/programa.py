from alunos import *
from relações import *
from turmas import *

while True:
    print("1 - Criar Turma")
    print("2 - Cadastrar Aluno.")
    print("3 - Adicionar Aluno á turma.")
    print("4 - Listar Turmas.")
    print("5 - Listar Alunos.")
    print("6 - Listar Alunos de uma turma.")
    print("7 - Remover aluno da turma.")
    print("0 - Sair")

    op = input("Digite uma opção: ")
    
    if op == "1":
        criar_turmas(ListaTurma)
    elif op == "2":
        cadastrar_alunos(ListaAluno)
    elif op == "3":
        adicionar_aluno_na_turma(relacoes)
    elif op == "4":
        listar_turmas(ListaTurma)
    elif op == "5":
        listar_alunos(ListaAluno)
    elif op == "6":
        listar_alunos_da_turma(relacoes)
    elif op == "7":
        remover_aluno_da_turma(relacoes)
    elif op == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")