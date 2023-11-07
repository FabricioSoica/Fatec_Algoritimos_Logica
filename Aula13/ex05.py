import math

def volume_da_esfera(raio):
    volume = (4/3) * math.pi * math.pow(raio, 3)
    return volume

raio = float(input("Digite o raio da esfera: "))
volume = volume_da_esfera(raio)
print(f"O volume da esfera é: {volume:.2f} ³")
