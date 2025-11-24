"""
Exercício 068: Faça um programa que jogue par ou ímpar
com o computador. O jogo só será interrompido quando
o jogador PERDER...
"""

import random

Cont = 0

# 1. Loop "Mestre" (o Jogo)
while True:
    print('-' * 20)
    Numero = int(input('Digite um valor entre 0 e 10: '))
    print('-' * 20)

    Aposta = ' '
    # 2. Loop "Filhote" (SÓ para validar a aposta)
    while Aposta not in 'PI':
        Aposta = str(input('Deseja Par ou Impar (P/I)')).strip().upper()[0]
        # Se a aposta for inválida, ele avisa e o 'while' repete
        if Aposta not in 'PI':
            print('Opção inválida. Digite P ou I.')

    # --- LÓGICA DO JOGO (Agora está no Loop Mestre) ---

    # 3. O PC joga SÓ DEPOIS que a aposta for válida
    Pc = random.randint(1, 10)
    Soma = Numero + Pc

    print(f'Você jogou {Numero} e o PC jogou {Pc}. Total deu {Soma}')

    # 4. Checa se a Soma é PAR
    if Soma % 2 == 0:
        if Aposta == 'P':
            print('Você ganhou!')
            Cont += 1
        else:
            print('Você perdeu!')
            # 5. O 'break' quebra o "Loop Mestre"
            break

            # 5. Se a Soma for ÍMPAR
    else:  # (Se não é Par, é Ímpar)
        if Aposta == 'I':
            print('Você ganhou!')
            Cont += 1
        else:
            print('Você perdeu!')
            # 5. O 'break' quebra o "Loop Mestre"
            break

        # 6. O Fim do Jogo (Fora do 'while True')
print('=' * 40)
print(f'GAME OVER! Você obteve {Cont} vitórias consecutivas.')
print('=' * 40)