import os

os.system("cls || clear")

# Função para cálculo do INSS
def calcular_inss(salario_bruto):
    if salario_bruto <= 1100:
        desconto_inss = salario_bruto * 0.075
    elif salario_bruto > 1100 and salario_bruto <= 2203.48:
        desconto_inss = salario_bruto * 0.09
    elif salario_bruto  > 2203.48 and salario_bruto <= 3305.22:
        desconto_inss = salario_bruto * 0.12
    elif salario_bruto > 3305.22 and salario_bruto <= 6433.57:
        desconto_inss = salario_bruto * 0.14
    else:
        desconto_inss = 854.36
    
    if desconto_inss >= 854.36: # testanto o desconto para garantir o teto de R$ 854,36
        desconto_inss = 854.36
    return desconto_inss

# Função para cálculo do IRRF
def calcular_irrf(salario_bruto):
    if salario_bruto <= 2259.20:
        irrf = 0.0
        return irrf

    if salario_bruto >= 2259.21 and salario_bruto <= 2826.65:
        irrf = (salario_bruto * 0.075) - 189.59  # descontos de dependentes
        return irrf
    
    if salario_bruto > 2826.65 and salario_bruto <= 3751.05:
        irrf = (salario_bruto * 0.15) - 189.59
        return irrf
    
    if salario_bruto > 3751.05 and salario_bruto <=  4664.68:
        irrf = (salario_bruto * 0.225) - 189.59
        return irrf

    if salario_bruto > 4664.68:
        irrf = (salario_bruto * 0.275) - 189.59
        return irrf

# Solicitar matrícula e senha
matricula = input("Digite a matrícula do funcionário: ")
senha = input("Digite a senha do funcionário: ")

# Autenticação simulada

# Solicitar salário base
salario_base = float(input("Digite o salário base do funcionário: R$ "))

# Perguntar se o funcionário deseja receber vale transporte
opcao_vt = input("Deseja receber vale transporte? (s/n): ").lower()
if opcao_vt == 's':
    vale_transporte:float = salario_base * 0.06
else:
    vale_transporte:float = 0.0

# Perguntar valor do vale refeição
valor_vr = float(input("Digite o valor do vale refeição fornecido pela empresa: R$ "))
desconto_vr:float = valor_vr * 0.2

# Calcular descontos e acréscimos
inss:float = calcular_inss(salario_base)
irrf:float = calcular_irrf(salario_base)
plano_saude:float = 150.00 * 2  # desconto fixo de plano de saúde titular + dependente


# Calcular salário líquido
salario_liquido:float = (salario_base - inss - irrf - plano_saude - vale_transporte - desconto_vr)
print(type(desconto_vr))
print(type(vale_transporte))
print(type(plano_saude))
print(type(irrf))
print(type(inss))
print(type(salario_base))

# Exibir resultado

print("\nFolha de pagamento para o funcionário de matrícula", matricula)
print(f"Salário Base: R$ {salario_base:.2f}")
print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Desconto Vale Transporte: R$ {vale_transporte:.2f}")
print(f"Desconto Vale Refeição: R$ {desconto_vr:.2f}")
print(f"Desconto Plano de Saúde: R$ {plano_saude:.2f}")
print(f"\nSalário Líquido a Receber: R$ {salario_liquido:.2f}")
