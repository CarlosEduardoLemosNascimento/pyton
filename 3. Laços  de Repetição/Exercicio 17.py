# Escrever um programa de computador que solicite do usuário 3 notas 
# Ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado.

#Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.

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
for i in range(1, 4):
    nota=int(input(f"Digite a {i}ª nota: "))
    # Calculando valores
    soma=soma+nota
media=soma/3
        
# Exibindo resultados
if media >=7:
    print(f"\nMédia do aluno: {media:.2f}")
    print(f"\nResultado: APROVADO")
elif media < 4:
    print(f"\nMédia do aluno: {media:.2f}")
    print(f"\nResultado: REPROVADO")
else:
    print(f"\nMédia do aluno: {media:.2f}")
    print(f"Resultado: EM RECUPERAÇÃO")