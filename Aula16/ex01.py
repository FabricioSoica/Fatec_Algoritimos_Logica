def patoCoelho(cabecas, pes):
    coelhos = (pes -(2*cabecas))/2
    patos = (-pes + (4*cabecas))/2

    return (patos,coelhos)

cabecas = int(input('Digite o numero total de cabeças:'))
pes = int(input('Digite o numero total de pes:'))
total = patoCoelho(cabecas, pes)
print(f'Total de patos: {int(total[0])}')
print(f'Total de coelhos: {int(total[1])}')