from tabulate import tabulate
listaViagens = []

def registrar_viagem(listaViagens):
    motorista = input("Digite o nome do motorista: ")
    destino = input("Digite o destino: ")
    distancia = float(input("Digite a distancia. (em km): "))
    valorgasto = float(input("Digite o valor de gasolina gasto em R$: "))
    
    if distancia > 0:
        cons = valorgasto / distancia
    else:
        cons = 0

    viagem = {
        "Motorista": motorista,
        "Destino": destino,
        "Distancia": distancia,
        "Gasto": valorgasto,
        "Consumo": cons
    }
    
    listaViagens.append(viagem)
    print("Viagem marcada com sucesso!")

def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem cadastrada.")
        return

    headers = ["Motorista", "Destino", "Distancia (km)", "Gasto (R$)", "Consumo (R$/km)"]
    dados = [
        [v["Motorista"], v["Destino"], v["Distancia (km)"], v["Gasto (R$)"], v["Consumo (R$/km)"]]
        for v in listaViagens
    ]

    print(tabulate(
        dados,
        headers=headers,
        tablefmt="fancy_grid",
        numalign="right",
        stralign="center",
        colalign=("center", "center", "right", "right", "right")
    ))

def buscar_motorista(listaViagens):
    motorista_buscar = input("Digite o nome do motorista: ")
    motoristabusca = []
    for i in listaViagens:
        if i ["Motorista"] == motorista_buscar:
            motoristabusca.append(i)
            print(motoristabusca)
def viagem_mais_cara(listaViagens):
    maiorGasto = 0
    for i in listaViagens:
        if i["Gasto"] >= maiorGasto:
            maiorGasto = i["Gasto"]
        print(maiorGasto)
def media_consumo(listaViagens):
    for i in listaViagens:
        for medcons in i["Consumo"]: