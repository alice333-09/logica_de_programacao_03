
def calcular_media(ListaNotas):
    for i in range(1,5):
        digitar = int(input("Digite as notas: "))
        ListaNotas.append(digitar)
    notas = sum(ListaNotas)
    media = notas / i
    return (f"A média é {media}")

def verificar_situação(media):
    if media >= 7:
        return ("Aprovado!")
    if media >= 5 or media <= 6.9:
        return ("Recuperação")
    else:
        return ("Reprovado")


    