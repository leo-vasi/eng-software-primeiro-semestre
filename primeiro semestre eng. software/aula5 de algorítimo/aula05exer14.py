import os
os.system("cls")
print("Calculando o novo peso de uma pessoa")
pesoAtual = float(input("Digite aqui o seu peso atual em quilos(kg): "))
engordar = pesoAtual + (pesoAtual * 0.15)
emagrecer = pesoAtual - (pesoAtual * 0.20)
print(f"O seu peso atual é {pesoAtual} quilos, mas se você egordar 15% terá {engordar} quilos , caso emagreça 20% terá {emagrecer} quilos.")