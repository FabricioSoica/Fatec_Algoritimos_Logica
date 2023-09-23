numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Agora Digite o segundo número: "))

if numero1 == numero2:
    print(f"Os números são iguais")

else:
    if numero1 < numero2:
        print(f"O número {numero2} é o maior")

    if numero2 < numero1:
        print(f"O número {numero1} é o maior")