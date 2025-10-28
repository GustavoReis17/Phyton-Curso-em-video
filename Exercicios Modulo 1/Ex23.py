"""
Exercício 023: Faça um programa que leia um número de 0 a 9999
e mostre na tela cada um dos dígitos separados
(unidade, dezena, centena, milhar).
"""

# Pedi o número ao usuário
Numero = int (input('Digite um numero de 0 a 9999: '))

# --- O "Pulo do Gato" (Método da String) ---
# Achei bem mais fácil do que fazer a matemática de divisão.
# Eu uso a f-string :04d para forçar o número a ter 4 dígitos.
# Ex: 123 vira "0123". 5 vira "0005".
Formatado = f'{Numero:04d}'

# Agora que 'Formatado' é uma string, eu pego cada dígito pela posição.
# Lembrei que a ordem é inversa: o índice 0 é o milhar e o 3 é a unidade.
Unidade = Formatado[3]
Dezena = Formatado[2]
Centena = Formatado[1]
Milhar = Formatado[0]

# Na hora de mostrar, eu imprimo o 'Numero' original, pra não ficar "0123" feio.
print (f'O numero digitado foi {Numero}')
# E aqui eu mostro cada dígito que separei.
print (f'Unidade: {Unidade}')
print (f'Dezena: {Dezena}')
print (f'Centena: {Centena}')
print (f'Milhar: {Milhar}')