import itertools

def quadradoMagico(matriz):
    tam = len(matriz)
    somaRef = sum(matriz[0])

    for i in range(tam):
        if sum(matriz[i]) != somaRef or sum(matriz[j][i] for j in range(tam)) != somaRef:
            return False

    if sum(matriz[i][i] for i in range(tam)) != somaRef or sum(matriz[i][tam - 1 - i] for i in range(tam)) != somaRef:
        return False

    return True

def gerarQuadradosMagicos(tam):
    nums = list(range(1, tam ** 2 + 1))
    quadradosMagicos = []

    for perm in itertools.permutations(nums):
        matriz = [list(perm[i:i+tam]) for i in range(0, len(perm), tam)]
        if quadradoMagico(matriz):
            quadradosMagicos.append(matriz)

    return quadradosMagicos

tamQuadrado = 3
quadradosMagicos = gerarQuadradosMagicos(tamQuadrado)

for quadrado in quadradosMagicos:
    print("Quadrado Mágico:")
    for linha in quadrado:
        print(linha)
    print()
