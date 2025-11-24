"""
Exercício 065: Crie um programa que leia vários números
inteiros pelo teclado. No final da execução, mostre a
média entre todos os valores e qual foi o maior e o
menor valores lidos. O programa deve perguntar ao
usuário se ele quer ou não continuar a digitar valores.
"""

import time

Numero = 0
opcao = 'S'  # Flag para o loop começar
Soma = 0
cont = 0
Media = 0
Maior = 0
Menor = 0

# Loop "Mestre": roda enquanto a opção for 'S'
while opcao == 'S':
    print('=' * 30)
    Numero = int(input('Digite um valor: '))

    # 1. Acumulei a soma
    Soma = Soma + Numero

    # 2. Calibrei o Maior/Menor na primeira volta (quando cont == 0)
    if cont == 0:
        Maior = Numero
        Menor = Numero
    else:
        # 3. Chequei os próximos
        if Numero > Maior:
            Maior = Numero
        elif Numero < Menor:
            Menor = Numero

    # 4. Contei +1
    cont += 1

    # --- O PULO DO GATO (A Validação S/N) ---
    # Eu "prendo" o usuário aqui até ele digitar S ou N
    while True:
        opcao = str(input('Deseja continuar? (S/N)')).strip().upper()[0]

        #  A opção é válida se for 'S' OU 'N'
        if opcao == 'S' or opcao == 'N':
           # Pausa
            break
        else:
            # Avisa que foi digitado errado
            print('Você digitou uma opção invalida. Tente novamente.!')

    # A pausa só roda se a opção for 'N'.
    if opcao == 'N':
        print('Finalizando...')
        print('=' * 30)
        time.sleep(0.4)

# --- FIM DO LOOP MESTRE ---

# Calculo a Média
Media = (Soma / cont)

print(f'Soma: {Soma} -> ', end='')
print(f'Media: {Media:.2f} -> ', end='')
if Maior == Menor:
    print(f'Maior e menor são iguais: {Maior} -> ', end='')
else:
    print(f'Maior: {Maior} -> ', end='')
    print(f'Menor: {Menor} -> ', end='')
print('Fim !!!')