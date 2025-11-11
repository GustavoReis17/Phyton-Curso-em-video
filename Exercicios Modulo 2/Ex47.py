"""
Exercício 047: Crie um programa que mostre na tela todos os
números pares que estão no intervalo entre 1 e 50.
(Versão Eficiente)
"""

# Importei o 'time' para dar a pausa
import time

print('=' * 50)
print('Aqui está todos os numeros pares entre 1 e 50')
print('=' * 50)

# --- O Pulo do Gato (O 'for' eficiente) ---
# Em vez de checar todos os números com 'if', eu usei
# o terceiro argumento do 'range()' que é o "passo" (step).
#
# range(2, 51, 2) significa:
# Comece no 2, vá ATÉ o 51 (sem incluir), pulando de 2 em 2.
#
# Assim, o 'for' já me dá só os números pares (2, 4, 6... 50)
# e eu não preciso de 'if' nenhum!
for i in range(2, 51, 2):
    print(i)
    # Pausei um pouquinho só pra ver o efeito
    time.sleep(0.2)

print('Fim !!!')