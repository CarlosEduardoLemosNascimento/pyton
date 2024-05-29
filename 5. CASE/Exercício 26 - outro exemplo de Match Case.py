# Algoritmo de calculadora

import os
import sys

os.system("cls || clear")

resultado = False

a = int(input("Digite o primeiro número: "))
while True:
    operador = input("Digite o operador: + - * / : ")
    
    if operador != '+' and operador != '-' and operador != '*' and operador != '/':
        print("Operador inválido")

    else:
        break

b = int(input("Digite o segundo número: "))

match(operador):
    case "+" :
        resultado = a + b
    case "-" :
        resultado = a - b
    case "*" :
        resultado = a * b
    case "/" :
        resultado = a / b
    case _:
        print("Operador inválido")

if resultado:
    print(f"\nResultado: {a} {operador} {b} = {resultado}")