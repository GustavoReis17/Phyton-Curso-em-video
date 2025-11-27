"""
Exercício 074: Crie um programa que vai gerar cinco números
aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados e
também indique o menor e o maior valor que estão na tupla.
"""

import random

# --- O Pulo do Gato (Tupla Packing) ---
# Eu chamei 'randint' 5 vezes, e o Python
# "empacotou" os 5 resultados na tupla 'numeros'.
numeros = (random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10),
           random.randint(1, 10))

print('=' * 30)
print(f'Os numeros são: {numeros} ')
print('=' * 30)

# --- A Mágica do Módulo 3 ---
# Eu não precisei de 'for' nem 'if' pra achar o maior.
# A função 'max()' já faz isso direto na tupla!
print(f'O maior é: {max(numeros)}')
print('=' * 30)

# A mesma coisa para o 'min()'
print(f'O menor é: {min(numeros)}')
print('=' * 30)