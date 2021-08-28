# Faça um programa em Python que abra e reproduza o áudio
# de um arquivo MP3
import pygame
pygame.init()
pygame.mixer.music.load('Game Music 10.mp3')
pygame.mixer.music.play()
input()
"""Só funcionou depois que adicionei o input(), pesquisado em 
stackoverflow em português"""
pygame.event.wait()
