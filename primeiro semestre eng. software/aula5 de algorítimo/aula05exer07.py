import os
os.system("cls")
print("Conversão de segundos em minutos")
segundos = float(input("Digite os segundos: "))
convMin = segundos / 60
convSeg = segundos % 60
print(f"O resultado da conversão é: {convMin:.0f} minutos e {convSeg:.0f} segundos")