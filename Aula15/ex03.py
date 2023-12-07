def somaImposto(taxaImposto, custo):

    imposto = custo * (taxaImposto / 100)
    
    custoComImposto = custo + imposto
    
    return custoComImposto

taxa = float(input("Digite a taxa de imposto sobre vendas em porcentagem: "))
custoItem = float(input("Digite o custo do item antes do imposto: "))

novoCusto = somaImposto(taxa, custoItem)

print(f"O novo custo do item, incluindo o imposto, é: {novoCusto}")
