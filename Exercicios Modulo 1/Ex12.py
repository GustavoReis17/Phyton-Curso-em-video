"""
Exercício 012: Faça um algoritmo que leia o preço de um produto
e mostre seu novo preço, com 5% de desconto.
"""

# Pedi o preço do produto, usando float() para aceitar centavos
Produto = float (input('Digite o preço do seu produto: R$: '))

# --- O Cálculo do Desconto ---
# Eu fiz o cálculo todo direto dentro do .format() do print.
# 1. (Produto * 0.05) -> Calculei quanto é 5% (o valor do desconto)
# 2. Produto - (...)  -> Subtraí esse valor do preço original
# 3. :.2f             -> Corrigi aqui para formatar como dinheiro (ex: R$ 9.50)
print('O preço do seu produto com 5% de desconto sai a R${:.2f}'.format(Produto - (Produto * 0.05)))