"""
Exercício 039: Faça um programa que leia o ano de nascimento
de um jovem e informe, de acordo com sua idade:
– Se ele ainda vai se alistar ao serviço militar.
– Se é a hora exata de se alistar.
– Se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

# 1. O Pulo do Gato!
# Importei a ferramenta 'date' para pegar o ano atual
from datetime import date

# Pedi o ano de nascimento
Ano = int(input('Digite o ano que você nasceu: '))

# 2. Calculei a idade da pessoa, usando o ano ATUAL (date.today().year)
#    (Assim o programa não fica "preso" em 2025)
Idade = date.today().year - Ano

# --- Lógica dos 3 Cenários (Antes, Durante, Depois) ---

# 1. Se a idade for MENOR que 18 (ainda vai se alistar)
if Idade < 18:
    print(f'Atualmente a sua idade é {Idade} ainda vai se alistar')
    # Calculei o tempo que falta (18 - Idade)
    print(f'Falta {18 - Idade} anos para você se alistar')

# 2. Se a idade for EXATAMENTE 18 (hora de alistar)
elif Idade == 18:
    print('Você está exatamente na idade de se alistar, procure o alistamento mais proximo')

# 3. Se não for menor nem igual, é porque já passou (MAIOR que 18)
else:
    print(f'A sua idade atualmente é {Idade}')
    # Calculei o tempo que já passou (Idade - 18)
    print(f'Você devia ter se alistado a {Idade - 18} anos atrás')