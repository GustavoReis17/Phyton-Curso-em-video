"""
Exercício 042: Refaça o DESAFIO 035 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais
– ESCALENO: todos os lados diferentes
"""

# Pedi os três lados
r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

# 1. Checagem principal: Pode formar um triângulo?
#    (Um lado NUNCA pode ser maior que a soma dos outros dois)
if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print('=' * 50)
    print('Os segmentos PODEM FORMAR um triângulo!')
    print('=' * 50)

    # 2. Se sim, qual tipo? (if aninhado)

    # Chequei o caso mais fácil primeiro (todos iguais)
    if r1 == r2 and r2 == r3:
        print('Seu triângulo é EQUILATERO')

    # Chequei se TODOS os 3 lados são diferentes entre si.
    # (r1 != r2) E (r2 != r3) E (r1 != r3)
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('Seu triângulo é ESCALENO')

    # Se não for equilátero NEM escaleno, só pode ser isósceles.
    else:
        print('Seu triângulo é ISÓSCELES')

# 3. Se não puder formar um triângulo
else:
    print('Os segmentos NÃO PODEM FORMAR um triângulo.')