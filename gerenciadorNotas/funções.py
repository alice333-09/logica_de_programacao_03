
def calcular_media(ListaNotas):
    for i in range(1,5):
        digitar = int(input("Digite as notas: "))
        ListaNotas.append(digitar)
        notas = sum(ListaNotas)
    media = notas / 4

def verificar(media):
    if media >= 7:
        print("Aprovado!")
    