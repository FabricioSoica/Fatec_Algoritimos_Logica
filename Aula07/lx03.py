soma_peso = 0
soma_altura = 0
maior_imc = float('-inf')
menor_imc = float('inf')
imcs = []
status = []

for i in range(1, 6):
    print(f"Digite os dados da pessoa {i}:")
    peso = float(input("Peso (em kg): "))
    altura = float(input("Altura (em metros): "))

    imc = peso / (altura ** 2)
    imcs.append(imc)

    soma_peso += peso
    soma_altura += altura

    if imc > maior_imc:
        maior_imc = imc
    if imc < menor_imc:
        menor_imc = imc

    if imc < 18.5:
        status.append("Abaixo do peso")
    elif imc < 24.9:
        status.append("Peso normal")
    elif imc < 29.9:
        status.append("Acima do peso")
    else:
        status.append("Obesa")

peso_medio = soma_peso / 5
altura_media = soma_altura / 5

print("\nResultados:")
print(f"Peso médio: {peso_medio:.2f} kg")
print(f"Altura média: {altura_media:.2f} metros")
print(f"Maior IMC: {maior_imc:.2f} ({status[imcs.index(maior_imc)]})")
print(f"Menor IMC: {menor_imc:.2f} ({status[imcs.index(menor_imc)]})")
