"""
Exercício 045: Crie um programa que faça o computador
jogar Jokenpô (Pedra, Papel, Tesoura) com você.
(Versão 1: Usando Strings)
"""

# Preciso do 'random' para o computador "escolher"
import random

# Mostrei o menu de texto
print('''Digite a opcao que deseja jogar:
 Pedra
 Papel
 Tesoura
      ''')

# Pedi a minha escolha
Escolha = str(input('Escolha: '))

# --- O Pulo do Gato (Limpeza do Input) ---
# Deixei a minha escolha limpa (sem espaços) e em MAIÚSCULA,
# para facilitar as comparações lá embaixo
Transformado = Escolha.strip().upper()

# O computador sorteia a dele.
# Usei random.choice() pra sortear uma das 3 strings.
Sorteio = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])

# --- A Lógica (Ifs Aninhados) ---
# O 'if' de fora checa o que EU joguei.
# O 'if' de dentro compara com o que o PC jogou.

# 1. O que acontece se EU joguei PEDRA:
if Transformado == 'PEDRA':
    if Sorteio == 'PEDRA':
        print('Empatou')
    elif Sorteio == 'TESOURA':
        print('Você ganhou') # (Pedra quebra Tesoura)
    else: # (Se não é Pedra nem Tesoura, o PC jogou Papel)
        print('Você Perdeu')