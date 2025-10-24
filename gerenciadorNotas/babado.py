listanomes = []
nome = input("Dgt um nome: ")
notas = []
for i in range(1,4):
    nt = float(input(f"Digite a {i} nota: "))
    notas.append(nt)
notadict = {
    nome : notas
}
listanomes.append(nome)
print(notadict)
