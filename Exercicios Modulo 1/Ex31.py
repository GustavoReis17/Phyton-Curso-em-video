"""
Exercício 031: Desenvolva um programa que pergunte a distância de uma viagem
em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens
de até 200Km e R$0,45 para viagens mais longas.
"""

# Pedi a distância em float, caso a viagem tenha Km "quebrados"
Km = float (input('Digite a distancia da sua viagem em Km: '))

# A lógica principal: checar se a viagem é curta ou longa
if Km <= 200:
    # Viagem curta (até 200Km), o preço é 50 centavos por Km
    # (Usei :.0f para arredondar o valor, ex: R$75)
    print(f'O preço da sua pasagem será R${Km * 0.50:.0f} ')
else:
    # Viagem longa (mais de 200Km), o preço é 45 centavos por Km
    # (Usei :.2f para formatar como dinheiro, ex: R$90.45)
    print(f'O preço da sua viagem será R${Km * 0.45:.2f} ')