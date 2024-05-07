# Escreva um algoritmo que solicite um número ao usuário e imprima a tabuada de multiplicar desse número

import os
os.system("cls || clear")

# Variáveis

numero: int
i: int

# Solicitando dados do usuário

numero=int(input("Digite número inteiro para exibir a tabuada de multiplicação: "))

 # Exibindo a tabuada
os.system("cls || clear") 
for i in range(1, 11):
    print(f"{numero} x {i} = {numero*i}")