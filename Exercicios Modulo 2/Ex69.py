"""
Exercício 069: Crie um programa que leia a idade e o sexo
de várias pessoas. A cada pessoa cadastrada, o programa
deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
"""

from datetime import date  # (Esse import não foi usado, mas tudo bem)

# 1. Zerei todos os meus contadores
Homens = 0
Mulher = 0
Maior = 0

# 2. Loop "Mestre" (infinito)
while True:
    print('=' * 30)
    print('CADASTRE UMA PESSOA')
    print('=' * 30)

    # Pedi os dados
    Nome = str(input('Nome: '))
    Idade = int(input('Idade: '))
    # Peguei o sexo e já tratei (strip, upper, [0])
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    # --- Faço as checagens e atualizo os contadores ---

    # A) Quantos são maiores de 18
    if Idade > 18:
        Maior += 1

    # B) Quantos são homens
    if sexo == 'M':
        Homens += 1

    # C) Quantas mulheres são menores de 20
    if sexo == 'F' and Idade < 20:
        Mulher += 1

    # --- "Mini-loop" de validação do [S/N] ---
    while True:
        Opcao = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

        # Se for 'S' ou 'N', a resposta é válida
        if Opcao == 'N' or Opcao == 'S':
            break  # Quebra o "mini-loop"
        else:
            # Se for inválido, eu só aviso e o mini-loop repete
            print('Você digitou uma opção invalida. Tente novamente.')

    # --- Checagem de parada do Loop "Mestre" ---
    # (O 'break' do mini-loop joga o código aqui)
    if Opcao == 'N':
        break  # Quebra o "loop mestre"

# --- Fim do Jogo - Mostro os resultados ---
print('=' * 30)
print(f'Foi cadastrado um total de {Maior} pessoas com mais de 18 anos.')
print('=' * 30)
print(f'Foi cadastrado {Homens} Homens.')
print('=' * 30)
print(f'Foi cadastrado {Mulher} mulheres com menos de 20 anos.')