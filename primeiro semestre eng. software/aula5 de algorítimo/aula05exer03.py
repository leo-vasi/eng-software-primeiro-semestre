import os
os.system("cls")
print("Calculando o consumo médio de um automóvel")
distancia = float(input("Digite a distância percorrida em kms: "))
consumo = float(input("Digite quanto de combustível você gastou: "))
calculoCosumo = distancia / consumo
print(f"Você gastou: {calculoCosumo:.1f}" " litros")