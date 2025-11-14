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
    print(tabulate(listaViagens))

def buscar_motorista(listaViagens):
    motorista_buscar = input("Digite o nome do motorista: ")
    for i in listaViagens:
        if i ["Motorista"] == motorista_buscar:
            print(i)
        else:
            print("Nenhuma viagem feita por esse motorista.")
def viagem_mais_cara(listaViagens):
    maiorGasto = 0
    for i in listaViagens:
        if i["Gasto"] >= maiorGasto:
            maiorGasto = i["Gasto"]
            condutor = i["Motorista"]
        print(f"a viagem mais cara custa: {maiorGasto} e o motorista que conduziu foi {condutor}.")

def media_consumo(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem registrada.")
        return

    total = sum(v.get("Consumo", 0) for v in listaViagens)
    contador = len(listaViagens)
    media = total / contador if contador else 0
    print(f"A média de consumo de todas as viagens é {media:.2f}")