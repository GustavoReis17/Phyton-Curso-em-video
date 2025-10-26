"""
Exercício 006: Crie um algoritmo que leia um número
e mostre o seu dobro, triplo e raiz quadrada.
"""

# Pedi o número para o usuário
Numero = int(input('Digite um numero: '))

# --- Os Cálculos ---
# Fiz tudo em um print só, usando \n para quebrar as linhas.
# 1. Dobro = Numero * 2
# 2. Triplo = Numero * 3
# 3. Raiz Quadrada = Numero ** 0.5
print('O dobro do seu numero é: {} \nO triplo do seu numero é: {} \nA Raiz quadrada do seu numero é: {}'.format(Numero * 2, Numero * 3, Numero ** 0.5))