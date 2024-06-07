import os

os.system("cls || clear")

# Função para exibir o menu
def exibir_cardapio():
    os.system("cls || clear")
    print("\033[1;33m\t\tCARDÁPIO\033[m\n")
    print("Código\t Descrição\t\t Valor")
    print("==========================================")
    print("  1  \t Produto 01\t\t R$ 10,00")
    print("------------------------------------------")
    print("  2  \t Produto 02\t\t R$ 20,00")
    print("------------------------------------------")
    print("  3  \t Produto 03\t\t R$ 30,00")
    print("------------------------------------------")
    print("  4  \t Produto 04\t\t R$ 40,00")
    print("------------------------------------------")
    print("  5  \t Produto 05\t\t R$ 50,00")
    print("------------------------------------------")
    print("  6  \t Produto 06\t\t R$ 60,00")
    print("------------------------------------------")
    print("  7  \t Produto 07\t\t R$ 70,00")
    print("==========================================\n")

precos = [10,20,30,40,50,60,70]
produtos = ["Código 1 - Produto 01","Código 2 - Produto 02","Código 3 - Produto 03","Código 4 - Produto 04","Código 5 - Produto 05","Código 6 - Produto 06","Código 7 - Produto 07"]
pedido = []
valor_do_consumo = 0

while True:
    exibir_cardapio()
    codigo = int(input("Digite o código de um ítem para fazer o pedido (Digite 0 encerrar): "))
    if codigo == 0:
        confirmacao_saida = input("\nVocê optou em fechar a comanda. Tem certeza? Digite S ou N ").lower()
        if confirmacao_saida == "s":
            print("\nDigite a forma de pagamento: ")
            opcao_de_pagamento = input("Digite 1 para 'À vista' ou 2 para 'Cartão'. ")

            if opcao_de_pagamento == 1:
                forma_de_pagamento = "À vista"
                valor_final = valor_do_consumo * 0.9
                desconto_acrescimo = "Desconto de 10%"

            if opcao_de_pagamento == 2:
                forma_de_pagamento = "Cartão de crédito / débito"
                valor_final = valor_do_consumo * 1.1
                desconto_acrescimo = "Acrescimo de 10%"

            if opcao_de_pagamento != 1 and opcao_de_pagamento != 2:
                input("Opção inválida.Digite qualquer tecla para tentar novamente.")

            os.system("cls || clear")
            print("\033[1;33m\t\tCOMANDA\033[m\n")
            print("==========================================")
            print("Ítens consumidos")
            
            for i in range(len(pedido)):
                print(f"\t{pedido[i]}")
            print()
            print(f"Valor do consumo: R$ {valor_do_consumo:.2f}")
            print("Forma de pagamento: ",forma_de_pagamento)
            print(f"Observação: {desconto_acrescimo}")
            print(f"Valor cobrado: {valor_final:.2f}")
            break

    elif codigo >=1 and codigo <=7:
        os.system("cls || clear")
        exibir_cardapio()
        confirmacao_inclusao_item = input("\033[1;31mDeseja realmente incluir o ítem à comanda? Digite S ou N \033[m").lower()
        if confirmacao_inclusao_item == "s":
            pedido.append(produtos[codigo - 1])
            valor_do_consumo = valor_do_consumo + precos[codigo - 1]
            exibir_cardapio()
            print(f"\033[1;31mProduto adicionado à comanda com sucesso.\033[m")
            input("Digite qualquer tecla para continuar... ")
    
    else:
        os.system("cls || clear")
        exibir_cardapio()
        input("\033[1;31mOpçao ínvalida. Pressione qualquer tecla para retornar ao menu.\033[m")
        
    


