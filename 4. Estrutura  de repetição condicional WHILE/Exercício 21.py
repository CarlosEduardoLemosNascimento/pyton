# Escrever um programa que solicite duas notas.
# Caso seja menor que 0 ou maior que 10, mostre a pergunta novamente
# Calcule e mostre a média 

import os
os.system("cls || clear")

QUANTIDADE_NOTAS = 2

# Variáveis

nota: float
i: int
soma: float
soma=0

for i in range(QUANTIDADE_NOTAS):
    while True:
        nota=int(input(f"Digite a {i+1}ª nota: "))

        if nota < 0 or nota > 10:
            print("Nota inválida. Por favor, tente novamentw. \n")
        else:
            soma=soma+nota
            break

        # Calculando valores

media=soma/QUANTIDADE_NOTAS

# Exibindo resultados
print("\n=== RESULTADO ===")
if media >=7:
    print(f"Média do aluno: {media:.2f}")
    print(f"Resultado: APROVADO")
elif media < 4:
    print(f"Média do aluno: {media:.2f}")
    print(f"Resultado: REPROVADO")
else:
    print(f"Média do aluno: {media:.2f}")
    print(f"Resultado: EM RECUPERAÇÃO")