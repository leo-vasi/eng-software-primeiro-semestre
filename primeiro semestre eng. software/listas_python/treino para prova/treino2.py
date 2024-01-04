import os
os.system("cls")
print("Programa que receba a idade e o peso de 25 pessoas")
idadeSup40 = 0
peso60ou80 = 0
somadopeso = 0
for i in range(5):
    idade = int(input(f"Digite aqui a idade da {i+1}ª pessoa: "))
    peso = float(input(f"Digite aqui o peso da {i+1}ª pessoa: "))
    if idade > 40:
        idadeSup40 += 1
    elif peso >= 60 and peso <= 80:
        peso60ou80 += 1
if idadeSup40 != 0:
    mediaPeso = (peso + somadopeso) / idadeSup40
else:
    mediaPeso = 0
percentual = (peso60ou80 / 5) * 100
print(f"A média de peso é {mediaPeso}")
print(f"Número de pessoas com idade superior a 40: {idadeSup40}")
print(f"Percentual de pessoas com peso entre 60 e 80 quilos: {percentual:.2f}%")