"""
Exercício 063: Escreva um programa que leia um número N
inteiro qualquer e mostre na tela os N primeiros
elementos de uma Sequência de Fibonacci.
Ex: 0 – 1 – 1 – 2 – 3 – 5 – 8
"""

# Pedi quantos termos a pessoa quer ver
Numero = int(input('Digite um numero para a sequencia Fibonacci: '))

# A sequência SEMPRE começa com 0 e 1
Termo1 = 0
Termo2 = 1

print('=' * 30)
# Eu já imprimi os DOIS primeiros termos aqui
print(f'{Termo1} -> {Termo2}', end='')

# Como eu já mostrei 2 termos, o meu contador
# tem que começar a contar a partir do 3º termo.
Cont = 3

# O loop vai rodar "enquanto o contador for menor ou igual ao objetivo"
while Cont <= Numero:
    # 1. Calculei o próximo termo (t3 = t1 + t2)
    Termo3 = Termo1 + Termo2
    # 2. Mostrei o termo novo
    print(f' -> {Termo3}', end='')

    # 3. O PULO DO GATO: "Andei com a fila"
    # O t1 antigo morre
    # O t2 vira o novo t1
    Termo1 = Termo2
    # O t3 vira o novo t2
    Termo2 = Termo3

    # 4. Somei 1 no contador
    Cont = Cont + 1

print(' -> FIM')
print('=' * 30)