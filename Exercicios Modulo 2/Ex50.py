"""
Exercício 050: Desenvolva um programa que leia seis números
inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

# Comecei o meu acumulador 'Soma' com 0
Soma = 0

# O 'range(0, 6)' vai fazer o loop rodar 6 vezes (0, 1, 2, 3, 4, 5)
for n in range(0, 6):
    # Pedi o número dentro do loop
    # (Usei f-string pra ficar mais claro qual número é)
    Numero = int(input(f'Digite o {n + 1}º numero: '))

    # --- A Lógica da Soma ---
    # Eu checo se o 'Numero' (que o usuário digitou) é par.
    if Numero % 2 == 0:
        # Se for par, eu adiciono ele na 'Soma'
        # (Se for ímpar, o 'if' falha e o programa só ignora o número)
        Soma += Numero

# No final do loop, eu mostro a soma total dos pares
print(f'A soma dos numeros pares que você digitou é: {Soma}')