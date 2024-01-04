import os
os.system("cls")
print("\nLendo a idade de 1000 pessoas e exibindo suas respectivas classes eleitorais")
n = 0
o = 0
f = 0
for i in range(1, 5):
    idade = int(input("\n\nDigite aqui a sua idade: "))
    if idade <16:
        n += 1
    elif idade >= 18 and idade <= 65:
        o += 1
    else:
        if idade >= 16 and idade >65:
            f += 1
print(f"\nNão eleitores: {n}")
print(f"\nEleitor obrigatório: {o}")
print(f"\nEleitor facultativo: {f}")