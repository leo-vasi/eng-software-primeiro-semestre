import os
os.system("cls")
print("Programa que lê para cada candidato, o tempo de experiência em anos e o sexo de 30 candidatos")
cont_tc = 0  # total de candidatos
cont_cm = 0  # total de candidatos masculinos
cont_cf = 0  # total de candidatos femininos
cont_exp = 0  # total de candidatos que têm entre 2 e 4 anos de experiência
for i in range(30):
    temp_exp = int(input(f"Digite aqui quantos anos de experiência o {i+1}º candidato(a) tem: "))
    sexo = str(input(f"Digite aqui o sexo do {i+1}º candidato(a): (F para feminino ou M para masculino) ")).lower()
    if sexo == 'm':
        cont_tc += 1
        cont_cm += 1
    elif sexo == 'f':
        cont_tc += 1
        cont_cf += 1
    if temp_exp >= 2 and temp_exp <= 4:
        cont_exp += 1
if cont_cm != 0:
    mediaF = cont_cf / cont_cm
else:
    mediaF = 0
percentual = (cont_exp / cont_tc) * 100
print(f"Total de candidatos homens: {cont_cm}")
print(f"Média de tempo das candidatas mulheres: {mediaF}")
print(f"Percentual de candidatos com experiência entre 2 e 4 anos: {percentual}")