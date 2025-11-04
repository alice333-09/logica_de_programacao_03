import requests, json

nome = input("Digite seu nome: ")
cep_digitado = input('Digite seu CEP: ')
dados = requests.get(f"https://viacep.com.br/ws/{cep_digitado}/json/").json()
print(dados)

with open(f"CEP {nome}.json" , "w") as ceppessoa: 
    json.dump(dados, ceppessoa, indent=4)

print(f"\n✅ Dados do CEP salvos em 'CEP {nome}.json'")