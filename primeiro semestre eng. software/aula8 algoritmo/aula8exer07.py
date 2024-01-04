import os
os.system("cls")
print("Algoritmo que mostra o somatório de dos números de 1 a N")
n = int(input("Digite o valor de N: "))
s = 0
for cont in range (1,n+1):
    s = s + cont
print(f"A soma de 1 até {n} é de: {s}") 