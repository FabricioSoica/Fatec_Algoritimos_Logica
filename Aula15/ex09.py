import random

def embaralharPalavra(palavra):
    palavra = palavra.lower()
    charsEmbaralhados = random.sample(palavra, len(palavra))
    palavraEmbaralhada = ''.join(charsEmbaralhados)
    return palavraEmbaralhada

palavraOriginal = input("Digite uma palavra: ")
palavraEmbaralhada = embaralharPalavra(palavraOriginal)

print(f"A palavra embaralhada é: {palavraEmbaralhada}")
