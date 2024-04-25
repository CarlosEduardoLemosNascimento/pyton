# Elabore um algoritmo para ler o nome de um aluno, sua idade e as 3 notas.
# Caso a média do aluno seja menor que 7, o aluno está reprovado.
# Mostra: Nome, idade, média e se está aprovado ou reprovado.

import os
os.system("cls || clear")

# Variáveis

nome:str
idade:int
nota1:float
nota2:float
media:float

# Solicitando dados

print("=== INSIRA OS DADOS SOLICITADOS ===")
nome = str(input("Digite o nome do aluno: "))
idade = int(input("Digite a idade do aluno: "))
nota1 = float(input("Digite a 1ª nota do aluno: "))
nota2 = float(input("Digite a 2ª nota do aluno: "))

# Calculando a média
media = (nota1 + nota2)/2

os.system("cls || clear")

# Exibindo os dados

print("=== DADOS DO ALUNO E RESULTADO ===")
print(f"Nome do aluno: {nome}")
print(f"idade: {idade} anos")
print(f"1ª nota: {nota1}")
print(f"2ª nota: {nota2}")
print(f"Média: {media}")

if media <7:
    print("Resultado final: REPROVADO")
else:
    print("Resultado final: APROVADO")

print("=== FIM ===")
