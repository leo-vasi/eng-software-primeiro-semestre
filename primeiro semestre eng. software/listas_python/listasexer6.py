import os 
os.system("cls") 
print("Programa que recebe um lista de 15 números inteiros e que determine e mostre quantas vezes o número 0 foi repetido") 
num = [] 
for i in range(15): 
    numero = int(input(f"Digite aqui o {i+1}º número da lista: ")) 
    if numero == 0: 
        num.append(numero) 
print("o número zero se repetiu:", len(num),"vezes") 