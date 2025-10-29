
import tabulate
ListaLivros = []
status = ["Disponivel" , "Emprestado"]
while True:
    print("1 - Adicionar Livro")
    print("2 - Exibir livros")
    print("3 - Emprestar Livro")
    print("4 - Devolver Livro")
    print("0 - Sair")
    dgt = int(input("Digite uma opção: "))
    if dgt == 1:
        titulo = input("Digite o titulo do Livro: ")
        autor = input("Digite o autor do livro: ")
        sl = status[0]
        dict = {
        "Titulo:" : titulo,
        "Autor:" : autor,
        "Status:" : sl
        }
        ListaLivros.append(dict)
        print("Livro adicionado.")
    if dgt == 2:
        print(ListaLivros)
    if dgt == 3:
        livro = input("Digite o titulo do livro: ")
        print(f"{livro} Emprestado com sucesso!")
        sl = status[1]
    if dgt == 4:
        livro = input("Digite o titulo do livro: ")
        print(f"{livro} Devolvido com sucesso!")
        sl = status[0]
    
