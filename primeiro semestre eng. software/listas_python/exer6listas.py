import os 
os.system("cls") 
print("Elaborar um programa para ler uma lista A de 15 elementos e um valor X. O programa deve copiar para a lista B somente os elementos de A que são maiores que X. Exibir no final a lista B.") 
listaA = [] 
listaB = [] 
for i in range(15): 
    listaA.append(int(input(f"Digite aqui o {i+1}º número da lista A: "))) 
x = int(input("Digite aqui um valor qualquer: ")) 
for i in range(15): 
    if listaA[i] > x: 
        listaB.append(listaA[i]) 
print(f"Lista A: {listaA}") 
print(f"Valor X: {x}") 
print(f"Lista B: {listaB}") 