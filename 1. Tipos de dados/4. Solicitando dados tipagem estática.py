nome:str
idade:int
peso:float
altura:float

nome = (input("Digite o seu nome: "))
idade = int(input("Digite s sua idade: "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

print("")
print("=== Exibindo dados coletados ===")
print(f"Nome: {nome}.")
print(f"Idade: {idade} anos.")
print(f"Peso: {peso} kg.")
print(f"Altura: {altura} m.")