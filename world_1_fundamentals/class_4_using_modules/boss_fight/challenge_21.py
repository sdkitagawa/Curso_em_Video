'''
Make a Python program that opens and plays audio from an MP3 file.

'''

import pygame

pygame.init()
pygame.mixer.music.load("challenge_21_pkbm.mp3")
pygame.mixer.music.play
pygame.event.wait()
