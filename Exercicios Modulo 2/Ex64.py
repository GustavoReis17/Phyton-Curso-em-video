"""
Exercício 064: Crie um programa que leia vários números
inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual
foi a soma entre eles (desconsiderando o flag).
"""

# Comecei meus acumuladores zerados
Numero = 0
cont = 0
Soma = 0

# A condição de parada é o 999
while Numero != 999:
    # Pedi o número DENTRO do loop
    Numero = int(input('Digite um Numero (999 para parar): '))

    # --- O Pulo do Gato ---
    # Eu SÓ vou somar e contar se o número NÃO FOR 999
    if Numero != 999:
        #    Eu acumulo o 'Numero' na 'Soma'
        Soma = Soma + Numero  # (Ou Soma += Numero)

        #    Eu só conto +1 se não for 999
        cont += 1

# No final, eu mostro a 'Soma' e o 'cont'
print(f'A soma dos numeros é {Soma} e a quantidade de numeros digitados foi {cont}')