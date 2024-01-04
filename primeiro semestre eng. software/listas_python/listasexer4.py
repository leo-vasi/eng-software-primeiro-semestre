import os
os.system("cls")
print("programa que recebe uma lista com 12 números e imprime quais são os números que estão armazenados nas posições de índice ímpar")
lista = []
for i in range(12):
    numero = int(input(f"Digite aqui o {i+1}º número: "))
    lista.append(numero)
num_impar = lista[0::2]
print(f"Números na posição ímpar: {num_impar}")