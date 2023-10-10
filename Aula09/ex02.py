'''vetor = []

for i in range(5):
    elemento = int(input(f"Digite o {i+1}º elemento: "))
    vetor.append(elemento)

maior_valor = vetor[0]
posicao_maior_valor = 0

for i in range(1, len(vetor)):
    if vetor[i] > maior_valor:
        maior_valor = vetor[i]
        posicao_maior_valor = i

print(f"O maior valor é {maior_valor} e está na posição {posicao_maior_valor}.") '''


lista = []
for i in range(5):
    lista.append(int(input(f"digite o número {i+1}: ")))

pos = 0
maior = lista[pos]

for i in range(0, len(lista)):
    if lista[i] >= maior:
        maior = lista[i]
        pos = i

print(f"O maior elemento é {maior} no índice {pos}.")
