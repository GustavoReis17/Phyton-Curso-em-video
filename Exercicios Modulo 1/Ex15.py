"""
Exercício 015: Escreva um programa que pergunte a quantidade de Km
percorridos por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro
custa R$60 por dia e R$0,15 por Km rodado.
"""

# Pedi a quantidade de dias (usei int, dias são inteiros)
Dias = int (input('Digite a quantidade de dias alugados: '))
# Pedi a quantidade de Km (usei float, pode ter km quebrado)
Km = float(input('Digite a quantidade de Km rodados: '))

# --- O Pulo do Gato ---
# Eu fiz o cálculo todo direto dentro do .format() do print.
# 1. (Dias * 60) -> Calculei o total dos dias
# 2. (Km * 0.15) -> Calculei o total dos Km
# 3. (...) + (...) -> Somei os dois
# Também usei o {:.2f} para formatar o Km e o R$
print('O preço a pagar pela quantidade de {} dias alugados \ne a quantidade de KM {:.2f} Rodados\n o valor total a pagar é R${:.2f}'.format(Dias,Km,(Dias * 60)+(Km * 0.15)))