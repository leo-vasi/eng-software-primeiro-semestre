import os
os.system("cls")
print("Algoritmo que receba a idade, o peso e a altura de 25 pessoas.")
a = 0 # # pessoas com mais de 90kg e menos de 1.60
b = 0 # pessoas com idade entre 21 e 30 que tem mais de 1.90 de altura
c = 0 # soma das idades para tirar média
for i in range(25):
    idade = int(input(f"Digite aqui a idade da {i+1}ª pessoa: "))
    altura = float(input(f"Digite aqui a altura da {i+1}ª pessoa: "))
    peso = int(input(f"Digite aqui o peso da {i+1}ª pessoa: "))
    c += idade
    if peso >= 90 and altura <= 1.60:
        a += 1
    elif idade >= 21 and idade <= 30 and altura >= 1.90:
        b += 1
if c != 0:
    mediaIdade = c / 5
percentual = (b / 5) * 100
print(f"A média de idade é: {mediaIdade}")
print(f"Quantidade de pessoas com 1.60 de altura e mais de 90kgs: {a}")
print(f"Percentual de pessoas com idade entre 21 e 30 e mais de 1.90 de altura: {percentual}")