import os 
os.system("cls") 
print("Programa que recebe uma lista com 10 valores numéricos, gera uma nova lista onde cada elemento dessa lista é o quadrado dos elementos da primeira lista.") 
num = []
quadrado = [] 
for i in range(10): 
    valor = float(input(f"Digite aqui o {i+1}º valor númerico: ")) 
    if valor > 0: 
        x2 = valor ** 2 
    num.append(valor) 
    quadrado.append(x2) 
print(f"Lista: {num}") 
print(f"Lista ao quadrado: {quadrado}") 