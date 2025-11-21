import random
from tabulate import tabulate

ListaTurma = []

def criar_turmas(ListaTurma):
    print("Cadastro de turma.")
    nometurma = str(input("Digite o nome da turma: "))
    id = random.randint(1, 100)
    turma = {
        "ID": id,
        "Nome": nometurma,
    }
    ListaTurma.append(turma)
    print("Turma criada com sucesso!")

def listar_turmas(ListaTurma):
    if not ListaTurma:
        print("Não tem nenhuma turma cadastrada.")
    else:
        print(tabulate(ListaTurma, headers="keys", tablefmt="grid"))

def buscar_turma_por_id(ListaTurma):
    dgtid = int(input("Digite o id da turma: "))
    encontrada = False
    for i in ListaTurma:
        if dgtid == i["ID"]:
            print(i)
            encontrada = True
            break
    if not encontrada:
        print("Turma não foi encontrada.")