# Escrever um programa que pergunte ao usuário se deseja inserir mais uma nota. Mostre um menu conforme abaixo:
# S - Inserir nota
# P - Ver quantas notas foram inseridas
# N - Calcular a média aritmética das notas informadas
# O programa deve mostrar a média para o usuário.

import os
import time
os.system("cls || clear")

contadorNotas = 0
soma = 0

while True:
    print("======================= MENU =======================")
    print("S - Inserir uma nota")
    print("P - Ver a quantidade de notas inseridas")
    print("N - Calcular a média aritmética das notas informadas")
    print("Z - Zerar contadores e valores")
    print("====================================================")

    resposta=input(f"Digite a opção: ")

    resposta = resposta.upper()

    if resposta == "S":
        nota=float(input(f"Digite uma nota: "))
        contadorNotas += 1
        soma += nota
        os.system("cls || clear")
    elif resposta == "P":
        if contadorNotas == 0:
            input("Não foram inseridas notas. Digite qualquer tecla para continuar... ")
            os.system("cls || clear")
        else:
            print(f"A quantidade de notas digitadas é {contadorNotas}")
            input("Digite qualquer tecla para continuar... ")
            os.system("cls || clear")
    elif resposta == "N":
        media=soma/contadorNotas
        print(f"A média aritmética das notas informadas é: {media:.2f}")
        input("Digite qualquer tecla para continuar... ")
        os.system("cls || clear")
    elif resposta == "Z":
        media=0
        soma=0
        contadorNotas=0
        input("Valores reiniciados. Digite qualquer tecla para continuar... ")
        os.system("cls || clear")
    else:
        break

