"""
Exercício 040: Crie um programa que leia duas notas de um aluno
e calcule sua média, mostrando uma situação no final,
de acordo com a média atingida:
– Média abaixo de 5.0: REPROVADO
– Média entre 5.0 e 6.9: RECUPERAÇÃO
– Média 7.0 ou superior: APROVADO
"""

# Pedi as duas notas, usando float()
Nota1 = float(input('Digite a sua primeira nota: '))
Nota2 = float(input('Digite a sua segunda nota: '))

# Calculei a média (soma / 2) antes de tudo, pra deixar o if mais limpo.
Media = (Nota1 + Nota2) / 2

# --- A Lógica dos 3 Níveis (if-elif-else) ---

# 1. Primeiro, eu checo se o aluno foi APROVADO (>= 7)
if Media >= 7:
    print(f'Com uma média de {Media} você está:')
    print('-' * 20)
    print('Aprovado')
    print('-' * 20)

# 2. Esse 'elif' é o pulo do gato dessa aula.
#    Eu uso 'and' para checar se a média está DENTRO do intervalo
#    de recuperação (maior ou igual a 5 E menor que 7).
elif Media >= 5 and Media < 7:
    print(f'Com uma média de {Media} você está:')
    print('-' * 20)
    print('Em Recuperação') # Corrigido!
    print('-' * 20)

# 3. Se não foi Aprovado (if) NEM Recuperação (elif),
#    é porque a média é menor que 5.
elif Media < 5:
    print(f'Com uma média de {Media} você está:')
    print('-' * 20)
    print('Reprovado')
    print('-' * 20)