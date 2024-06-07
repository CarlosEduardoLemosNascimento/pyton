# Escreva um programa utilizando o cpmandp caso-escolha que imprima um mês de ano de acordo com o número digitado pelo usuário
# 1... janeiro, 2... fevereiro...

import os
import sys

os.system("cls || clear")

opcao = 0



while True:
    os.system("cls || clear")
    opcao = int(input("Digite um número (1 a 12) para saber o mês correspondente. Digite 0 para sair. "))

    match(opcao):
        case 1:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Janeiro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
                                        
        case 2:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Fevereiro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
            
        case 3:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Março.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
                                    
        case 4:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Abril.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")

        case 5:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Maio.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")

        case 6:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Junho.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 7:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Julho.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 8:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Agosto.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 9:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Setembro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 10:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Outubro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 11:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Novembro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")
         
        case 12:
            os.system("cls || clear")
            print("A opção digitada corresponde ao mês de Dezembro.")
            input("\033[0;30;31mPressione qualquer tecla para continuar...\033[m")

        case 0:
            os.system("cls || clear")
            print("Obrigado!")
            break
                    
        case _:
            os.system("cls || clear")
            input("\033[0;30;31mOpção inválida. Pressione qualquer tecla para continuar...\033[m")
            