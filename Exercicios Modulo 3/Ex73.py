"""
Exercício 073: Crie uma tupla preenchida com os 20 primeiros
colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
A) Apenas os 5 primeiros.
B) Os últimos 4 colocados.
C) Times em ordem alfabética.
D) Em que posição (na tabela) está o time da Chapecoense.
"""

# 1. Criei a Tupla com os 20 times (baseado nos dados de 09/11/2025)
Time = ('Palmeiras', 'Flamengo', 'Cruzeiro', 'Mirassol', 'Bahia', 'Botafogo', 'Fluminense', 'São Paulo', 'Atlético-MG', 'Vasco da Gama', 'Red Bull Bragantino', 'Ceará', 'Corinthians', 'Grêmio', 'Internacional', 'Vitória', 'Santos', 'Juventude', 'Fortaleza', 'Sport')

# A) Para os 5 primeiros, eu usei fatiamento (slice) [0:5]
#    (Pega do índice 0 até o 4)
print('=' * 30)
print(f'Os 5 primeiros colocados{Time[0:5]}.')

# B) Para os 4 últimos, eu usei o fatiamento [16:]
#    (Pega do índice 16 [o 17º time] até o final)
print('=' * 30)
print(f'Os ultimos 4 colocados{Time[16:]}.')

# C) Para a ordem alfabética, eu usei a função sorted(Time).
#    (O 'sorted' cria uma LISTA nova, sem mexer na tupla original)
print('=' * 30)
print(f'Os times em ordem alfabetrica: {sorted(Time)}')

# D) Para achar a posição, eu usei Time.index("Flamengo")
#    e somei +1 (porque o índice começa em 0, mas a posição começa em 1)
print('=' * 30)
# (O exercício original pedia a Chapecoense, mas eu adaptei para o Flamengo!)
print(f'A colocação em que está o Flamengo é: {Time.index("Flamengo") + 1}º Colocado.')
print('=' * 30)