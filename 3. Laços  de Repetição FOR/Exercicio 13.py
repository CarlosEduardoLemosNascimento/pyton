# Escrever um algoritmo que mostre os números ímpares entre 1 e 20.

import os
os.system("cls || clear")

# Variáveis

i: int

# Exibindo a tabuada
os.system("cls || clear") 
for i in range(1, 20):
    if i%2 !=0:
        print(f"{i}")
