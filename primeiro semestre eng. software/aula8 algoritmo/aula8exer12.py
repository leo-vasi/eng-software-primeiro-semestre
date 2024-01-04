import os
os.system("cls")
print("""algoritmo que recebe duas notas de 60 alunos e calcula a média aritmética
para cada aluno.""")
aprovado = 0
reprovado = 0
exame = 0
for alunos in range(1, 61):
    nota1 = float(input("Digite aqui a sua 1ª nota: "))
    nota2 = float(input("Digite aqui a sua 2ª nota: "))
    media = (nota1 + nota2) / 2
    if media >= 5:
        aprovado += 1
    elif media >=3:
        reprovado +=1
    else:
        exame +=1
    print(f"Aprovados: {aprovado}")
    print(f"Reprovados: {reprovado}")
    print(f"Fazer exame: {exame}")