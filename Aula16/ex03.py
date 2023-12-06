def calculos(string):

    somaDigitos = 0
    multDigitos = 1

    for digito in string:

        digitoInt = int(digito)

        somaDigitos += digitoInt

        multDigitos *= digitoInt

    return somaDigitos, multDigitos

string = input("Digite um número positivo no formato string: ")

soma, multiplicacao = calculos(string)

print(f"Soma dos dígitos: {soma}")
print(f"Multiplicação dos dígitos: {multiplicacao}")

# RA 3011392323002