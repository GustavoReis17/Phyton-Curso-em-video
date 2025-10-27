"""
Exercício 011: Faça um programa que leia a largura e a altura de uma
parede em metros, calcule a sua área e a quantidade de tinta necessária
para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².
"""

# Pedi a largura e a altura, usando float() para aceitar medidas tipo 2.5m
Largura = float(input('Digite a largura em metros: '))
Altura = float(input('Digite a altura em metros: '))

# 1. Calculei a área (Largura x Altura) e guardei na variável 'Area'
Area = Largura * Altura

# 2. No print, eu já mostrei a área e fiz o cálculo da tinta
#    Se 1 litro pinta 2m², eu só precisei dividir a Area total por 2.
print('O calculo da area é {} Metros quadrados.\n'
      'A quantidade de tinta necessaria para pintar é {} Litros'.format(Area,Area / 2 ))