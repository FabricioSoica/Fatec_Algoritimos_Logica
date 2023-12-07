def reversoNumero(num):
    numStr = str(num)
    revStr = numStr[::-1]
    revNum = int(revStr)
    return revNum

numInformado = int(input("Digite um número inteiro: "))
reverso = reversoNumero(numInformado)

print(f"O reverso do número {numInformado} é: {reverso}")
