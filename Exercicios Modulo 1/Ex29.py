"""
Exercício 029: Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""

# Pedi a velocidade em float, porque ela pode ser 80.5 Km/h
Velocidade = float (input('Digite a velocidade em Km/h: '))

# Só multa se for MAIOR que 80
if Velocidade > 80:
    # O cálculo da multa:
    # 1. (Velocidade - 80) -> Pega só o que passou do limite
    # 2. (...) * 7         -> Multiplica por R$7,00
    # 3. :.2f              -> Formata para dinheiro (duas casas decimais)
    print(f'Você foi multado \n o valor da multa é R${(Velocidade- 80) * 7:.2f} ')
else:
    # Se for 80 ou menos, não foi multado
    print(f'Parabens, você não foi multado')