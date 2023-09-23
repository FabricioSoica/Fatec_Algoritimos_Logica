salario_atual = float(input("Digite seu salário atual: "))
porcentagem_aumento = float(input("Digite o percentual de aumento: "))

total_do_aumento = salario_atual + ((salario_atual * porcentagem_aumento) / 100)

print("----------------------")
print("Seu novo salário pós aumento será: R$", total_do_aumento)