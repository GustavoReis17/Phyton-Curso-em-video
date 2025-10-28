"""
Exercício 017: Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo,
calcule e mostre o comprimento da hipotenusa.
"""

# Importei a 'math' para me ajudar nos cálculos
import math

# Pedi os dois catetos, usando float() para aceitar medidas com vírgula
CatetoO = float(input('Digite um Cateto Oposto: '))
CatetoA = float(input('Digite um Cateto Adjacente: '))

# --- O Pulo do Gato ---
# Eu poderia fazer o Teorema de Pitágoras na mão ( (co**2 + ca**2) ** 0.5 ),
# mas a biblioteca 'math' já tem a função 'hypot()' que faz
# exatamente isso de forma mais rápida e precisa.
Hipotenusa = math.hypot(CatetoO, CatetoA)

# Imprimi o resultado formatado com 2 casas (:.2f)
print('Se o Cateto Oposto é {:.2f} e o Cateto Adjacente é {:.2f} \nEntão a Hipotenusa é {:.2f}'.format(CatetoO,CatetoA,Hipotenusa))