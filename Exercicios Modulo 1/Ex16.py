"""
Exercício 016: Crie um programa que leia um número Real qualquer
pelo teclado e mostre na tela a sua porção Inteira.
"""

# Importei a 'math' só para usar a função 'trunc'
import math

# Pedi um número Real, então usei float() para aceitar ex: 6.127
Numero = float(input('Digite um numero Real: '))

# --- O Pulo do Gato ---
# Usei a função 'math.trunc()' (truncar)
# Ela "corta" o número na vírgula e joga a parte decimal fora.
# (Eu poderia ter usado 'int()' também, que teria o mesmo efeito)
Inteiro = math.trunc(Numero)

# Imprimi o resultado
print('A porção inteira do seu numero é: {}'.format(Inteiro))