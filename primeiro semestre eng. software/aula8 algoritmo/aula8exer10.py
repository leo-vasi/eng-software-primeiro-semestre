import os
os.system("cls")
print("algoritmo que recebe N números e conta quantos destes números são pares")
n = int(input("Digite aqui a quantidade de números que você deseja verificar: "))
s = 0
for i in range(n):
    numero = int(input(f"Digite {i+1}º: "))
    if numero % 2 == 0:
        s += 1
print(f"Entre {n} números, {s} são pares")
