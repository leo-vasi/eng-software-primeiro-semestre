import os
os.system("cls")
print("Programa que recebe uma lista de 8 números inteiros e imprime quantos elementos múltiplos de 3 existem na lista.")
nums = []
for i in range(8):
    digito = int(input(f"Digite aqui o {i+1}º número: "))
    if digito % 3 == 0:
        nums.append(digito)
print(f"Dentro dessa lista, esses são os número multilplos de 3: {nums}")