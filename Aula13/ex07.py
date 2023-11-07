''' Crie uma função que recebe como parâmetro um número interio positivo, maior que zero. Esta função mostra (print)
quantidade de números que existe entre 1 e n
se n=3, ela imprimiria o valor 3, pois existem 3 números primos(1,2,3)
Se n=10, ela imprimiria o valor 5, pois existem 5 números primos(1,2,3,5,7) '''

from funcoes import eh_primo

def contar_numeros_primos(n):
    quantidade_primos = 0
    for i in range(1, n + 1):
        if eh_primo(i):
            quantidade_primos += 1
    return quantidade_primos

n = int(input("Digite um número inteiro positivo maior que zero: "))
quantidade_primos = contar_numeros_primos(n)
print(f"Existem {quantidade_primos} números primos entre 1 e {n}.")

