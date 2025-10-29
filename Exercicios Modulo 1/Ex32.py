"""
Exercício 032: Faça um programa que leia um ano qualquer
e mostre se ele é BISSEXTO.
"""

# Pede o ano para o usuário
Ano = int (input('Digite um ano: '))

#  Lógica do Ano Bissexto
# 1. (Ano % 4 == 0): Tem que ser divisível por 4
# 2. (and Ano % 100 != 0): ...E não pode ser divisível por 100 (essa é a exceção!)
# 3. (or Ano % 400 == 0): ...A MENOS que ele seja divisível por 400 (essa é a exceção da exceção!)
#
# Você acertou a regra completa!

if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f'O Ano {Ano} é Bissexto')
else:
    print(f'O Ano {Ano} não é Bissexto')