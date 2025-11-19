"""
Exercício 059: Crie um programa que leia dois valores
e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

# Importei o 'time' para usar a pausa (sleep)
import time

# Pedi os números ANTES do loop começar
Numero1 = int(input('Digite um numero: '))
Numero2 = int(input('Digite outro numero: '))

# Comecei o 'opcao' com 0 para forçar o 'while' a rodar a 1ª vez
opcao = 0

# O loop principal: só para quando a 'opcao' for 5
while opcao != 5:
    # Mostrei o menu
    print('''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos numeros
    [ 5 ] Sair do programa
    ''')
    # Pedi a opção DENTRO do loop
    opcao = int(input('Digite a opção:'))

    # --- Lógica das Opções ---

    if opcao == 1:
        Somar = Numero1 + Numero2
        print('=' * 50)
        print(f'A soma entre {Numero1} e {Numero2} é: {Somar}.')

    elif opcao == 2:
        Multiplicar = Numero1 * Numero2
        print('=' * 50)
        print(f'A multiplicção entre {Numero1} e {Numero2} é: {Multiplicar}')

    # (CORRIGIDO) A lógica do "Maior" agora tem 3 checagens
    elif opcao == 3:
        print('=' * 50)
        if Numero1 > Numero2:
            print(f'O maior numero digitado foi {Numero1}')
        elif Numero2 > Numero1: # Usei 'elif'
            print(f'O maior numero digitado foi {Numero2}')
        else:  # E o 'else' para o empate
            print('Os dois números são IGUAIS.')

    # Aqui eu "atualizo" as variáveis Numero1 e Numero2
    elif opcao == 4:
        Numero1 = int(input('Digite um novo numero: '))
        Numero2 = int(input('Digite outro novo numero: '))
        print(f'Números atualizados para {Numero1} e {Numero2}.')

    # Se for 5, eu só aviso e o 'while' vai parar
    elif opcao == 5:
        print('Finalizando...')

    # O 'else' para pegar qualquer opção inválida
    else:
        print('=' * 50)
        print('Opção INVÁLIDA. Tente novamente.')

    #  O Pulo do Gato: a pausa só acontece
    # se o usuário NÃO pediu para sair (opcao != 5)
    if opcao != 5:
        print('=' * 50)
        time.sleep(1)  # Pausa para o usuário ler a resposta

# Essa linha só roda quando o 'while' termina
print('Fim do programa.')