import os
os.system("cls")
print("Quanto restará do salário de João após pagamento de suas dívidas")
salarioDeJoao = float(input("Digite aqui o seu salário: "))
conta1 = float(input("Digite aqui o valor da primeira conta: "))
conta2 = float(input("Digite aqui o valor da segunda conta: "))
contasComJuros = (conta1 * 0.02) + (conta2 * 0.02)
restoTotal = salarioDeJoao - contasComJuros
print(f"Sobrará {restoTotal} reais após o pagamento das contas com os juros inclusos.")