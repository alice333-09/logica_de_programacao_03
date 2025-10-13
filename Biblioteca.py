
import requests
import json

nome = input("Digite seu nome: ")
cep = int(input("Digite seu CEP: "))
dados = requests.get (f"https://viacep.com.br/ws/{cep}/json/") 
with open(f"{nome}-cep.json" , "w") as ceppessoa:
    ceppessoa.write(print(f"{dados.json()}"))
    















