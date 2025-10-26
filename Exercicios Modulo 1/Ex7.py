"""
Exercício 007: Desenvolva um programa que leia as duas notas
de um aluno, calcule e mostre a sua média.
"""

# Pedi as duas notas do aluno.
# (Usei int() aqui. Se a nota pudesse ser 7.5, eu usaria float())
Nota1 = int (input('Digite sua Primeira nota: '))
Nota2 = int (input('Digite sua Segunda nota: '))

# --- O Cálculo da Média ---
# Eu fiz o cálculo todo direto dentro do .format()
# 1. (Nota1 + Nota2) -> Somei as duas notas. Os parênteses são
#                      essenciais para somar *antes* de dividir.
# 2. (...) / 2        -> Dividi o total por 2.
print('A media da suas Notas é: {}'.format((Nota1 + Nota2)/2))