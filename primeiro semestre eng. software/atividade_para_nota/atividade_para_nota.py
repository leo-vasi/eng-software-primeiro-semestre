import os
os.system("cls")
print("\n\tPrograma que recebe o número do operário, o número de peças fabricadas no mês e sexo do funcionário")
tot_folha = 0
tot_pecas = 0
media_m = 0
media_f = 0
cont_m = 0
cont_f = 0
SM = 724.00
for cont in range(1, 5+1):
    num_op = int(input("\nDigite aqui o número da operação: "))
    sexo_op = str(input("\nDigite aqui seu gênero, 'M' para masculino ou 'F' para feminino: ")).lower()
    pecas_op = int(input("\nDigite aqui quantas peças você produz: "))
    while sexo_op != 'm' and sexo_op != 'f':
        sexo_op = str(input("\nDigite aqui seu gênero, 'M' para masculino ou 'F' para feminino: ")).lower()
    if pecas_op <= 30:
        salario_op = SM
    else:
        if pecas_op > 30 and pecas_op <= 35:
            salario_op = SM + ((pecas_op - 30) * 3/100 * SM)
        else:
            salario_op = SM +  ((pecas_op - 30) * 5/100 * SM)
    print(f"O número da operação é {num_op} e o salário é {salario_op}")
    tot_folha = tot_folha + salario_op
    tot_pecas = tot_pecas + pecas_op
    if sexo_op == 'm':
        media_m += pecas_op
        cont_m += 1
    else:
        media_f += pecas_op
        cont_f += 1
    if cont == 1:
        salario_maior = salario_op
        num_maior = num_op
    else:
        if salario_op > salario_maior:
            salario_maior = salario_op
            num_maior = num_op
if cont_m == 0:
    media_m = 0
else:
    media_m = media_m / cont_m
if cont_f == 0:
    media_f = 0
else:
    media_f = media_f / cont_f
print("\n\n\n\t\t\tRelatório")
print(f"\n\n- O total da folha de pagamento da fábrica é: {tot_folha}")
print(f"- O número total de peças fabricadas no mês é: {tot_pecas}")
print(f"- A média de peças fabricadas por mulheres é: {media_f}")
print(f"- A média de peças fabricadas por homens é: {media_m}")
print(f"- O número do operário ou operária de maior salário é: {num_maior}")