#================================================================================
'''  Exercicio 021:
    Faca um programa que abra e reproduza um audio de arquivo mp3.
'''
#================================================================================
import pygame
pygame.init()
pygame.mixer.music.load('Exercicio021(TocarMusica).mp3')
pygame.mixer.music.play()
pygame.event.wait()
print('=' * 45)
print('\033[1;36mESTA TOCANDO...\033[m')
print('\033[1;35mFool Me (feat. Nanette, Baby S.O.N & Jay Sax)\033[m')
print('\033[1;34mKelvin Momo\033[m - \033[1;36mAMUKELANI\033[m')
print('=' * 45)

