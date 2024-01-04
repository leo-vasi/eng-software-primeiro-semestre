import os
os.system("cls")
print("""algoritmo que imprime na tela os números de 1 a 100 exceto os números
múltiplos de 3.""")
for n in range(1, 101):
    if n % 3 != 0:
        print(n)
