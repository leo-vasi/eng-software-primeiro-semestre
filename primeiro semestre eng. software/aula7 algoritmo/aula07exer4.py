import os
os.system("cls")
print("Calculando a conta final do hóspede")
nomeHospede = str(input("Digite aqui o seu nome: "))
tipoApt = str(input("Digite aqui o tipo de apartamento escolhido(entre A, B, C e D ): ")).lower()
if tipoApt != "a" and tipoApt != "b" and tipoApt != "c" and tipoApt != "d":
    print("Erro, digite uma opção válida!")
else:
    quantidadeDiaria = int(input("Digite aqui quantas diárias foram feitas: "))
    if quantidadeDiaria < 0 or quantidadeDiaria >= 25:
        print("Digite uma quantia válida!")
    else:
        consumoIntern = float(input("Digite aqui o valor do seu consumo interno: "))
        if consumoIntern < 0:
            print("Erro, digite uma quantia válida!")
        else:
            match tipoApt:
                case "a":
                    valorDiaria = 150.00
                case "b":
                    valorDiaria = 100.00
                case "c":
                    valorDiaria = 75.00
                case "d":
                    valorDiaria = 50.00
valorTotalDiarias = quantidadeDiaria * valorDiaria
subtotal = valorTotalDiarias + consumoIntern
taxa = subtotal * 0.10
contaFinal = subtotal + taxa
print(f"\n\n\tConta Final \n\nNome do hóspede: {nomeHospede} \n\nTipo de apartamento: {tipoApt} \n\nQuantidade de diárias feitas: {quantidadeDiaria} \n\nValor das diárias: {valorDiaria} \n\nValor do consumo interno: {consumoIntern} \n\nSubtotal: {subtotal} R$ \n\nTaxa de 10% do subtotal: {taxa} \n\nValor total: {contaFinal}")
