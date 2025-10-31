"""
Exercício 036: Escreva um programa para aprovar o empréstimo bancário
para a compra de uma casa. O programa vai perguntar o valor da casa,
o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode
exceder 30% do salário, ou então o empréstimo será negado.
"""

# Pedi os 3 valores principais. Usei float() para dinheiro e int() para anos.
ValorC = float(input('Valor da casa em R$ '))
Salario = float(input('Qual valor do seu salario em R$'))
Anos = int(input('Quantas anos você deseja pagar? '))

# Calculei a prestação mensal (valor total / total de meses)
Parcela = ValorC / (Anos * 12)
# Calculei o limite (30% do salário) separado, para o if ficar mais limpo
Limite = Salario * 0.30

# --- A Lógica da Aprovação ---
# A regra é clara: se a Parcela for MAIOR (>) que o Limite, tá negado.
if Parcela > Limite:
    print('-' * 20)
    print('O emprestimo foi negado')
    print('-' * 20)
    # Adicionei essa mensagem extra para o usuário
    print('Infelizmente você não pode financiar essa casa !!')
else :
    # Se a parcela for menor OU IGUAL ao limite, tá aprovado.
    print('-' * 20)
    print('O emprestimo foi aprovado')
    print('-' * 20)
    # E aqui eu mostro os detalhes do financiamento
    print(f'O valor da casa é R${ValorC:.2f}')
    print(f'Você vai pagar prestações de: R${Parcela:.2f} Em {Anos} anos.')