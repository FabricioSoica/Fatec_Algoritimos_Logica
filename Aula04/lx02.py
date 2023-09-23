ano_nacimento = int(input("Ano de nascimento: "))
ano_atual = int(input("Ano atual: "))

total_de_ano = ano_atual - ano_nacimento
total_de_meses = total_de_ano * 12
total_de_semanas = total_de_ano * 52
total_de_dias = total_de_ano * 365

print("----------------------")
print("Você tem", total_de_ano, "anos;")
print("Você tem", total_de_meses, "meses;")
print("Você tem", total_de_semanas, "semanas;")
print("Você tem", total_de_dias, "dias.")
print("----------------------")
print("Tenha um bom dia :)")