def contarDigitos(num):
    num = abs(num)

    if num == 0:
        return 1

    count = 0
    while num > 0:
        num //= 10
        count += 1

    return count

numInformado = int(input("Digite um número inteiro: "))
qtdDigitos = contarDigitos(numInformado)

print(f"O número {numInformado} possui {qtdDigitos} dígitos.")
