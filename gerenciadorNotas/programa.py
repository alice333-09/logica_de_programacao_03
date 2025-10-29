from funções import *
import tabulate

ListaAlunos = []

while True:
    print("1 - Cadastrar alunos e notas")
    print("2- Exibir relatório")
    print("0- Sair")

    dgt = int(input("Escolha uma das opções: "))

    if dgt == 1:
        nomalu = input("Digite o nome do aluno: ")
        
        listaNotas = []
                        
        for i in range(1, 4):
            nota = float(input(f"Digite a {i}ª nota: "))
            listaNotas.append(nota)
        
        Media = calcular_media(listaNotas)
        sit = verificar_situação(Media)
        
        aluno_dados = {
            "Aluno": nomalu, 
            "Notas": listaNotas, 
            "Media": Media, 
            "Situação": sit
        }
        
        ListaAlunos.append(aluno_dados)
        print(f"✅ {nomalu} foi cadastrado.")

    elif dgt == 2:
        headers = ["Aluno", "Média", "Situação"]
        
        table_data = []
        for aluno in ListaAlunos:
            table_data.append([
                aluno['Aluno'],
                f"{aluno['Media']:.2f}",
                aluno['Situação']
            ])
        print("📊 RELATÓRIO DE ALUNOS E NOTAS")
        
        print(tabulate.tabulate(table_data, headers=headers, tablefmt="simple"))

        if dgt == 0:
            print("Programa Finalizado.")