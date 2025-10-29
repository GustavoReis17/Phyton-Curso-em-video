"""
Exercício 028: Escreva um programa que faça o computador "pensar" em um
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
o número escolhido pelo computador. O programa deverá escrever na tela
se o usuário venceu ou perdeu.
"""

# Para esse, eu precisei importar a biblioteca 'random'
import random

# Pedi o palpite do jogador (entre 0 e 5)
Numero = int (input('Digite um numero entre 0 a 5: '))

# Aqui é o computador "pensando" no número.
# Usei 'random.randint(0, 5)' porque ela sorteia um número
# incluindo o 0 e o 5 no sorteio.
X = random.randint(0,5)

# A lógica do jogo é só essa:
# Se o meu número for igual ao do computador, eu ganhei.
if Numero == X:
    print('Você venceu!')
else:
    # Senão, eu perdi.
    print('Você perdeu!')