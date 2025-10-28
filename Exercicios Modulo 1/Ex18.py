"""
Exercício 018: Faça um programa que leia um ângulo qualquer e mostre
na tela o valor do seno, cosseno e tangente desse ângulo.
"""

# Para as funções de trigonometria (sen, cos, tan) e para a conversão,
# eu precisei importar a biblioteca 'math'.
import math

# Pedi o ângulo em graus. Usei float() para aceitar ângulos "quebrados" (ex: 45.5)
Angulo = float(input('Digite um Angulo real em graus: '))

# --- O Pulo do Gato: Converter para Radianos ---
# As funções do 'math' (sin, cos, tan) não entendem graus!
# Elas só trabalham com radianos.
# Então, eu usei math.radians() para converter o ângulo primeiro.
Angulo_em_radianos = math.radians(Angulo)

# Agora sim, com o ângulo em radianos, eu calculo o Seno...
Seno = math.sin(Angulo_em_radianos)
# o Cosseno...
Cosseno = math.cos(Angulo_em_radianos)
# e a Tangente.
Tangente = math.tan(Angulo_em_radianos)

# Imprimi os 3 resultados, formatando com 2 casas decimais (:.2f)
print('De acordo com o Angulo {:.2f} \nO Seno é {:.2f} \nO Cosseno é {:.2f} \nA Tange