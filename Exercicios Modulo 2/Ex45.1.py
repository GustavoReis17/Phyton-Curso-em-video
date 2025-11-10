"""
Exercício 045: Crie um programa que faça o computador
jogar Jokenpô (Pedra, Papel, Tesoura) com você.
(Versão 2: Usando Números)
"""
import random

print('''Escolha abaixo a opção que deseja jogar:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
      ''')

# Pedi a escolha como um número inteiro
Escolha = int(input('Qual a sua escolha? '))

# O computador sorteia um número de 1 a 3
Sorteado = random.randint(1, 3)

# --- A Lógica (Ifs Aninhados com Números) ---
# 1 = Pedra
# 2 = Papel
# 3 = Tesoura

# 1. O que acontece se EU joguei PEDRA (1):
if Escolha == 1 :
    if Sorteado == 1 :
        print('Empatou')
    elif Sorteado == 3: # PC jogou Tesoura
        print('Você ganhou') # Pedra (1) ganha de Tesoura (3)
    else: # PC jogou Papel (2)
        print('Você perdeu') # Pedra (1) perde para Papel (2)

# 2. O que acontece se EU joguei PAPEL (2):
elif Escolha == 2 :
    if Sorteado == 2 :
        print('Empatou')
    elif Sorteado == 1: # PC jogou Pedra
        print('Você ganhou') # Papel (2) ganha de Pedra (1)
    else: # PC jogou Tesoura (3)
        print('Você perdeu') # Papel (2) perde para Tesoura (3)

# 3. O que acontece se EU joguei TESOURA (3):
elif Escolha == 3 :
    if Sorteado == 3 :
        print('Empatou')
    elif Sorteado == 2: # PC jogou Papel
        print('Você ganhou') # Tesoura (3) ganha de Papel (2)
    else: # PC jogou Pedra
        print('Você perdeu') # Tesoura (3) perde para Pedra (1)

# 4. Se eu digitei qualquer outra coisa (4, 0, 5...)
else:
    print('Opção digitada invalida')