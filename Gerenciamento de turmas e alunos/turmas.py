import random
from tabulate import tabulate

ListaTurma = []

id = random.randint(1,100)

def criar_turmas(ListaTurma):
    print("Cadastro de turma.")
    nometurma = str(input("Digite o nome da turma: "))
    turma = {
        "ID" : id,
        "Nome" : nometurma,
    }
    ListaTurma.extend(turma)
def listar_turmas(ListaTurma):
    lista_vazia = []
    if ListaTurma == lista_vazia:
        print("Não tem nenhuma turma cadastrada.")
    else:
        print(tabulate(ListaTurma, headers="keys", tablefmt="grid"))
def buscar_turma_por_id(ListaTurma):
    dgtid = input("Digite o id da turma: ")
    for i in ListaTurma:
        if dgtid == i["ID"]:
            print(i)
        else: 
            print("Não foi encontrada essa turma.")
