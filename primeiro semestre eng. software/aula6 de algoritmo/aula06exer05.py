import os
os.system("cls")
print("Calculando a conta final do hóspede")
nomeHospede = str(input("Digite aqui o seu nome: "))
tipoApt = str(input("Digite aqui o tipo de apartamento escolhido(entre A, B, C e D ): "))
quantidadeDiaria = int(input("Digite aqui quantas diárias foram feitas: "))
consumoIntern = float(input("Digite aqui o valor do seu consumo interno: "))
if tipoApt == "A" or tipoApt == "a":
    valorDiaria = 150.00
elif tipoApt == "B" or tipoApt == "b" :
    valorDiaria = 100.00
elif tipoApt == "C" or tipoApt == "c":
    valorDiaria = 75.00
elif tipoApt == "D" or tipoApt == "d" :
    valorDiaria = 50.00
else:
    print("Tipo de apartamento inválido")
valorTotalDiarias = quantidadeDiaria * valorDiaria
subtotal = valorTotalDiarias + consumoIntern
taxa = subtotal * 0.10
contaFinal = subtotal + taxa
print(f"\n\n\tConta Final \n\nNome do hóspede: {nomeHospede} \n\nTipo de apartamento: {tipoApt} \n\nQuantidade de diárias feitas: {quantidadeDiaria} \n\nValor das diárias: {valorDiaria} \n\nValor do consumo interno: {consumoIntern} \n\nSubtotal: {subtotal} R$ \n\nTaxa de 10% do subtotal: {taxa} \n\nValor total: {contaFinal}")
