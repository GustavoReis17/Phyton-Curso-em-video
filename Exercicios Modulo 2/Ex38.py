"""
Exercício 038: Escreva um programa que leia dois números
inteiros e compare-os, mostrando na tela uma mensagem:
– O primeiro valor é maior
– O segundo valor é maior
– Não existe valor maior, os dois são iguais
"""

# Pedi os dois números inteiros
Numero1 = int(input('Digite o primeiro Numero inteiro: '))
Numero2 = int(input('Digite o segundo Numero inteiro: '))

# --- Lógica da Comparação ---
# Eu usei a estrutura 'if-elif-else' porque
# só existem 3 possibilidades (maior, menor ou igual).

# 1. Chequei se o primeiro é maior
if Numero1 > Numero2:
    print (f'O Primeiro Numero {Numero1} é maior que o segundo Numero {Numero2}')

# 2. Se não for, chequei se o primeiro é menor (ou seja, o segundo é maior)
elif Numero1 < Numero2:
    print(f'O Segundo Numero {Numero2} é maior que o primeiro Numero {Numero1}')

# 3. Se ele não é maior E não é menor, ele SÓ PODE ser igual.
else:
    print(f'O Primeiro Numero {Numero1} e o segundo Numero {Numero2} são iguais.')