import os
os.system("cls")
print("Menu de opções da calculadora")
operadores = float(input("\n\n\n\tMenu de opções \n\n1- Somar dois números. \n\n2- Multiplicar dois números \n\n3- Subtrair dois números \n\n4- Dividir dois números \n\nDigite aqui o número referente a operação desejada:  "))
num1 = float(input("Digite aqui o primeiro número: "))
num2 = float(input("Digite aqui o segundo número: "))
if operadores == 1:
    resultado = num1 + num2
    print(f"O resultado é: {resultado}")
elif operadores == 2:
    resultado = num1 * num2
    print(f"O resultado é: {resultado}")
elif operadores == 3:
    resultado = num1 - num2
    print(f"O resultado é: {resultado}")
elif operadores == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado é: {resultado}")
    else:
        print("Número inválido, tente denovo.")
else:
    print("Operação inválida, digite um número de 1 a 4 para selecionar a operação.")
       