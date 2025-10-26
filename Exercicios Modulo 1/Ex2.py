"""
Exercício 002: Faça um programa que leia o nome de uma pessoa
e mostre uma mensagem de boas-vindas.
"""

# Pedi o nome da pessoa e guardei na variável 'nome'
nome = input('Qual o seu nome?')

# Usei o .format() para colocar a variável 'nome'
# dentro do {} na mensagem de boas-vindas.
print ('Olá {}, Seja bem vindo !'.format(nome))