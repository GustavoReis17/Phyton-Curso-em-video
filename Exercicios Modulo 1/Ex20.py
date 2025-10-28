"""
Exercício 020: O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos. Faça um programa
que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

# Precisei da biblioteca 'random'
import random

# Pedi o nome dos 4 alunos, um em cada variável
Nome1 = str(input('Digite o nome do primeiro aluno: '))
Nome2 = str(input('Digite o nome do segundo aluno: '))
Nome3 = str(input('Digite o nome do terceiro aluno: '))
Nome4 = str(input('Digite o nome do quarto aluno: '))

# Para conseguir embaralhar, primeiro eu juntei os 4 nomes em uma lista
lista = [Nome1, Nome2, Nome3, Nome4]

# --- O Pulo do Gato ---
# A função 'random.shuffle()' é a ferramenta certa pra isso.
# Ela não escolhe um, ela EMBARALHA a ordem dos itens
# dentro da própria lista. A 'lista' original é modificada.
random.shuffle(lista)

# Agora é só imprimir a lista inteira, que já está na nova ordem.
# (Corrigi a digitação de "apresentação" aqui)
print(f'A ordem de apresentação será: {lista}')