from random import randint

lista = [0]*7

for _ in range(6000):
    n = randint(1, 6)
    lista[n] = lista[n]+1

p = [0]*7

for i in range(1, 7):
    p[i] = (lista[i] / 6000) * 100
    print(f"{i} - {p[i]:.2f}% - {lista[i]}")


'''resultados = []

for _ in range(6000):
    lado = randint(1, 6)
    resultados.append(lado)

frequencia_faces = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

for resultado in resultados:
    frequencia_faces[resultado] += 1

for face, frequencia in frequencia_faces.items():
    print(f"Face {face}: {frequencia} vezes ({(frequencia / 6000) * 100:.2f}% do total)")'''



