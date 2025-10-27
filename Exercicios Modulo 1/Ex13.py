"""
Exercício 013: Faça um algoritmo que leia o salário de um funcionário
e mostre seu novo salário, com 15% de aumento.
"""

# Pedi o salário, usando float() para aceitar centavos (ex: 1500.50)
salario = float (input('Digite o valor do seu salario: R$'))

# --- O Cálculo do Aumento ---
# Eu fiz o cálculo todo direto dentro do .format() do print.
# 1. (salario * 0.15) -> Calculei quanto é 15% do salário (o aumento)
# 2. salario + (...)  -> Somei o aumento ao salário original
# 3. :.2f             -> Formatei o resultado final como dinheiro
print('O valor do seu novo salario com 15% de aumento é: R${:.2f}'.format(salario + (salario * 0.15)))