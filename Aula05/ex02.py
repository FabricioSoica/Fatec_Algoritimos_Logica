nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))

nota_media = (nota1 + nota2 + nota3) / 3
nota_exame = 0

if nota_media <= 3:
    resultado = "Você foi reprovado!"
else:
    if nota_media < 7:
        resultado = "Você tem direito para fazer o exame!"
        nota_exame = 12 - nota_media
    else:
        resultado = "Parabéns, você foi aprovado!"

print(resultado)
if nota_exame != 0:
    print(f"tem que tirar no minio {nota_exame:5.2f} no exame para completar a sua nota")
