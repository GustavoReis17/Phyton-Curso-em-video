"""
Exercício 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
o nome com todas as letras maiúsculas e minúsculas, quantas letras ao
todo (sem considerar espaços), e quantas letras tem o primeiro nome.
"""

# Pedi o nome completo
Nome = input('Digite seu nome completo: ')

# Usei .upper() para a versão maiúscula
Mausculo = (Nome).upper()
# Usei .lower() para a versão minúscula
Minusculo =  (Nome).lower()

# Para contar as letras sem espaços, primeiro eu
# criei uma nova string trocando ' ' por '' (nada)
SemE = Nome.replace(' ','')

# Para pegar o primeiro nome, eu quebrei a string
# em uma lista (com .split()) e peguei só o primeiro item [0]
PrimNome =  Nome.split(' ')[0]

# --- Saída dos Dados ---
print(f'Nome em Mausculo: {Mausculo}')
print(f'Nome em Minusculo: {Minusculo}')

# Aqui eu uso o len() na string 'SemE', que não tem espaços
print(f'Seu nome ao todo tem {len(SemE)} letras')

# E aqui eu uso o len() na string 'PrimNome'
# (só ajustei seu texto do print pra ficar mais claro)
print(f'Seu primeiro nome tem {len(PrimNome)} letras')