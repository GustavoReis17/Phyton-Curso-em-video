# Exercício 027
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

# Solicita que o usuário digite o nome completo.
# O método strip() remove espaços extras no início e no final.
# O método title() coloca a primeira letra de cada nome em maiúscula.
# O método split() separa o nome em uma lista, dividindo pelas palavras.
nome = input('Digite seu nome completo: ').strip().title().split()

# Exibe o primeiro nome (índice 0 da lista)
print(f'Primeiro nome: {nome[0]}')

# Exibe o último nome (índice -1 da lista, ou seja, o último elemento)
print(f'Último nome: {nome[-1]}')
