"""
Exercício 066: Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
(Versão com 'while True' e 'break')
"""

# Comecei meus acumuladores zerados
Numero = 0
Cont = 0
Soma = 0

# 1. O "Pulo do Gato" da Aula 15: Loop Infinito
while True:
    Numero = int(input('Digite um numero(Digite 999 para parar):  '))

    # 2. A Mágica: Checar a condição de parada ANTES de somar
    #    Se o número for 999...
    if Numero == 999:
        break  # ...eu "quebro" o loop infinito e pulo fora.

    # 3. Se não for 999, o 'break' não roda.
    #    Aí sim eu acumulo a soma...
    Soma = Soma + Numero
    #    ...e conto +1.
    Cont += 1

# 4. O 'print' final, fora do loop
print('=' * 30)
print(f'A soma dos {Cont} Numeros é: {Soma}')
print('=' * 30)