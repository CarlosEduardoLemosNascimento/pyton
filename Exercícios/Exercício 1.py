# Construa um algoritmo para ler dois números
# Em seguida calcule a soma, a subtração, a multiplicação e a divisão desses números, armazenando os resultados em variáveis
# Mostre os dados iniciais e os resultados
import os
os.system("cls || clear")

primeiroNumero: float
segundoNumero: float
soma: float
subtracao: float
multiplicacao: float
divisao: float

print("=== SOLICITANDO DADOS===\n")
primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))

soma = primeiroNumero + segundoNumero
subtracao = primeiroNumero - segundoNumero
multiplicacao = primeiroNumero * segundoNumero
divisao = primeiroNumero / segundoNumero

os.system("cls || clear")

print("=== EXIBINDO RESULTADOS ===\n")
print(f"Numeros digitados: {primeiroNumero} e {segundoNumero}")
print (f"Soma: {soma}")
print (f"Subtração: {subtracao}")
print (f"Multiplicação: {multiplicacao}")
print (f"Divisão: {divisao}")
