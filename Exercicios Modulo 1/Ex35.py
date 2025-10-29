"""
Exercício 035: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

# Pega as três retas, usando float para aceitar números quebrados
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# A regra de ouro do triângulo:
# Um lado NUNCA pode ser maior que a soma dos outros dois.
# Por isso, checamos se todos os lados são menores que a soma dos outros.
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('Os segmentos PODEM FORMAR um triângulo!')
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo.')