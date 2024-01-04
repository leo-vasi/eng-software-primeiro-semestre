import os
os.system("cls")
print("Jogo de adivinhação")
tentativas = 0
player1 = int(input("Digite aqui um número de 1 a 10: "))
if player1 <= 0 or player1 > 10:
    print("Erro, digite um número de 1 a 10")
else:
    player2 = int(input("Tente adivinhar o número entre 1 e 10: "))
    if player2 <= 0 or player2 >10:
        print("Erro, digite um número de 1 a 10")
    else:
        while player1 != player2:
            tentativas += 1
        while player2 == player2:
            break
        print(f"O segundo jogador acertou o número depois de {tentativas} tentativas")