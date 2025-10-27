"""
Exercício 010: Crie um programa que leia quanto dinheiro uma pessoa
tem na carteira e mostre quantos dólares ela pode comprar.
(Considere US$1,00 = R$3,27)
"""

# Pedi o valor em Reais, usando float() para aceitar os centavos
Reais = float(input('Digite o valor de Reais:'))

# --- A Conversão ---
# A lógica é simples: dividir o total em Reais pelo valor do dólar (3.27)
# Eu já fiz o cálculo direto dentro do .format()
# Também usei o :.2f para formatar tanto os Reais quanto os Dólares
print('Com R${:.2f} você pode comprar US${:.2f}'.format(Reais, Reais / 3.27))