import os

# Função para exibir o menu
def exibir_cardapio():
    os.system("cls || clear")
    print("Cardápio:")
    print("1 - Código do Prato 1: Nome do Prato 1 - R$10.00")
    print("2 - Código do Prato 2: Nome do Prato 2 - R$15.00")
    print("3 - Código do Prato 3: Nome do Prato 3 - R$20.00")
    print("4 - Código do Prato 4: Nome do Prato 4 - R$25.00")
    print("5 - Código do Prato 5: Nome do Prato 5 - R$30.00")
    print("6 - Código do Prato 6: Nome do Prato 6 - R$35.00")
    print("7 - Código do Prato 7: Nome do Prato 7 - R$40.00")

# Lista para armazenar o pedido do usuário
prato = []
valor = []

while True:
    exibir_cardapio()
    codigo = input("Insira o código do prato (0 para finalizar o pedido): ")

    if codigo == '0':
        break

    if codigo in cardapio:
        pedido.append(cardapio[codigo])
        print(f"{cardapio[codigo][0]} adicionado ao pedido.\n")
        print(f"{cardapio[codigo][0]} adicionado ao pedido.")
    else:
        print("Código inválido. Tente novamente.")
        print("Código inválido. Tente novamente.")