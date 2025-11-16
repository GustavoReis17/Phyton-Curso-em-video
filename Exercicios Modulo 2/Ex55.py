"""
Exercício 055: Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

# Comecei minhas variáveis 'Maior' e 'Menor' com 0.
Maior = 0
Menor = 0

# Criei o loop para rodar 5 vezes (0, 1, 2, 3, 4)
for i in range(0, 5):
    # Pedi o peso (em float)
    Peso = float(input(f'Digite o {i + 1}º peso: '))

    # --- O Pulo do Gato (Calibrando as variáveis) ---
    # Esse 'if' só vai ser Verdadeiro na PRIMEIRA volta do loop
    # (quando Maior e Menor ainda são 0).
    # Eu faço isso para que o *primeiro peso digitado*
    # se torne o Maior e o Menor temporário.
    if Menor == 0 and Maior == 0:
        Menor = Peso
        Maior = Peso

    # Da segunda volta em diante, esse 'if' vai ser Falso,
    # e o programa vai pular para as comparações 'elif'.

    # Se o Peso que acabei de ler for maior que o 'Maior' atual...
    elif Peso > Maior:
        Maior = Peso  # ...ele vira o novo 'Maior'

    # Se o Peso que acabei de ler for menor que o 'Menor' atual...
    elif Peso