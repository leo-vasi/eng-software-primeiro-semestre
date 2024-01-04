import os
os.system("cls")
print("Algoritmo que receba o salário de N funcionários")
n = int(input("Digite aqui o número de funcionários: "))
a = 0 # Valor total pago a todos os funcionários
b = 0 # A quantidade de funcionários que recebem mais de R$ 2500.00
c = 0 # A quantidade de funcionário que funcionários que recebem menos de R$ 1300.00 
d = 0 # O valor total somando o salário de todos os funcionários que recebem menos de R$ 1300.00
for i in range(0, n+1):
    salario = float(input(f"Digite aqui o salário do {i+1}º funcionário: "))
    a += salario
    if salario <= 1300.00:
        c += 1
        d += salario
    elif salario > 2500.00:
        b += 1
if salario != 0:
    mediaSalario = a / n
else:
    mediaSalario = 0
if n != 0:
    percentual = (c / n) * 100
else:
    percentual = 0
print(f"O valor total pago a todos os funcionários é: {a}")
print(f"A quantidade de funcionários que recebem mais de 2500.00 é: {b}")
print(f"A média de salárial é: {mediaSalario}")
print(f"O percentual de funcionários que recebem menos de 1300.00 é: {percentual}")