import os

os.system("cls || clear")

# Função para exibir o menu
def exibir_cardapio():
    os.system("cls || clear")
    print("Cardápio:")
    for i in range(len(pratos)):
        print(f"{i+1} - Código do Prato {i+1}: {pratos[i][0]} - R${pratos[i][1]:.2f}")

# Função para calcular o subtotal
def calcular_subtotal(pedido):
    subtotal = 0
    for item in pedido:
        subtotal += pratos[item][1]
    return subtotal

# Função para calcular o total com desconto ou acréscimo
def calcular_total(subtotal, pagamento):
    if pagamento == 'vista':
        total = subtotal * 0.9  # Aplica desconto de 10% para pagamento à vista
        desconto_acrescimo = 'Desconto: 10%'
    elif pagamento == 'credito':
        total = subtotal * 1.1  # Aplica acréscimo de 10% para pagamento com cartão de crédito
        desconto_acrescimo = 'Acréscimo: 10%'
    return total, desconto_acrescimo

# Lista de pratos com seus respectivos códigos e preços
pratos = [
    ('Nome do Prato 1', 10),
    ('Nome do Prato 2', 15),
    ('Nome do Prato 3', 20),
    ('Nome do Prato 4', 25),
    ('Nome do Prato 5', 30),
    ('Nome do Prato 6', 35),
    ('Nome do Prato 7', 40)
]

# Lista para armazenar o pedido do usuário
pedido = []

# Loop para fazer os pedidos
while True:
    exibir_cardapio()
    codigo = input("Insira o código do prato (0 para finalizar o pedido): ")
    
    if codigo == '0':
        break

    codigo = int(codigo)
    if 1 <= codigo <= len(pratos):
        pedido.append(codigo - 1)
        print(f"{pratos[codigo-1][0]} adicionado ao pedido.")
        input("Pessione qualquer tecla para continuar")

    else:
        print("Código inválido. Tente novamente.")
        input("Pessione qualquer tecla para continuar")

# Solicitar a forma de pagamento
pagamento = input("Digite 'vista' para pagamento à vista ou 'credito' para pagamento no cartão de crédito: ").lower()

# Calcular o subtotal e o total a pagar
subtotal = calcular_subtotal(pedido)
total_a_pagar, desconto_acrescimo = calcular_total(subtotal, pagamento)

# Mostrar o resumo do pedido e o total a pagar
print("\nResumo do Pedido:")
for item in pedido:
    print(f"Código: {item + 1} - Nome: {pratos[item][0]}")

print("Forma de Pagamento:", "À vista" if pagamento == 'vista' else "Cartão de Crédito")
print(desconto_acrescimo)
print("Subtotal: R$", subtotal)
print("Total a Pagar: R$", total_a_pagar)