N = int(input("Digite o valor de N: "))

soma = 0

for i in range(1, N + 1):
    termo = 2 ** i
    soma += termo

print("O valor de E =", soma)
