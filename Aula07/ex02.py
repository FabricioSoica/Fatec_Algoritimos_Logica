soma: int = 0
for i in range(1, 11):
    n = int(input(f"Entre com o {i}º valor: "))
    soma = soma + n

media = soma / 10
print(f"A média dos valores é {media:.2f}")
