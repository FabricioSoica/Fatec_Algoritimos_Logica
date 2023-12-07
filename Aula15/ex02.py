def verificarPosNeg(numero):
    if numero > 0:
        return 'Positivo'
    else:
        return 'Negativo'

numeroInserido = float(input("Digite um número: "))

resultVerificacao = verificarPosNeg(numeroInserido)

print(f"Resultado da verificação: {resultVerificacao}")
