import os 
os.system("cls")
print("Programa que lê uma lista que contenha 20 números inteiros e em seguida o programa exibirá o maior e o menor número") 
num = [] 
for i in range(20+1): 
    num.append(int(input(f"Digite aqui o {i+1}º número: "))) 
maior = max(num) 
menor = min(num) 
print(f"O maior valor é: {maior} e o menor é: {menor}") 