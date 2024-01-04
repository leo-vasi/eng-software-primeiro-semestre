import os
os.system("cls")
print("Programa que recebe uma lista com 10 números reais e imprime os números maiores que 15")
num = []
for i in range(10):
    digito = int(input(f"Digite aqui o {i+1}º número: "))
    if digito > 15:
        num.append(digito)
print(f"Os números maiores que 15 nessa lista são: {num}")