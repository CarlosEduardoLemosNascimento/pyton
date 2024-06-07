# Escreva um algorítimo que calcule a média aritimética de vários valores inteiros positivos inseridos pelo usuário
# O final da leitura será quando for inserido um número negativo
# Mostre a média aritimética dos números informados pelo usuário

import os
import sys

os.system("cls || clear")

def exibir_menu():
    os.system("cls || clear")
    print('\033[1;30;43m\u2573\u2573\u2573\u2573\u2573\u2573\u2573\u2573   M E N U  \u2573\u2573\u2573\u2573\u2573\u2573\u2573\u2573\033[m')
   
    #print("\u2573\u2573\u2573\u2573\u2573\u2573\u2573\u2573   M E N U  \u2573\u2573\u2573\u2573\u2573\u2573\u2573\u2573")
    print("\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501")
    print("\u2551\u2551 \033[0;30;33mOPÇÂO\033[m \u2551\u2551   \033[0;30;33mDESCRIÇÃO\033[m   \u2551\u2551")
    print("\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501")
    print("\u2551\u2551   1   \u2551\u2551 INSERIR NOTAS \u2551\u2551")
    print("\u2551\u2551   2   \u2551\u2551 EXIBIR MÉDIA  \u2551\u2551")
    print("\u2551\u2551   3   \u2551\u2551 APAGAR DADOS  \u2551\u2551")
    print("\u2551\u2551   4   \u2551\u2551      SAIR     \u2551\u2551")
    print("\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501\u2501")

valores = []
soma = 0
media = 0
quantidade = 0



while True:
    
    exibir_menu()
    
    opcao = int(input("Digite a opção desejada: "))

    match(opcao):
        case 1:
            exibir_menu()

            print("=== Inserindo valores ===")

            while True:
                valor = int(input("Digite um valor (Digite um número negativo  para sair): "))
                
                if valor < 0:
                    break
                valores.append(valor)
                soma = soma + valor
                quantidade = quantidade + 1

            media = soma / quantidade
                
        case 2:
            exibir_menu()

            if quantidade == 0:
                input("\033[0;30;31mNão foram digitados valores. Pressione qualquer tecla para retornar ao menu.\033[m")
                           
            else:
                print("=== Mostrando resultados ===\n")
                print(f"Média aritimética dos valores digitados: {media:.2f}")
                print(f"Quantidade de valores inseridos: {quantidade}")
                input("Pressione qualquer tecla para continuar...")

        case 3:
            os.system("cls || clear")
            soma = 0
            media = 0
            quantidade = 0
            exibir_menu()
            input("\033[0;30;32mDados apagados com sucesso! Pressione qualquer tecla para continuar...\033[m")
                        
        case 4:
            break
                    
        case _:
            exibir_menu()
            input("\033[0;30;31mOpção inválida. Pressione qualquer tecla para continuar...\033[m")
            