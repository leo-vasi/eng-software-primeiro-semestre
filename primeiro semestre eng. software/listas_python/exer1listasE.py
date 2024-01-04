import os
os.system("cls")
print("Todos os múltiplos de 2, 3 e 4")
numero = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
dados = []
for x in numero:
    if x % 2 == 0 and x % 3 == 0 and x % 4 == 0:
        dados.append(x)
print(f"E: {dados}")