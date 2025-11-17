"""
Exercício 057: Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto.
"""

# 1. O "Pulo do Gato" do 'while'
# Eu começo a variável 'Sexo' com 'A' (qualquer letra inválida)
# só para FORÇAR o loop 'while' a rodar pelo menos uma vez.
Sexo = 'A'

# 2. A Condição do 'while'
# "Enquanto a variável 'Sexo' NÃO FOR 'M' E NÃO FOR 'F', repita o loop"
while Sexo not in 'M' and Sexo not in 'F':

    # Pedi o sexo, já tratando com .upper() e .strip()
    Sexo = str(input('Digite seu sexo (M ou F): ')).upper().strip()

    # 3. O 'if' interno (a validação)
    # Se, depois do input, a variável 'Sexo' AINDA for inválida...
    if Sexo != 'M' and Sexo != 'F':
        # Eu aviso o usuário, e o 'while' vai repetir a pergunta.
        print('Você digitou uma opção invalida')

# 4. Saída do Loop
# O programa SÓ chega aqui se o 'while' for Falso
# (ou seja, se Sexo == 'M' ou Sexo == 'F')
if Sexo == 'M':
    print('=' * 20)
    print('Sexo masculino')
    print('=' * 20)
if Sexo == 'F':
    print('=' * 20)
    print('Sexo feminino')
    print('=' * 20)