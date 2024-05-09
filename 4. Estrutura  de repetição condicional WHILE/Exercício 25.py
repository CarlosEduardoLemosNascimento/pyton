# Escrever um programa que pergunte calcule a média aritmética de valores inteiros positivos inseridos pelo usuário.
# O final da leitura acontecerá quando for inserido um valor negativo.
# Mostre a média dos números informados pelo usuário

import os
import time

os.system("cls || clear")
contador:int=0
soma:int=0
media:float=0

while True:
    valor = int(input("Insira um número inteiro positivo (ou um número negativo para sair): "))
    os.system("cls || clear")
    if valor > 0:
        soma = soma + valor
        contador = contador +1
        
    else:
        break
    os.system("cls || clear")
    media = soma / contador
print(f"A média dos números informados é: {media}")
