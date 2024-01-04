import os
os.system("cls")
print("Quanto irá sobrar de ração para gatos após 5 dias")
pesoSaco = float(input("Digite aqui o peso do saco em quilos: "))
pesoGramas = pesoSaco * 1000
racaoGato1 = float(input("Digite a quantidade de ração dada para o primeiro gato em um dia (em gramas): "))
racaoGato2 = float(input("Digite a quantidade de ração dada para o segundo gato em um dia (em gramas): "))
totalRacao = (racaoGato1 + racaoGato2) * 5
sobraRacao = pesoGramas - totalRacao
print(f"Após 5 dias irá sobrar: {sobraRacao:.2f} gramas")