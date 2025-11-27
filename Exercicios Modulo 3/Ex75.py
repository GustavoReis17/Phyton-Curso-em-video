"""
Exercício 075: Desenvolva um programa que leia
quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

# 1. Pedi os 4 números
Numero1 = int(input('Digite o primeiro numero: '))
Numero2 = int(input('Digite o segundo numero: '))
Numero3 = int(input('Digite o terceiro numero: '))
Numero4 = int(input('Digite o quarto numero: '))

# 2. "Empacotei" eles na Tupla
Numeros = (Numero1, Numero2, Numero3, Numero4)
print(f'Você digitou os valores: {Numeros}')

# A) Contando o 9
print('=' * 30)
print(f'O numero 9 apareceu: {Numeros.count(9)} vezes.')

# B) Achando o 3
print('=' * 30)
# (O Pulo do Gato: Eu checo 'if 3 in Numeros' PRIMEIRO!)
# (Assim eu evito o erro se o 3 não existir)
if 3 in Numeros:
    # (E somei +1 para mostrar a 'posição' e não o 'índice', como no Ex do Flamengo)
    print(f'O primeiro 3 foi digitado na posição {Numeros.index(3) + 1}ª.')
else:
    print('O valor 3 não foi digitado em nenhuma posição.')

# C) Achando os pares
print('=' * 30)
print('Os números pares digitados foram: ', end='')
for numero in Numeros:
    if numero % 2 == 0:
        # (Usei end=' ' para imprimir todos na mesma linha)
        print(f'-> {numero}', end=' ')