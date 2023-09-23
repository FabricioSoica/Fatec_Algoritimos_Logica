preco = float(input("Digite o valor da compra: R$ "))

if preco <= 1000:
    desconto = preco * 0.10
elif preco <= 5000:
    desconto = preco * 0.20
else:
    desconto = preco * 0.30

preco = preco - desconto

print(f"Desconto aplicado: R$ {desconto:.2f}")
print(f"Valor total com desconto: R$ {preco:.2f}")