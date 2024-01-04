import os
os.system("cls")
print("\t\tCalculando o peso certo")
genero = str(input("\nDigite F se for mulher e H se for homem: ")).lower()
altura = float(input("\nDigite aqui sua altura: "))
if genero == "f":
    pesoCerto = (62.1 * altura) - 44.7
    print(f"\n\nSeu peso adequado é: {pesoCerto:.2f} kg")
elif genero == "h":
    pesoCerto = (72.7 * altura) - 58
    print(f"\n\nSeu peso adequado é: {pesoCerto:.2f} kg")
else:
    print("Valor inválido, digite F ou H para a seleção correta.")