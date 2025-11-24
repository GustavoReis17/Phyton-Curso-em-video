"""
Exercício 067: Faça um programa que mostre a tabuada de vários
números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número
solicitado for negativo.
"""

import time
Numero = 0

# 1. Criei o loop "mestre" (infinito)
while True:
    # Pedi o número DENTRO do loop
    Numero = int(input('Digite um numero para a tabuada(Digite um negativo para sair):   '))

    # 2. A condição de parada (o 'break')
    #    Se o número for negativo, eu "quebro" o 'while True'
    if Numero < 0:
        break

    print('-' * 20)  # Botei um separador

    # --- O Pulo do Gato ---
    # 3. O loop "escravo" (o da tabuada)
    #    Eu uso um 'for' aqui dentro. É o jeito mais limpo,
    #    porque o 'range(1, 11)' já faz a contagem de 1 a 10
    #    automaticamente toda vez que o 'while' roda.
    for i in range(1, 11):
        Mult = Numero * i
        print(f'{Numero} x {i} = {Mult}')
        time.sleep(0.2)
    print('-' * 20)  # Botei outro separador

# 4. Quando o 'break' roda, ele pula aqui pra fora
print('Programa finalizado com sucesso!')