import os 
os.system("cls") 
print("Programa que lê uma lista de 6 números inteiros e mostra cada número juntamente com a sua posição na lista") 
num_list = [] 
for i in range(6): 
    num_list.append(int(input(f"Digite aqui o {i+1}º número: "))) 
print(num_list) 
for x in num_list: 
    print(x) 
for pos, x in enumerate(num_list): 
    print(f"{pos} <-- {x}") 
for i in range(len(num_list)): 
    print(i) 