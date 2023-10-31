pessoas = {}

for i in range(5):
    sobrenome = input("Digite o sobrenome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas[sobrenome] = idade

sobrenome_mais_velho = max(pessoas, key=pessoas.get)

print(f"A pessoa mais velha é {sobrenome_mais_velho} com {pessoas[sobrenome_mais_velho]} anos de idade.")


