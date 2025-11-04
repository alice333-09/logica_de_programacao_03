import json

nome = input("Digite seu nome: ")
senha = input("Digite sua senha (apenas números): ")
email = input("Digite seu e-mail: ")
telefone = input("Digite seu telefone (apenas números): ")

print(f"\nDados coletados.")

dados_para_salvar = {
    "nome": nome,
    "senha": senha,
    "email": email,
    "telefone": telefone
}

nome_arquivo = f"Conta_{nome}.json"

with open(nome_arquivo, "w", encoding="utf-8") as arquivo_json: 
    json.dump(dados_para_salvar, arquivo_json, indent=4)

print(f"✅ Sucesso! Os dados foram salvos em '{nome_arquivo}'.")