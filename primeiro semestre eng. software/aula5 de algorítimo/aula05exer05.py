import os
os.system("cls")
print("Mostrando o valor de aumento de salário")
salario = float(input("Digite o seu salário atual: "))
percentual = float(input("Digite o percentual de aumento: "))
aumento = salario * percentual / 100
novoSalario = salario + aumento
print(f"O novo salário é: {novoSalario}")
