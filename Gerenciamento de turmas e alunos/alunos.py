import random
from tabulate import tabulate

ListaAluno = []

def cadastrar_alunos(ListaAluno):
    nomealuno = input("Digite o nome do aluno: ")
    id = random.randint(1, 100)
    aluno = {
        "ID": id,
        "Nome": nomealuno
    }
    ListaAluno.append(aluno)
    print("Aluno cadastrado com sucesso!")

def listar_alunos(ListaAluno):
    if not ListaAluno:
        print("Não tem nenhum aluno cadastrado.")
    else:
        print(tabulate(ListaAluno, headers="keys", tablefmt="grid"))

def buscar_aluno_por_id(ListaAluno):
    dgtid = int(input("Digite o id do aluno: "))
    encontrado = False
    for i in ListaAluno:
        if dgtid == i["ID"]:
            print(i)
            encontrado = True
            break
    if not encontrado:
        print("Aluno não foi encontrado.")