# Escreva um programa que informe o valor e a forma de pagamento e calcule o valor a ser pago.

import os
import sys

os.system("cls || clear")

valorDaCompra:float = 0
desconto:float = 0
qdeParcelas:int = 0
valorDaParcela:float = 0
valorTotalPrazo:float = 0



while True:
    os.system("cls || clear")
    valorDaCompra = int(input("Digite o valor da compra: "))
    print("Digite a forma de pagamento: ")
    print("1 - Pagamento à vista.")
    print("2 - Pagamento à prazo.")
    opcao=int(input())

    match(opcao):
        case 1:

            os.system("cls || clear")
            desconto = valorDaCompra*0.1
            print("Opção de pagamento à vista")
            print(f"Valor do produto: R$ {valorDaCompra:.2f}")
            print(f"Valor do desconto: R$ {desconto:.2f}")
            print(f"Total a pagar: R$ {valorDaCompra-desconto:.2f}")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
                                        
        case 2:
            os.system("cls || clear")
            print("Opção de pagamento à prazo")
            qdeParcelas = int(input("Digite a quantidade de parcelas (1 a 12). "))
            print(f"Quantidade de parcelas: {qdeParcelas}")
            valorDaParcela = valorDaCompra / qdeParcelas
            print(f"Valor das parcelas: R$ {valorDaParcela:.2f}")
            valorTotalPrazo = valorDaParcela * qdeParcelas
            print(f"Valor total a prazo: R$ {valorTotalPrazo:.2f}")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
            
                            
        case _:
            os.system("cls || clear")
            input("\033[0;30;31mOpção inválida. Pressione qualquer tecla para continuar...\033[m")
            