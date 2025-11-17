"""
Exercício 056: Desenvolva um programa que leia o nome,
idade e sexo de 4 pessoas. No final, mostre:
- A média de idade do grupo.
- Qual é o nome do homem mais velho.
- Quantas mulheres têm menos de 20 anos.
"""

# --- Meus Acumuladores e Variáveis ---
# 1. (CORREÇÃO DA MÉDIA) Criei um acumulador para a soma
SomaIdades = 0

# 2. Um CONTADOR para as mulheres
MulheresMenor20 = 0  # (Seu 'Menor' estava certo, só mudei o nome)

# 3. (CORREÇÃO DO NOME) Variáveis para o homem mais velho
IdadeMaisVelho = 0
NomeMaisVelho = ''  # Começo com uma string vazia (ISSO CORRIGE O BUG 2)

# O loop vai rodar 4 VEZES (usei 1 a 5, que dá 1, 2, 3, 4)
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    Nome = str(input('Digite seu nome: ')).strip()
    Idade = int(input('Digite sua idade: '))
    Sexo = str(input('Digite seu sexo (M/F): ')).strip().upper()

    # --- Lógica da Média ---
    # Eu SÓ somo a idade na média se a pessoa for válida ('M' ou 'F')
    if Sexo == 'M' or Sexo == 'F':
        SomaIdades += Idade

    # --- Lógica do Homem Mais Velho ---
    if Sexo == 'M':
        # Se for o primeiro homem OU se a idade dele for maior que a do "campeão"
        if Idade > IdadeMaisVelho:
            IdadeMaisVelho = Idade
            NomeMaisVelho = Nome

    # --- Lógica das Mulheres ---
    elif Sexo == 'F':
        if Idade < 20:
            MulheresMenor20 += 1

    # --- Tratando a Opção Inválida ---
    else:
        print('Opção de sexo INVÁLIDA. Essa pessoa não será contada.')

# --- Cálculos Finais (Fora do Loop) ---
Media = SomaIdades / 4  # (Média das 4 pessoas)

print('-' * 50)
print(f'A média de idade do grupo é {Media} anos.')
print('-' * 50)

# Checo se algum homem foi digitado
if NomeMaisVelho == '':
    print('Não foi digitado nenhum homem no grupo.')
else:
    print(f'O homem mais velhor é {NomeMaisVelho.title()} com {IdadeMaisVelho} anos.')

print('-' * 50)
print(f'A quantidade mulheres com menos de 20 anos foram: {MulheresMenor20}')
print('-' * 50)