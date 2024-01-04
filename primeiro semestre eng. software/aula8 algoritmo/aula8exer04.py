import os 
os.system("cls")
print("Mostrando o quadrado de números")
n = int(input("Digite o número de repetições: "))
for k in range (1,n+1):
    num = float(input(f"Digite o {k} a número: "))
    q = num **2
    print(f"O quadrado de {num} é {q}")