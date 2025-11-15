"""
Exercício 053: Crie um programa que leia uma frase qualquer
e diga se ela é um palíndromo, desconsiderando os espaços.
"""

# 1. Pedi a frase e já "limpei" (sem espaços inúteis e maiúscula)
frase = str(input('Digite uma frase: ')).strip().upper()

# 2. Criei a versão "junta" (sem espaços no meio)
#    Primeiro eu quebro em lista (split) e depois junto (join)
palavras = frase.split()
frase_junta = ''.join(palavras) # Ex: "APOSASOPA"

# 3. Criei o inverso "na mão", usando o 'for'
inverso = ''
# Usei o 'for' para ler a 'frase_junta' de trás pra frente
for i in range(len(frase_junta) - 1, -1, -1):
    inverso += frase_junta[i] # Fui colando as letras no 'inverso'

print(f'O inverso de {frase_junta} é {inverso}')

# 4. Comparei as duas
if inverso == frase_junta:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO.')