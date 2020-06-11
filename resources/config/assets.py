import pygame
from config import *
from os import path

pygame.init()

def load_assets():
    assets = {}

    # ------ Imagens para o Fundo:
    assets['background'] = pygame.image.load('resources/img/background.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets['Letreiro'] = pygame.image.load('resources/img/TelaInicialLetreiro.png').convert_alpha()
    assets['Instrucoes'] = pygame.image.load('resources/img/TelaInicialInstrucoes.png').convert_alpha()
    assets['PressKey'] = pygame.image.load('resources/img/TelaInicialPressKey.png').convert_alpha()
    assets['TelaFinal'] = pygame.image.load('resources/img/TelaFinalDivisao.png').convert_alpha()
    assets['PressSpace'] = pygame.image.load('resources/img/TelaFinalPressSpace.png').convert_alpha()
    assets['Player1Win'] = pygame.image.load('resources/img/TelaFinalPlayer1Win.png').convert_alpha()
    assets['Player2Win'] = pygame.image.load('resources/img/TelaFinalPlayer2Win.png').convert_alpha()

    # ------- Imagens para o jogo:
    assets['asteroids'] = pygame.image.load('resources/img/asteroid_corona.png').convert_alpha()
    assets['asteroids'] = pygame.transform.scale(assets['asteroids'], (ASTEROID_WIDTH,ASTEROID_HEIGHT))
    assets['ship1'] = pygame.image.load('resources/img/ship1.png').convert_alpha()
    assets['ship1'] = pygame.transform.scale(assets['ship1'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship1'] = pygame.transform.rotate(assets['ship1'], -90)
    assets['ship2'] = pygame.image.load('resources/img/ship2.png').convert_alpha()
    assets['ship2'] = pygame.transform.scale(assets['ship2'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship2'] = pygame.transform.rotate(assets['ship2'], 90)
    assets['laser1'] = pygame.image.load('resources/img/bullet1.png').convert_alpha()
    assets['laser2'] = pygame.image.load('resources/img/bullet2.png').convert_alpha()
    
    explosion = []
    for e in range(NUMERO_FRAMES):
        file = 'resources/img/regularExplosion0{}.png'.format(e)
        img = pygame.image.load(file).convert_alpha()
        img =  pygame.transform.scale(img, (40, 40))
        explosion.append(img)
    assets['explosion'] = explosion

    return assets