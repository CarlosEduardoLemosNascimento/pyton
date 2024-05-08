# Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média.

import os
os.system("cls || clear")

# Variáveis

nota: float
soma: float
media: float
i: int


os.system("cls || clear")
nota=0
soma=0
media=0
# Pedindo os números ao usuário
for i in range(1, 5):
    nota=int(input(f"Digite a {i}ª nota: "))
    # Calculando valores
    soma=soma+nota
media=soma/4
        
# Exibindo resultados
print(f"\nMédia do aluno: {media:.2f}")
