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
        cons = 0.0

    viagem = {
        "Motorista": motorista,
        "Destino": destino,
        "Distancia (km)": distancia,
        "Gasto (R$)": valorgasto,
        "Consumo (R$/km)": cons
    }
    
    listaViagens.append(viagem)
    print("Viagem marcada com sucesso!")
def exibir_viagens(listaViagens):
    if not listaViagens:
        print("Nenhuma viagem cadastrado.")
    else:
       table = tabulate(
            listaViagens, 
            headers=["Motorista", "Destino", "Distancia" , "Gasto" "Consumo"], 
            tablefmt="fancy_grid",
            numalign="right",
            stralign="center",
            colalign=("center", "center", "right")
        )
    print(table)