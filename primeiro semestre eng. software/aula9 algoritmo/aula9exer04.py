import os
os.system("cls")
print("""\n\tCódigo do Lanche Especificação Preço Unitário(R$)
100 Cachorro quente 2,50
101 Bauru simples 2,00
102 Bauru c/ovo 3,50
103 Hamburger 5,10
104 Cheeseburger 3,30
105 Refrigerante 2,00""")
cardapio = {
    100: ("Cachorro quente", 2.50),
    101: ("Bauru simples", 2.00),
    102: ("Bauru c/ovo", 3.50),
    103: ("Hamburger", 5.10),
    104: ("Cheeseburger", 3.30),
    105: ("Refrigerante", 2.00)
}
continuar = True
total_pedido = 0.0
while continuar:
    codigo = int(input("Digite o código do lanche (ou 0 para encerrar o pedido): "))
    if codigo == 0:
        continuar = False
    elif codigo in cardapio:
        quantidade = int(input("Digite a quantidade desejada: "))
        if quantidade > 0:
            preco_unitario = cardapio[codigo][1]
            valor_item = preco_unitario * quantidade
            total_pedido += valor_item
            print(f"{quantidade}x {cardapio[codigo][0]}: R$ {valor_item:.2f}")
        else:
            print("A quantidade deve ser maior que zero.")
    else:
        print("Código de lanche inválido. Por favor, insira um código válido.")
print(f"Total do pedido: R$ {total_pedido:.2f}")
