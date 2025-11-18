import random
from tabulate import tabulate
id = random.randint(1,100)

ListaAluno = []

def cadastrar_alunos(ListaAluno):
    nomealuno = input("Digite o nome do aluno: ")
    aluno = {
        "ID" : id , "Nome" : nomealuno
    }
    ListaAluno.extend(aluno)
def listar_alunos(ListaAluno):
    lista_vazia = []
    if ListaAluno == lista_vazia:
        print("Não tem nenhum aluno cadastrado.")
    else:
        print(tabulate(ListaAluno, headers="keys", tablefmt="grid"))
def buscar_aluno_por_id(ListaAluno):
    dgtid = input("Digite o id do aluno: ")
    for i in ListaAluno:
        if dgtid == i["ID"]:
            print(i)
        else: 
            print("Não foi encontrada esse aluno.")
