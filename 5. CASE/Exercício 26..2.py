# Desenvolva um programa que receba como entrada um número inteiro que represente um dos 7 dias da semana.
# Imprima na tela se esse dia é útil ou é final de semana ou dia inválido

import os
import sys

os.system("cls || clear")


dia = int(input("Digite um número (de 1 a 7) referente a um dia da semana: "))

if dia >= 2 and dia <= 5:
    tipo = "Dia útil"
else:
    tipo = "Final de semana"

match(dia):
    case 1 :
        print(f"\nO número digitado corresponde ao Domingo - {tipo}")
    case 2 :
        print(f"\nO número digitado corresponde à segunda-feira - {tipo}")
    case 3 :
        print(f"\nO número digitado corresponde à terça-feira - {tipo}")
    case 4 :
        print(f"\nO número digitado corresponde à quarta-feira - {tipo}")
    case 5:
        print(f"\nO número digitado corresponde à quinta-feira - {tipo}")
    case 6:
        print(f"\nO número digitado corresponde à sexta-feira - {tipo}")
    case 7:
        print(f"\nO número digitado corresponde ao sábado - {tipo}")
    case _:
        print("\nOpção inválida")

