"""
Exercício 019: Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele, lendo o nome
deles e escrevendo o nome do escolhido.
"""

# Importei a biblioteca 'random' para poder fazer o sorteio
import random

# Pedi o nome dos 4 alunos
Nome1 = str(input('Digite o nome do primeiro aluno: '))
Nome2 = str(input('Digite o nome do segundo aluno: '))
Nome3 = str(input('Digite o nome do terceiro aluno: '))
Nome4 = str(input('Digite o nome do quarto aluno: '))

# --- O Sorteio ---
# 1. Eu criei uma lista temporária com os 4 nomes: [Nome1, Nome2, Nome3, Nome4]
# 2. Usei a função 'random.choice()' para ESCOLHER UM item dessa lista.
NomeRandom = random.choice([Nome1,Nome2,Nome3,Nome4])

# Imprimi o nome que foi escolhido.
# (Aqui eu usei o .format() que você tinha colocado)
print('O aluno escolhido para limpar o quadro foi o: {}'.format(NomeRandom))