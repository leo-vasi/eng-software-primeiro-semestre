import os 
os.system("cls") 
print("""Elaborar um programa que contém uma lista com 5 elementos. O usuário deve preencher essa lista. 
       Exibir no final os valores inseridos pelo usuário, porém os valores negativos (caso existirem) devem ser substituídos por zero (0)""") 
num = [] 
for i in range(5): 
    num.append(int(input(f"Digite aqui o {i+1}º número: "))) 
for i in range(5): 
    if num[i] < 0: 
        num[i] = 0 
for n in num: 
    print(n) 