def converterPara12Horas(horas, minutos):
    if 0 <= horas < 24 and 0 <= minutos < 60:
        periodo = 'A.M.' if horas < 12 else 'P.M.'
        horas12 = horas if horas <= 12 else horas - 12
        return f"{horas12}:{minutos:02d} {periodo}"
    else:
        return "Horário inválido"

while True:
    try:
        horas24 = int(input("Digite as horas (formato de 24 horas): "))
        minutos = int(input("Digite os minutos: "))
        
        resultado = converterPara12Horas(horas24, minutos)
        print("A conversão para a notação de 12 horas é:", resultado)
    except ValueError:
        print("Por favor, insira valores numéricos para horas e minutos.")
    
    repetir = input("Deseja converter outro horário? (S para sim, qualquer outra tecla para sair): ").upper()
    if repetir != 'S':
        break
