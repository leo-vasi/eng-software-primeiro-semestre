import os
os.system("cls")
print("""algoritmo que deixe escolher qual a tabuada de multiplicar que se deseja
imprimir""")
n = int(input("Digite aqui qual número: "))
for i in range(1, 11):
    r = n * i
    print(f"O número {n} * {i} = {r}")