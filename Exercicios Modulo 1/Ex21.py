"""
Exercício 021: Faça um programa em Python que abra
e reproduza o áudio de um arquivo MP3.
"""

# Para tocar música, eu precisei importar a biblioteca 'pygame'
import pygame

# Tive que iniciar o pygame (e o mixer dele)
pygame.init()

print('Tocando a musica...')

# --- O Caminho do Arquivo ---
# 1. Usei 'pygame.mixer.music.load' para carregar.
# 2. Usei o r'...' (raw string) na frente do caminho
#    para o Python não se confundir com as barras '\' do Windows.
pygame.mixer.music.load(r'C:\Users\Gugux\OneDrive\Área de Trabalho\John Lennon.mp3')

# Dei o play
pygame.mixer.music.play()

# --- O Pulo do Gato ---
# Se eu não colocasse esse loop, o programa fecharia
# no mesmo segundo. O 'while' fica checando se a música
# 'está ocupada' (get_busy) e segura o script aberto até ela acabar.
while pygame.mixer.music.get_busy():
    pass

print('A música terminou de tocar.')