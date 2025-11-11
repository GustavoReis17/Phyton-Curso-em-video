"""
Exercício 046: Faça um programa que mostre na tela uma
contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

# Importei a 'time' para poder usar a pausa
import time

print('=' * 50)
print('Vai começar a contagem regressiva para os fogos...')
print('=' * 50)

# --- O Pulo do Gato (O 'for' loop) ---
# Aqui eu usei o 'for' pela primeira vez!
# 'range(10, 0, -1)' significa:
# Comece em 10, vá ATÉ o 0 (sem incluir ele), pulando de -1 em -1.
for m in range(10, 0, -1):
    print(m)
    # Usei o 'time.sleep(1)' para pausar 1 segundo
    time.sleep(1)

# (O exercício pedia pra ir até 0, mas o estouro já é o 0!)
print('=' * 20)
print('Feliz ano novo!!!')
print('=' * 20)