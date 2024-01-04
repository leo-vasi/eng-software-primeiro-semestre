import os
os.system("cls")
print("Determinando o grau de obesidade de uma pessoa")
peso = float(input("Digite aqui o seu peso: "))
if peso > 0.4 and peso <= 300:
    altura = float(input("Digite aqui a sua altura: "))
else:
    print("Peso inválido")
if altura> 0.4 and altura <= 3:
        imc = peso / altura **2
else:
        print("Altura inválida")
if imc < 26:
        print ("Peso normal")
else:
        if imc < 30:
            print("Acima do peso")
        else:
            print("Obesidade morbida")
