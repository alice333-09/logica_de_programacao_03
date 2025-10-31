import tabulate
def adicionar_livro(ListaLivros, status):
    titulo = input("Digite o titulo do Livro: ")
    autor = input("Digite o autor do livro: ")
    sl = status[0]
    dict_livro = {"Titulo": titulo, "Autor": autor, "Status": sl} 
    ListaLivros.append(dict_livro)
    print("Livro adicionado.")

def exibir_livros(ListaLivros):
    if not ListaLivros:
        print("Nenhum livro cadastrado.")
    else:
        headers = ["Título", "Autor", "Status"]

        tabela = [list(livro.values()) for livro in ListaLivros]
        print(tabulate.tabulate(tabela, headers=headers, tablefmt="fancy_grid"))

def emprestar_livro(ListaLivros, status):
    livro_titulo = input("Digite o titulo do livro que deseja emprestar: ")
    livro_encontrado = None

    for livro in ListaLivros:
        if livro["Titulo"] == livro_titulo:
            livro_encontrado = livro
            break

    if livro_encontrado:
        if livro_encontrado["Status"] == status[0]:
            livro_encontrado["Status"] = status[1]
            print(f"{livro_titulo} Emprestado com sucesso!")
        else:
            print(f"{livro_titulo} ja esta emprestado.")
    else:
        print(f"Livro '{livro_titulo}' nao encontrado.")

def devolver_livro(ListaLivros, status):
    livro_titulo = input("Digite o titulo do livro que deseja devolver: ")
    livro_encontrado = None

    for livro in ListaLivros:
        if livro["Titulo"] == livro_titulo:
            livro_encontrado = livro
            break

    if livro_encontrado:
        if livro_encontrado["Status"] == status[1]:
            livro_encontrado["Status"] = status[0]
            print(f"{livro_titulo} Devolvido com sucesso!")
        else:
            print(f"{livro_titulo} ja esta disponivel.")
    else:
        print(f"Livro '{livro_titulo}' nao encontrado.")