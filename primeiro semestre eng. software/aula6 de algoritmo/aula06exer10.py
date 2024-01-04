import os
os.system("cls")
print("\t\tDeclaração de imposto de renda")
nome = str(input("\n\nDigite aqui o seu nome: "))
cpf = float(input("\n\nDigite aqui o seu cpf: "))
if cpf <= 500:
        print("Erro, digite seu CPF!")
else:
    rendaAnual = float(input("\n\nDigite aqui a sua renda anual: "))
if rendaAnual <= 0:
        print("Erro, digite sua renda anual!")
else:
    numDepen = float(input("\n\nDigite aqui o número de dependentes: "))
if numDepen >= 50:
        print("Erro, digite um número de dependentes válido!")
else:
        valor = rendaAnual - (numDepen * 110)
if valor <= 800:
        print("\n\nInsento")
elif valor > 800 and valor <= 4.000:
        resultado = valor * 0.025
        resultadoTotal = resultado + valor
        print(f"\n\nO valor será: {resultadoTotal}")
elif valor > 4.000 and valor < 9.000:
        resultado = valor * 0.05
        resultadoTotal = resultado + valor
        print(f"\n\nO valor será: {resultadoTotal}")
elif valor > 9.000:
        resultado = valor * 0.1
        resultadoTotal = resultado + valor
        print(f"\n\nO valor será: {resultadoTotal}")
else:
        print("Valores inválidos, digite os valores requisitados")