"""
Exercício 037: Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.
"""

# Pedi o número inteiro que eu quero converter
Numero = int (input('Digite um numero inteiro: '))

# --- O Pulo do Gato (Otimização) ---
# Eu já calculei as TRÊS conversões de uma vez, antes de perguntar.
# Usei as funções 'bin()', 'oct()' e 'hex()'
# e usei o fatiamento [2:] para cortar o prefixo (0b, 0o, 0x) de todas.
Binario = bin(Numero)[2:]
Octal = oct(Numero)[2:]
Hexadecimal = hex(Numero)[2:]

# Mostrei o menu de opções para o usuário
print('''Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

# Pedi a opção
opcao = int(input('Digite a opção desejada: '))

# --- Lógica de Decisão ---
# Agora o if/elif/else fica bem simples, só preciso
# checar a 'opcao' e imprimir a variável que eu já calculei lá em cima.

if opcao == 1:
    print('-' * 20)
    print(f'Seu numero é: {Numero}')
    print('-' * 20)
    print(f'Seu numero em Binario: {Binario}')

elif opcao == 2:
    print('-' * 20)
    print(f'Seu numero é: {Numero}')
    print('-' * 20)
    print(f'Seu numero em Octal: {Octal}')

elif opcao == 3:
    print('-' * 20)
    print(f'Seu numero é: {Numero}')
    print('-' * 20)
    print(f'Seu numero em hexadecimal: {Hexadecimal}')

else:
    # Se o usuário não digitou 1, 2 ou 3
    print('-' * 20)
    print('Você digitou uma opção invalida')
    print('-' * 20)