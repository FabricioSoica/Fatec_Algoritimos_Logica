def verPrimo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def qntPrimo(valores):
    qnt = 0
    for num in range(valores + 1):
        if verPrimo(num):
            qnt += 1
    return qnt

def script():
    y = int(input("Seus 2 números finais do RA: "))

    valor = y * 2 + 5
    listaPrimos = [num for num in range(valor + 1) if verPrimo(num)]

    print(f"Números primos até {valor}: {listaPrimos}")

    soma = sum(listaPrimos)
    print(f"Soma dos números primos: {soma}")

script()
