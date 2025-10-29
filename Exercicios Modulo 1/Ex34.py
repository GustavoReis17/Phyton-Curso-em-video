"""
Exercício 034: Escreva um programa que pergunte o salário de um funcionário
e calcule o valor do seu aumento. Para salários superiores a R$1.250,00,
calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

# Pede o salário, float é importante aqui
Salario = float (input('Digite o valor do seu salario: '))

# Checa a condição principal: <= 1250 ganha 15%
if Salario <= 1250:
    # Calcula o novo salário (Salário + 15% de aumento)
    Salario = (Salario * 0.15) + Salario
else:
    # Se for maior, calcula o novo salário (Salário + 10% de aumento)
    Salario = (Salario * 0.10) + Salario

# Imprime o resultado já formatado como dinheiro (:.2f)
print(f'O valor do seu novo Salario é R${Salario:.2f}')