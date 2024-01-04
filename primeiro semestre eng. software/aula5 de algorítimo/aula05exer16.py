import os
os.system("cls")
print("Calculando quanto de luz um cômodo precisará")
largura = float(input("Digite aqui a largura do cômodo: "))
comprimento = float(input("Digite aqui o comprimento do cômodo: "))
areaM2 = largura * comprimento
potencia = areaM2 * 18
print(f"A área é: {areaM2} metros quadrados e a potência da iluminação será: {potencia}W")
