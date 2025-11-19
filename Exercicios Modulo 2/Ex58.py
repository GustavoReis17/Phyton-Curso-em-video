"""
Exercício 058: Melhore o jogo do DESAFIO 028 onde o computador vai
"pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.
"""

import random

# Comecei meus contadores/flags.
# O 'Numero' e 'Sorteado' com valores diferentes só pra forçar o 'while' a rodar.
Numero = 0
Cont = 0
Sorteado = 1  # (O PC não vai sortear 0 ou 1, mas o 'while' checa na primeira volta)

# O loop vai rodar "enquanto o palpite for diferente do sorteado"
while Numero != Sorteado:
    Numero = int(input('Acerte o numero entre 0 e 10: '))

    # --- O Pulo do Gato (Modo Difícil!) ---
    # Eu COLOQUEI O SORTEIO AQUI DENTRO do 'while' DE PROPÓSITO!
    # Isso faz o computador "pensar" em um NOVO número a cada palpite.
    # O jogador tá tentando acertar um alvo que se mexe!!
    # (O "Modo Fácil" seria colocar essa linha FORA do 'while',
    #  para o PC pensar em UM número só.)
    Sorteado = random.randint(0, 10)

    # Somei +1 tentativa
    Cont += 1

    # Se o palpite for diferente do NOVO número sorteado...
    if Numero != Sorteado:
        print('=' * 20)
        print('Você perdeu !!')
        # Eu imprimo qual foi o número que ele sorteou *dessa vez*
        print(f'(O PC pensou no {Sorteado} agora)')
        print('=' * 20)

# O programa SÓ sai do 'while' no momento de sorte em que
# o palpite do jogador for IGUAL ao número que o PC
# acabou de sortear.
print('=' * 50)
print('Parabéns você acertou!')
print('=' * 50)
print(f'O numero digitado foi {Numero} com {Cont} tentativas,')
print('=' * 50)