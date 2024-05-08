# Escrever um algoritmo que gera e escreve os números pares entre 100 e 120.

import os
os.system("cls || clear")

# Variáveis

i: int

# Exibindo a tabuada
os.system("cls || clear") 
for i in range(100, 121):
    if i % 2 == 0:
        print(f"{i}")
   