"""
Exercício 008: Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e milímetros.
"""

# Pedi a medida em Metros.
# Usei float() para o caso de a pessoa digitar ex: 1.80m
Metros = float (input('Digite quantos Metros: '))

# --- Os Cálculos ---
# Eu fiz as duas conversões direto dentro do .format()
# 1. Metros * 100 = Centímetros
# 2. Metros * 1000 = Milímetros
#
# Também usei o \n para quebrar a linha entre os dois resultados.
print( 'A medida em centimetros é {} \nA medida em milimetros é {}'.format(Metros * 100, Metros * 1000))