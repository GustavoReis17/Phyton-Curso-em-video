"""
Exercício 033: Faça um programa que leia três números
e mostre qual é o maior e qual é o menor.
"""

# Pede os 3 números
Num1 = int(input('Digite o primeiro numero: '))
Num2 = int(input('Digite o segundo numero: '))
Num3 = int(input('Digite o terceiro numero: '))

# 1. Testa se o Num1 é o maior
if (Num1 > Num2 and Num1 > Num3):
    print(f'O numero {Num1} é o maior')

    # Se Num1 é o maior, o menor só pode ser o Num2 ou o Num3
    if Num2 > Num3:
        print(f'O numero {Num3} é o menor')
    else:
        print(f'O numero {Num2} é o menor')

# 2. Se Num1 não for o maior, testa se o Num2 é
# (Note que aqui você nem precisa testar contra o Num1,
#  porque o if anterior já falhou, então o Num1 NÃO é o maior)
elif Num2 > Num3:
    print(f'O numero {Num2} é o maior')

    # Se Num2 é o maior, o menor é o Num1 ou o Num3
    if Num1 > Num3:
        print(f'O numero {Num3} é o menor')
    else:
        print(f'O numero {Num1} é o menor')

# 3. Se nem Num1 nem Num2 forem os maiores, o Num3 é o maior
else:
    print(f'O numero {Num3} é o maior')

    # Se Num3 é o maior, o menor é o Num1 ou o Num2
    if Num1 > Num2:
        print(f'O numero {Num2} é o menor')
    else:
        print(f'O numero {Num1} é o menor')