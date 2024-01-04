import os
os.system("cls")
print("Calculando a idade atual de uma pessoa e quantos anos ela terá em 2030")
anoNascimento = float(input("Digite em que ano você nasceu: "))
anoAtual = float(input("Digite o ano atual: "))
idadeAtual = anoAtual - anoNascimento
idade2030 = 2030 - anoNascimento
print(f"Você tem: {idadeAtual:.0f} anos" f" e em 2030 terá: {idade2030:.0f} anos")

