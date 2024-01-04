import os 
os.system('cls') 
print("Programa que lê uma lista com 4 números reais, em seguida o programa exibirá as notas e a média") 
notas = [] 
for i in range(4): 
    notas.append(int(input(f"Digite aqui a {i+1}ª nota: "))) 
    print(f"notas: {notas}") 
media = (notas[0] + notas[1] + notas[2] + notas[3]) / 4 
print(f"A média é: {media}") 