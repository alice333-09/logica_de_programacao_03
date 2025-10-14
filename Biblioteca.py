import requests, json , random
sorteio = ["babado do(a)" , "az area do(a)" , "babilonia do(a)" , "casa do carai do(a)" , "localizao do (a)"]
computador = random.choice(sorteio)
nome = input("Digite seu nome: ")
dados = requests.get(f"https://viacep.com.br/ws/{input('Digite seu CEP: ')}/json/").json()
print(dados)
with open(f"{computador} {nome}.json" , "w") as ceppessoa: json.dump(dados, ceppessoa)
