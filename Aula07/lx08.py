def eh_primo(numero):
    for divisor in range(3, int(numero**0.5) + 1, 2):
        if numero % divisor == 0:
            return False
    return True


numero = int(input("Digite um número inteiro maior que 1: "))

if eh_primo(numero):
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")

'''

k =int(input("Entre com o númeero: "))
primo = True
n = 0
for i in range(1, n+1):
    if (k % i) == 0;
    n = n + 1

if n > 2
    primo = False
if primo:
    print(f"O número {k} é primo!!")
else:
    print(f"O número {k} não é primo!!")
    
'''