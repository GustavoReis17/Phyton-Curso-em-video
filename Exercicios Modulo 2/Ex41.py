"""
Exercício 041: A Confederação Nacional de Natação precisa de
um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JUNIOR
– Até 25 anos: SÊNIOR (Eu usei 20, mas a lógica vale!)
– Acima: MASTER
"""

# 1. O Pulo do Gato!
# Importei a ferramenta 'date' para pegar o ano atual
from datetime import date

# Pedi o ano de nascimento
Ano = int(input('Digite o ano do seu nascimento: '))

# Calculei a idade usando o ano ATUAL (date.today().year)
# Agora o programa funciona em 2025, 2026, 2030...
Idade = date.today().year - Ano

# --- Lógica da Classificação (if-elif-else) ---
# Aqui eu monto uma "escada" de checagens.

# 1. Filtro 1: Menor ou igual a 9 anos
if Idade <= 9:
    print(f'Com {Idade} anos você está na categoria MIRIM')

# 2. Filtro 2: Se não for Mirim, checo se é Infantil
# (Aqui eu chequei se é > 9 E <= 14)
# (Dica: O 'Idade > 9' nem precisava, pq o 'if' de cima já pegou quem é <= 9)
elif Idade > 9 and Idade <= 14:
    print(f'Com {Idade} anos você está na categoria INFANTIL')

# 3. Filtro 3: Se não for Mirim NEM