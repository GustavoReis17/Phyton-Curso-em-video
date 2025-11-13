"""
Exercício 051: Desenvolva um programa que leia o primeiro termo
e a razão de uma PA (Progressão Aritmética). No final,
mostre os 10 primeiros termos dessa progressão.
"""

# Importei o 'time' para a pausa
import time

# Pedi o primeiro termo e a razão
# (Eu usei int(), então minha PA vai ser só com números inteiros)
PrimeiroTermo = int(input('Digite o Primeiro termo: '))
Razao = int(input('Digite a Razão: '))

# Comecei o 'Termoatual' com o 'PrimeiroTermo'
Termoatual = PrimeiroTermo

print('=' * 30)
print('Os 10 primeiros termos dessa PA são:')
print('=' * 30)

# O 'for c in range(0, 10)' vai repetir o bloco 10 vezes
for c in range(0, 10):
    # --- Lógica Corrigida ---
    # 1. Eu mostro o 'Termoatual' (Na primeira volta, mostra o PrimeiroTermo)
    print(Termoatual)

    # 2. Eu atualizo o 'Termoatual' somando a razão,
    #    deixando ele pronto para a PRÓXIMA volta do loop.
    Termoatual = Termoatual + Razao

    time.sleep(0.3)

print('ACABOU!')