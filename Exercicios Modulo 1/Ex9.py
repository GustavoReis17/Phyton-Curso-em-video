"""
Exercício 009: Faça um programa que leia um número Inteiro
qualquer e mostre na tela a sua tabuada.
"""

# Pedi o número da tabuada
Numero = int (input('Digite um numero: '))

# --- A Lógica (Modo Módulo 1 - "na mão") ---
# Eu fiz um print só para a tabuada inteira.
# Usei o \n (quebra de linha) para separar cada resultado.
#
# No .format(), eu passei os 10 cálculos em ordem:
# N*1, N*2, N*3, e assim por diante...
print(' x 1 = {} \n x 2 = {} \n x 3 = {} \n x 4 = {} \n x 5 = {} \n x 6 = {} \n'
      ' x 7 = {} \n x 8 = {} \n x 9 = {} \n x 10 = {}'.format(Numero * 1, Numero * 2, Numero * 3, Numero * 4, Numero * 5,Numero * 6, Numero * 7, Numero * 8, Numero * 9, Numero * 10))