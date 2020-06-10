import pygame
from config import WIDTH, HEIGHT, ASTEROID_WIDTH, ASTEROID_HEIGHT, SHIP_SIZE, BLACK
from os import path

pygame.init()

def load_assets():
    assets = {}
    assets['background'] = pygame.image.load('resources/img/background.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets['Letreiro'] = pygame.image.load('resources/img/TelaInicialLetreiro.png').convert_alpha()
    assets['Instrucoes'] = pygame.image.load('resources/img/TelaInicialInstrucoes.png').convert_alpha()
    assets['PressKey'] = pygame.image.load('resources/img/TelaInicialPressKey.png').convert_alpha()
    assets['asteroids'] = pygame.image.load('resources/img/asteroids.png').convert_alpha()
    assets['asteroids'] = pygame.transform.scale(assets['asteroids'], (ASTEROID_WIDTH,ASTEROID_HEIGHT))
    assets['ship1'] = pygame.image.load('resources/img/ship1.png').convert_alpha()
    assets['ship1'] = pygame.transform.scale(assets['ship1'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship1'] = pygame.transform.rotate(assets['ship1'], -90)
    assets['ship2'] = pygame.image.load('resources/img/ship2.png').convert_alpha()
    assets['ship2'] = pygame.transform.scale(assets['ship2'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship2'] = pygame.transform.rotate(assets['ship2'], 90)
    assets['laser'] = pygame.image.load('resources/img/bullet.png').convert_alpha()
    return assets