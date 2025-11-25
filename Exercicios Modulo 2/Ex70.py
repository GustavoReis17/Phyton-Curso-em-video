"""
Exercício 070: Crie um programa que leia o nome e o preço
de vários produtos. O programa deverá perguntar se o
usuário vai continuar. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
"""

# 1. Zerei meus contadores e acumuladores
Cont = 0  # (Contador de produtos > 1000)
Total = 0  # (Acumulador do total R$)

# 2. Varáveis para o mais barato
Valor_barato = 0  # (Usei 0 como "flag" da primeira volta)
Nome_barato = ''  # (Nome do mais barato)

# 3. Loop "Mestre" (infinito)
while True:
    print('=' * 30)
    print('Cadastre um Produto..')
    print('=' * 30)
    # (Usei .title() pra deixar o nome bonito, ex: 'Tv Samsung')
    Nome = str(input('Nome do produto: ')).strip().title()
    print('-' * 20)
    Valor = float(input('Valor do produto: '))
    print('-' * 20)

    # A) Chequei se o produto custa mais de 1000
    if Valor > 1000:
        Cont += 1

    # A) Somei o valor ao total, independente do preço
    Total += Valor

    # C) Lógica do mais barato
    # (Meu "pulo do gato": se Valor_barato == 0, é a primeira volta)
    if Valor_barato == 0:
        Valor_barato = Valor
        Nome_barato = Nome
    # (Da segunda volta em diante, eu checo se o novo valor é menor)
    elif Valor_barato > Valor:
        Valor_barato = Valor
        Nome_barato = Nome

    # 4. "Mini-loop" de validação do [S/N] (aprendi no Ex 065)
    while True:
        Opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if Opcao == 'N' or Opcao == 'S':
            break
        else:
            print('Você digitou uma opção invalida. Tente novamente.')

    # 5. Se o usuário digitou 'N', quebra o loop mestre
    if Opcao == 'N':
        break

# --- Fim do Loop Mestre ---
print('=' * 30)
print(f'O total gasto foi de R${Total:.2f} reais')
print('=' * 30)
print(f'São {Cont} produtos que custam mais de R$ 1000 reais.')
print('=' * 30)
print(f'O produto mais barato foi {Nome_barato} que custa R${Valor_barato:.2f} reais.')