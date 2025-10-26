"""
Exercício 005: Faça um programa que leia um número Inteiro
e mostre na tela o seu sucessor e seu antecessor.
"""

# Pedi um número inteiro
Numero = int (input('Digite um numero: '))

# --- O Cálculo ---
# Eu fiz o sucessor (Numero + 1) e o antecessor (Numero - 1)
# direto dentro do .format()
# Usei \n para quebrar a linha entre os dois.
print('O sucessor do seu numero é {} \nO antecessor do seu numero é {}'.format(Numero +1, Numero - 1))