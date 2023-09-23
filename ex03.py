largura = float(input("Digite a largura do aposento em metros: "))
comprimento = float(input("Digite o comprimento do aposento em metros: "))

altura = 2.80
area_paredes = 2 * (largura + comprimento) * altura
area_porta = 0.80 * 2.10
area_total_a_pintar = area_paredes - area_porta

tipo_embalagem = input("Escolha o tipo de embalagem de tinta ( lata / galão / litro ): ")

if tipo_embalagem == "lata":
    quantidade_litros_por_embalagem = 18
elif tipo_embalagem == "galão":
    quantidade_litros_por_embalagem = 30
elif tipo_embalagem == "litro":
    quantidade_litros_por_embalagem = 1
else:
    print("Opção de embalagem inválida.")

quantidade_embalagens = area_total_a_pintar / quantidade_litros_por_embalagem
print(f"Quantidade de {tipo_embalagem}s necessárias: {quantidade_embalagens:.2f}")