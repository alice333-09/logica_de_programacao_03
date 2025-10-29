
def calcular_media(ListaNotas):
    media = sum(ListaNotas) / len(ListaNotas)
    return media


def verificar_situação(media):
    if media >= 7:
        return ("Aprovado!")
    if media >= 5 or media <= 6.9:
        return ("Recuperação")
    else:
        return ("Reprovado")


    