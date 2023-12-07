def soma(num1, num2, num3):
    resultado = num1 + num2 + num3
    return resultado

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))

resultSoma = soma(numero1, numero2, numero3)

print(f"A soma dos três números é: {resultSoma}")
