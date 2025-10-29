"""
Exercício 025: Crie um programa que leia o nome de uma pessoa
e diga se ela tem "SILVA" no nome.
"""

# Pedi o nome completo da pessoa
Nome = str(input('Digite seu nome completo: '))

# 1. Eu joguei o nome todo para MAIÚSCULO com .upper()
#    (assim eu acho 'Silva', 'silva', 'SILVA', etc.)
# 2. Depois usei o .find() para procurar 'SILVA'.
Silva = Nome.upper().find('SILVA')

# O .find() retorna -1 se NÃO achar a palavra.
# Então, se o resultado for DIFERENTE (!=) de -1, é porque TEM SILVA.
if Silva != -1:
    print('Tem Silva no nome!')
else:
    # Corrigi o print aqui, faltou o "tem"
    print('Não tem Silva no nome!')