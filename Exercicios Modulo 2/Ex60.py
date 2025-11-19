"""
Exercício 060: Faça um programa que leia um número
qualquer e mostre o seu fatorial.
(Ex: 5! = 5x4x3x2x1 = 120)
(Modo 'while')
"""

Numero = int(input('Digite um numero: '))

# 1. O Pulo do Gato:
#    O acumulador de multiplicação (Fatorial) TEM que começar em 1.
Fatorial = 1
# O contador regressivo
cont = Numero

print(f'Calculando o fatorial de {Numero} ! = ', end='')

# O loop vai rodar 5, 4, 3, 2, 1...
while cont != 0:  # (ou cont > 0)

    # 2. A Lógica da Impressão (que você fez perfeito)
    #    Eu imprimo o 'cont' ANTES de diminuir ele.
    print(f'{cont}', end='')
    if cont > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')  # (Quando chegar no 1, bota o '=')

    # 3. A Lógica do Cálculo
    #    Eu multiplico o Fatorial atual pelo contador
    Fatorial *= cont

    # 4. Diminuo o contador para a próxima volta
    cont = cont - 1

# 5. Imprimo o resultado final (só quando o 'while' acaba)
print(Fatorial)