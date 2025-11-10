"""
Exercício 044: Elabore um programa que calcule o valor a ser pago
por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço normal
– 3x ou mais no cartão: 20% de juros
"""

# Pedi o preço do produto (float para os centavos)
Produto = float(input('Digite o valor do Produto: R$'))

# Mostrei o menu (usei aspas triplas para pular várias linhas)
print('''Ecolha abaixo as opções de pagamento
[ 1 ] Á Vista Dinheiro/Cheque
[ 2 ] Á Vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais
      ''')

# Pedi a opção ao usuário
opcao = int(input('Digite a opção desejada: '))

# --- Lógica do Menu (if-elif-else) ---
# Agora eu checo qual 'opcao' o usuário escolheu

# 1. Opção 1: 10% de desconto
if opcao == 1:
    # Calculei o desconto (Produto * 0.10) e subtraí do total
    print(f'O valor a pagar é: R${Produto - (Produto * 0.10):.2f}')

# 2. Opção 2: 5% de desconto
elif opcao == 2:
    # Calculei 5% de desconto (Produto * 0.05) e subtraí
    print(f'O valor a pagar é: R${Produto - (Produto * 0.05):.2f}')

# 3. Opção 3: Preço normal (sem desconto)
elif