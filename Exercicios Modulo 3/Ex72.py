"""
Exercício 072: Crie um programa que tenha uma Tupla
totalmente preenchida com uma contagem por extenso,
de zero até vinte. Seu programa deverá ler um número
pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""

# 1. O Pulo do Gato (Módulo 3)!
# Criei a TUPLA (com parênteses) com os 21 nomes.
# Ela funciona como uma "tabela" de consulta. A Posição 0 é 'zero', 1 é 'um', etc.
Numero = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
          'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# 2. A Lógica da Validação (Revisão da Aula 15)
while True:
    # Pedi o número
    Num = int(input('Digite um numero entre 0 e 20: '))

    # 3. O Filtro: Chequei se o número está FORA do intervalo (0 a 20)
    if Num < 0 or Num > 20:
        print('Você digitou um numero errado! Tente novamente.')
        # (Se der erro, o loop repete a pergunta, pois não dei 'break')
    else:
        # 4. Se o número for válido (0 a 20)...
        print('=' * 30)
        # ...eu uso o 'Num' como ÍNDICE para buscar a palavra na Tupla 'Numero'
        print(f'Você digitou o numero {Numero[Num]}.')
        print('=' * 30)
        # 5. E dou o 'break' para sair do 'while True'
        break