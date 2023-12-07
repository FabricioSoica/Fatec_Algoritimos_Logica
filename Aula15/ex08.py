import random

def jogarCraps():
    input("Pressione Enter para lançar os dados...")
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    print(f"Você lançou os dados: {dado1} + {dado2} = {total}")

    if total in (7, 11):
        print("Você ganhou! É um 'natural'.")
    elif total in (2, 3, 12):
        print("Você perdeu! É 'craps'.")
    else:
        ponto = total
        print(f"Seu Ponto é {ponto}. Continue lançando os dados.")

        while True:
            input("Pressione Enter para lançar os dados novamente...")
            dado1 = random.randint(1, 6)
            dado2 = random.randint(1, 6)
            novoTotal = dado1 + dado2
            print(f"Você lançou os dados novamente: {dado1} + {dado2} = {novoTotal}")

            if novoTotal == ponto:
                print("Você ganhou! Tirou o Ponto novamente.")
                break
            elif novoTotal == 7:
                print("Você perdeu! Tirou um 7 antes de tirar o Ponto novamente.")
                break

while True:
    jogarCraps()
    jogarNovamente = input("Deseja jogar novamente? (s/n): ").lower()
    if jogarNovamente != 's':
        break
