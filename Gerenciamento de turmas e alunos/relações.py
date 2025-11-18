# ...existing code...
from alunos import *
from turmas import *
from tabulate import tabulate

relacoes = []

def adicionar_aluno_na_turma(relacoes):
    id_aluno = int(input("Digite o ID do Aluno: "))
    id_turma = int(input("Digite o ID da Turma: "))
    turmaexiste = False
    alunoexiste = False
    for turma in ListaTurma:
        if id_turma == turma["ID"]:
            turmaexiste = True
            break
    for aluno in ListaAluno:
        if id_aluno == aluno["ID"]:
            alunoexiste = True
            break
    if not turmaexiste and not alunoexiste:
        print("A turma e nem aluno foi encontrado.")
        return
    if not turmaexiste and alunoexiste:
        print("Turma não encontrada.")
        return
    if turmaexiste and not alunoexiste:
        print("Aluno não foi encontrado.")
        return
    relacao = {
        "ID_ALUNO": id_aluno,
        "ID_TURMA": id_turma
    }
    relacoes.append(relacao)
    print("Relacao feita com sucesso.")

def listar_alunos_da_turma(relacoes):
    id_turma = int(input("Digite o ID da Turma: "))
    turmaexiste = False
    for turma in ListaTurma:
        if id_turma == turma["ID"]:
            turmaexiste = True
            break
    if not turmaexiste:
        print("Turma não encontrada.")
        return
    alunos_turma = []
    for relacao in relacoes:
        if relacao.get("ID_TURMA") == id_turma:
            id_aluno = relacao.get("ID_ALUNO")
            for aluno in ListaAluno:
                if aluno["ID"] == id_aluno:
                    alunos_turma.append(aluno)
                    break
    if not alunos_turma:
        print("Nenhum aluno encontrado nesta turma.")
        return
    print(tabulate(alunos_turma, headers="keys", tablefmt="grid"))

def remover_aluno_da_turma(relacoes):
    idaluno = input("Digite o id do aluno: ")
    idturma = input("Digite o id da turma: ")
    for i in relacoes:
        if idaluno == i["ID_ALUNO"] and id_turma == i["ID_TURMA"]:
            relacoes.remove(i)
        else:
            print("Não foi encontrada essa relação.")