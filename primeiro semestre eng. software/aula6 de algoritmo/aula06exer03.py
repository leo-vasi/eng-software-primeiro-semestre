import os
os.system("cls")
print("Checando classe eleitoral")
idade = int(input("Digite a sua idade: "))
if idade < 16:
    print("Não-eleitor(menor de idade)")
elif idade >= 18 and idade <= 65:
    print("Eleitor obrigatório")
else:
    print("Eleitor facultativo")   
    