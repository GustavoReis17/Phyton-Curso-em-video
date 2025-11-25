"""
Exercício 071: Crie um programa que simule o funcionamento
de um caixa eletrônico. No início, pergunte ao usuário qual
será o valor a ser sacado (número inteiro) e o programa
vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
"""
# 1. Zerei os contadores de cada nota
Ced50 = 0
Ced20 = 0
Ced10 = 0
Ced1 = 0

print('=' * 30)
print('     CAIXA ELETRÔNICO     ')
print('=' * 30)
Valor = int(input('Digite o valor a ser sacado em R$: '))

# --- A Lógica da Contagem (Subtração Contínua) ---
# O programa é uma SEQUÊNCIA. Primeiro ele gasta as notas de 50,
# DEPOIS gasta as de 20 com o que sobrou.

# 2. Loop das notas de R$ 50
#    (Ele vai rodar 'na mão' até o 'Valor' ser menor que 50)
while Valor >= 50:
    Valor -= 50
    Ced50 += 1

# 3. Loop das notas de R$ 20 (com o que SOBROU)
while Valor >= 20:
    Valor -= 20
    Ced20 += 1

# 4. Loop das notas de R$ 10 (com o que SOBROU)
while Valor >= 10:
    Valor -= 10
    Ced10 += 1

# 5. Loop das notas de R$ 1 (com o que SOBROU)
while Valor >= 1:
    Valor -= 1
    Ced1 += 1

# --- Impressão Final (Mais Limpa) ---
# Eu só vou imprimir a linha se o contador for maior que 0.
print('=' * 30)
if Ced50 > 0:
    print(f'Total de {Ced50} cédulas de R$ 50')
if Ced20 > 0:
    print(f'Total de {Ced20} cédulas de R$ 20')
if Ced10 > 0:
    print(f'Total de {Ced10} cédulas de R$ 10')
if Ced1 > 0:
    print(f'Total de {Ced1} cédulas de R$ 1')
print('=' * 30)
print('Volte sempre!')