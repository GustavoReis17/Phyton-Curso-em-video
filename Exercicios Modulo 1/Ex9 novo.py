"""
Exercício 009 Novo: Faça um programa que leia um número Inteiro
qualquer e mostre na tela a sua tabuada.
"""

# Pedi o número da tabuada
Numero = int(input('Digite um numero '))

# Fiz um print pra ficar bonitinho
print('-' * 12)

# --- O Pulo do Gato (usando um 'for' loop) ---
# Eu poderia ter feito 10 prints na mão, um por um...
# Mas usei um 'for' loop (que é do Módulo 2!),
# que é muito mais inteligente.
#
# O 'range(1, 11)' cria uma contagem de 1 até 10.
for n in range(1, 11):
    # O {:2} aqui é um truque para alinhar os números (1, 2... 9)
    # se a tabuada for de um dígito só.
    print('{} x {:2} = {}'.format(Numero, n, Numero * n))

print('-' * 12)