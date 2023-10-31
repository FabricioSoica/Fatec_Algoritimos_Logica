pessoas = {}

for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas[nome] = idade

idades = list(pessoas.values())
media_idades = sum(idades) / len(idades)

pessoas_acima_da_media = [nome for nome, idade in pessoas.items() if idade > media_idades]

print("Nomes das pessoas com idade maior que a média:")
for nome in pessoas_acima_da_media:
    print(nome)







