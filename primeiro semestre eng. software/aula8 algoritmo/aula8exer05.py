import os 
os.system("cls")
print("Recebendo 20 números e imprimindo a metade de cada um deles")
for j in range(1,21):
    num = float(input("Digite um número: "))
    metade = num / 2
    print(f"A metade do valor {num} é: {metade}")