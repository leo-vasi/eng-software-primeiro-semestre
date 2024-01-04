import os
os.system("cls")
print("Calculando o número de horas trabalhadas")
salario = float(input("Digite aqui o seu salário: "))
horas_Trab = float(input("Digite aqui quantas horas você trabalhou: "))
valor_horas_trabalhada = salario / 2
salario_bruto = horas_Trab * valor_horas_trabalhada
salario_receber = salario_bruto - (salario_bruto * 0.03)
print(f"Salário a receber será: {salario_receber} reais")