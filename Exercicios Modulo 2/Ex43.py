"""
Exercício 043: Desenvolva uma lógica que leia o peso e a altura
de uma pessoa, calcule seu IMC e mostre seu status,
de acordo com a tabela:
– Abaixo de 18.5: Abaixo do Peso
– Entre 18.5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
"""

# Pedi o peso e a altura, usando float()
Peso = float(input('Digite o seu peso: '))
Altura = float(input('Digite sua altura: '))

# 1. Calculei o IMC (Peso dividido pela Altura ao quadrado)
IMC = Peso / (Altura * Altura)

# --- Lógica de Classificação ---
# Eu uso o if-elif-else para criar as "faixas" de peso.

# 1. Faixa 1 (Abaixo do Peso)
if IMC < 18.5:
    print('=' * 30)
    # (Usei o :.2f para formatar o IMC)
    print(f'Seu IMC é {IMC:.2f}')
    print('=' * 30)
    print('Você está Abaixo do Peso')

# 2. Faixa 2 (Peso Ideal)
elif IMC >= 18.5 and IMC < 25:
    print('=' * 30)
    print(f'Seu IMC é {IMC:.2f}')
    print('=' * 30)
    # (Corrigi aqui, eu tinha digitado "mo" em vez de "no")
    print('Você está no Peso Ideal')

# 3. Faixa 3 (Sobrepeso)
elif IMC >= 25 and IMC < 30:
    print('=' * 30)
    print(f'Seu IMC é {IMC:.2f}')
    print('=' * 30)
    print('Você está com Sobrepeso')

# 4. Faixa 4 (Obesidade)
elif IMC >= 30 and IMC < 40:
    print('=' * 30)
    print(f'Seu IMC é {IMC:.2f}')
    print('=' * 30)
    print('Você está com Obesidade')

# 5.