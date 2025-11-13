"""
Exercício 048: Faça um programa que calcule a soma entre todos
os números ímpares que são múltiplos de três
e que se encontram no intervalo de 1 até 500.
"""

# Comecei o 'Soma' (que é o meu ACUMULADOR) com 0
Soma = 0

# --- O Pulo do Gato (O 'for' eficiente) ---
# Eu já fiz o 'for' pular de 2 em 2 (range(1, 501, 2))
# Assim, o 'i' SÓ vai valer números ÍMPARES (1, 3, 5, 7...)
for i in range(1, 501, 2):

    # Como eu já sei que 'i' é ímpar,
    # eu só preciso checar se ele é MÚLTIPLO DE 3 (resto 0)
    if i % 3 == 0:
        # Se ele for ÍMPAR e MÚLTIPLO DE 3, eu adiciono ele ao 'Soma'
        # O 'Soma += i' é o mesmo que 'Soma = Soma + i'
        Soma += i

# --- Impressão Final (Versão Limpa) ---
# No final do loop, eu mostro a soma total.
print('=' * 50)
print(f'A soma dos numeros impares que são multiplos de 3 é...{Soma}')
print('=' * 50)