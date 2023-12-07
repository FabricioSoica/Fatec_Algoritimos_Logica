def calcPagamento(val, diasAtraso):
    if diasAtraso == 0:
        return val
    else:
        multa = 0.03
        jurosDiarios = 0.001
        valPagar = val + (val * multa) + (val * jurosDiarios * diasAtraso)
        return valPagar

qtdPrest = 0
totalValPago = 0

while True:
    try:
        val = float(input("Digite o valor da prestação (ou 0 para encerrar): "))
        if val == 0:
            break
        
        diasAtraso = int(input("Digite o número de dias em atraso: "))
        
        valPagar = calcPagamento(val, diasAtraso)
        
        print(f"O valor a ser pago é: R${valPagar:.2f}")
        
        qtdPrest += 1
        totalValPago += valPagar
        
    except ValueError:
        print("Por favor, insira valores numéricos para a prestação e os dias em atraso.")

print("\nRelatório do Dia:")
print(f"Quantidade de prestações pagas: {qtdPrest}")
print(f"Total pago no dia: R${totalValPago:.2f}")
