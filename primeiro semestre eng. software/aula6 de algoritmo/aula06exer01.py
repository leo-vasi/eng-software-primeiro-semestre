import os
os.system("cls")
print("\tCalculando média do aluno")
media = float(input("Digite a sua média: "))
if media > 10:
    print("Erro, número inválido!")
elif media < 0:
    print("Erro, número inválido!")
elif media >= 5:
    situacao = "Aprovado"
elif 3 <= media < 5:
    situacao = "Exame"
else:
    situacao = "Reprovado"
print(f"Situação do aluno: {situacao}")
