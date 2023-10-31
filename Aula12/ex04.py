lista1 = []
lista2 = []

print("Digite os elementos da primeira lista:")
for i in range(5):
    elemento1 = int(input("Elemento {}: ".format(i+1)))
    lista1.append(elemento1)

print("Digite os elementos da segunda lista:")
for i in range(5):
    elemento2 = int(input("Elemento {}: ".format(i+1)))
    lista2.append(elemento2)

uniao = set(lista1) | set(lista2)

print("Conjunto da união das duas listas:", uniao)
