"""
Exercício 052: Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
"""

import time

# Pedi o número que eu quero testar
Numero = int(input('Digite um numero inteiro: '))

# 1. Criei o meu "contador" de divisores, começando em 0
Divisores = 0

# 2. Criei o loop para testar TODOS os números
#    de 1 até o próprio 'Numero' (por isso o '+ 1')
for i in range(1, Numero + 1):

    # 3. Chequei se o resto da divisão de 'Numero' por 'i' é 0
    if Numero % i == 0:
        # Se for 0, 'i' é um divisor!
        print(f'-> {i} (é divisor)')
        # E somo 1 no meu contador
        Divisores += 1
        time.sleep(0.3)
    else:
        # Se não for 0, 'i' não é um divisor
        print(f'-> {i} (não é divisor)')
        time.sleep(0.1)  # (Botei um sleep menor aqui)

# 4. No final do loop, eu mostro o total de divisores que achei
print(f'\nO número {Numero} foi divisível {Divisores} vezes.')
print('=' * 50)

# 5. A REGRA FINAL:
#    Se o contador for EXATAMENTE 2 (só 1 e ele mesmo), é PRIMO.
if Divisores == 2:
    print('E por isso ele É PRIMO!')
else:
    # Se for 1 (só o número 1) ou mais de 2, NÃO é primo.
    print('E por isso ele NÃO É PRIMO!')