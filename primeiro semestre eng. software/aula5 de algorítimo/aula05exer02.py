import os
os.system("cls")
print("Descobrindo o tempo necessário para download do seu arquivo")
arquivo = float(input("Informe o tamanho do arquivo: "))
velocidade = float(input("Informe aqui a velocidade de conexão: "))
tempo = arquivo / (velocidade * 8)
print(f"O tempo necessário para o download é: {tempo:.2f}")