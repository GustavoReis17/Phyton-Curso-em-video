"""
Exercício 014: Escreva um programa que converta uma temperatura
digitada em °C e converta para °F.
"""

# Pedi a temperatura em Celsius, usando float para aceitar casas decimais
temp = float(input('Digite a temperatura em graus Celsius: '))

# --- A Fórmula da Conversão ---
# Essa é a fórmula matemática para converter Celsius para Fahrenheit:
# Multiplica por 9, divide por 5, e soma 32.
fah = (temp * 9/5) + 32

# Imprimi o resultado já formatado com 2 casas decimais (:.2f)
print('A temperatura em Fahrenheit é : {:.2f}'.format(fah))