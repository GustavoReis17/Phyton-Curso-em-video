"""
Exercício 062: Melhore o DESAFIO 061, perguntando ao usuário
se ele quer mostrar mais alguns termos. O programa encerrará
quando ele disser que quer mostrar 0 termos.
"""

import time

# Pedi as informações iniciais
PrimeiroTermo = int(input('Digite o Primeiro termo: '))
Razao = int(input('Digite a Razão: '))

Termoatual = PrimeiroTermo

# --- Variáveis de Controle ---
# O contador de quantos termos já mostrei (começa em 1)
Cont = 1
# O objetivo total de termos a mostrar (começa em 10)
Totaldetermos = 10
# A variável que guarda quantos termos o usuário quer ver a mais
Mais = 10

print('=' * 30)
print(f'Os {Totaldetermos} primeiros termos dessa PA são:')
print('=' * 30)

# Loop "Mestre": Roda enquanto o usuário não digitar 0
while Mais != 0:

    # Loop "Escravo": Roda até atingir o objetivo (Totaldetermos)
    while Cont <= Totaldetermos:
        # 1. Mostra o termo
        print(Termoatual)
        time.sleep(0.3)
        # 2. Prepara o próximo
        Termoatual = Termoatual + Razao
        # 3. Incrementa o contador
        Cont += 1

    # Quando o loop "Escravo" termina, ele faz uma pausa
    print('=' * 30)
    # (Eu uso 'Cont - 1' porque o Cont já foi incrementado para o próximo)
    print(f'{Cont - 1} termos já mostrados.')
    print('=' * 30)

    # Pergunta se o usuário quer ver mais termos
    Mais = int(input('Deseja mostrar mais quantos termos? (0 para sair): '))

    # --- O PULO DO GATO ---
    # A mágica está aqui: eu atualizo o objetivo total
    # somando o que o usuário pediu.
    Totaldetermos = Totaldetermos + Mais

# Se o usuário digitou 0, o loop "Mestre" para
print('=' * 30)
print(f'Progressão finalizada com {Cont - 1} termos mostrados.')
print('ACABOU!')