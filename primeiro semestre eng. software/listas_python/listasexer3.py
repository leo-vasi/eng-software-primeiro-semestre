import os
os.system("cls")
print("Programa em Python que recebe uma lista com 9 valores numéricos, calcula e mostra a somatória dos números pares")
num = []
for i in range(9):
    digito = int(input(f"Digite aqui o {i+1}º número: "))
    if digito % 2 == 0:
        num.append(digito)
soma = sum(num)
print(f"A soma dos pares é: {soma}")
    