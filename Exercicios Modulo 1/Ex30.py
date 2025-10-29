"""
Exercício 030: Crie um programa que leia um número inteiro
e mostre na tela se ele é PAR ou ÍMPAR.
"""

# Pedi um número inteiro para o usuário
Numero = int(input('Digite um numero inteiro: '))

# A Lógica do Par ou Ímpar
# Eu uso o operador % (módulo) para pegar o RESTO da divisão por 2.
# Se o resto for 0 (== 0), o número é PAR.
if Numero % 2 == 0:
    print(f'O Numero {Numero} é Par')
else:
    # Se o resto não for 0 (ou seja, for 1), o número é ÍMPAR.
    print(f'O Numero {Numero} é Impar')