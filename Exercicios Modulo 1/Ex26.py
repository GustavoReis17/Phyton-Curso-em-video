# Pedi a frase. O str() é opcional, mas tudo bem.
Frase = str (input('Digite uma frase: '))

# --- Preparação da Frase ---
# 1. Usei .upper() para transformar tudo em maiúscula.
#    Assim eu não preciso procurar por 'a' e 'A' separado.
# 2. Usei .strip() para tirar espaços inúteis do começo e do fim.
LetraA = Frase.upper().strip()

# .count('A') conta quantas vezes 'A' aparece na string tratada.
print(f'A letra A aparece {LetraA.count('A')} vezes na frase.')

# .find('A') acha a posição (índice) da PRIMEIRA letra 'A'
print(f'A letra A aparece primeiro na posição: {LetraA.find('A')}')

# .rfind('A') ('r' de right/direita) acha a posição da ÚLTIMA letra 'A'
print(f'A letra A aparece por ultimo na posição: {LetraA.rfind('A')}')