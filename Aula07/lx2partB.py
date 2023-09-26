while True:
    base = float(input("Entre com a base: "))
    altura = float(input("Entre com a altura: "))
    if base and altura >0:
        print("O valor digitado é inválido")
        break

area = (base * altura) / 2

print(f"O valor de sua area é {area:5.2f}!!")