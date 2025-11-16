"""
Exercício 054: Crie um programa que leia o ano de nascimento
de sete pessoas. No final, mostre quantas pessoas ainda não
atingiram a maioridade e quantas já são maiores.
"""

# Importei a ferramenta 'date' para pegar o ano atual
from datetime import date

# 1. Comecei meus "contadores" zerados
Maior = 0
Menor = 0

# 2. Criei o loop para rodar 7 vezes (de 0 a 6)
for i in range(0, 7):
    # Pedi o ano de nascimento
    Nascimento = int(input(f'Digite o ano de nascimento da {i + 1}ª pessoa: '))

    # 3. Calculei a idade usando o ano ATUAL (date.today().year)
    Idade = date.today().year - Nascimento

    # --- A Lógica do Exercício ---
    # Na aula ele pediu para considerar a MAIORIDADE com 21 ANOS.
    # Por isso, eu checo se a idade é MENOR que 21.
    if Idade < 21:
        # Se for, somo 1 no contador de Menores
        Menor = Menor + 1
    else:
        # Se for 21 ou mais, somo 1 no contador de Maiores
        Maior = Maior + 1

# 5. No final do loop, mostro os totais
print('=' * 30)
print(f'Considerando 21 anos como maioridade:')
print(f'São {Maior} maiores de idade e {Menor} menores de idade')
print('=' * 30)