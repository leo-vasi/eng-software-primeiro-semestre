import os 
os.system("cls")
print("Exibindo todos os números pares entre 1 a N")
n = int(input("Digite um número: "))
k = 1
for k in range (1,n+1,2):
    print(f"{k}")