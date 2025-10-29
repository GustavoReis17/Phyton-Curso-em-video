"""
Exercício 024: Crie um programa que leia o nome de uma cidade
e diga se ela começa ou não com o nome "SANTO".
"""

# Pedi o nome da cidade
Cidade = str(input('Digite o nome da cidade: '))

# Eu fiz tudo em uma linha só, lendo da esquerda para a direita:
# 1. .strip()  -> Tirei os espaços inúteis do começo e do fim (ex: "  Santo... ")
# 2. .upper()  -> Joguei tudo pra maiúscula (ex: "SANTO ANDRÉ")
# 3. .split()  -> Quebrei a frase em uma lista de palavras (ex: ['SANTO', 'ANDRÉ'])
# 4. [0]       -> Peguei SÓ a primeira palavra dessa lista (ex: 'SANTO')
PrimeiraPalavra = Cidade.strip().upper().split()[0]

# Só precisei comparar se a primeira palavra é "SANTO"
if PrimeiraPalavra == 'SANTO':
    print('A cidade começa com Santo!')
else:
    print('A cidade não começa com Santo!')