# Quetão 1 (cadastro de nomes)

# lista=[]
# for i in range(5):
#     lista.append(input("Digite um nome: "))
# print(lista)
# letras=["A","a"]
# cont=0
# for i in lista:
#     if i[0] in letras:
#         cont=0
#     else:
#         cont+=1
# print(cont)

# questão 2 (media de notas)

# def calcular_media(lista_notas):
#     soma = 0
#     quantidade = 0
#     for nota in lista_notas:
#         soma += nota
#         quantidade += 1
#     return soma / quantidade
# notas = []
# for i in range(4):
#     nota = float(input(f"Digite a {i+1} nota: "))
#     notas.append(nota)
# media = calcular_media(notas)
# print(f"Média = {media}")
# if media >= 7:
#     print("Aluno aprovado!")
# else:
#     print("Aluno reprovado!")

# quetão 3 (soma de pares e ímpares)

lista=[]
lisp=[]
lisi=[]
for i in range(10):
    lista.append(int(input("Digite um número: ")))
for i in lista:
    if i % 2 == 0:
        lisp.append(i)
print(lisp)
        


# questão 4 (lista de convidados)

# lista=[]
# for i in range(5):
#     lista.append(input("Digite o nome do convidado: "))
# nomeconv=input("Digite o nome do convidado que gostaria de confirmar: ")
# if nomeconv in lista:
#     print("Convidado confirmado!")
# else:
#     print("Convidado não encontrado!")

