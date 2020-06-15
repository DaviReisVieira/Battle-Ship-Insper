import pygame
from config import *
from os import path

pygame.init()
pygame.mixer.init()

def load_assets():
    assets = {}

    # ------ Imagens para o Fundo:
    assets['background'] = pygame.image.load('resources/img/background.png').convert_alpha()
    assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
    assets['Letreiro'] = pygame.image.load('resources/img/TelaInicialLetreiro.png').convert_alpha()
    assets['Letreiro'] = pygame.transform.scale(assets['Letreiro'], (WIDTH,HEIGHT))
    assets['Instrucoes'] = pygame.image.load('resources/img/TelaInicialInstrucoes.png').convert_alpha()
    assets['Instrucoes'] = pygame.transform.scale(assets['Instrucoes'], (WIDTH,HEIGHT))
    assets['PressKey'] = pygame.image.load('resources/img/TelaInicialPressKey.png').convert_alpha()
    assets['PressKey'] = pygame.transform.scale(assets['PressKey'], (WIDTH,HEIGHT))
    assets['TelaFinal'] = pygame.image.load('resources/img/TelaFinalDivisao.png').convert_alpha()
    assets['TelaFinal'] = pygame.transform.scale(assets['TelaFinal'], (WIDTH,HEIGHT))
    assets['PressSpace'] = pygame.image.load('resources/img/TelaFinalPressSpace.png').convert_alpha()
    assets['PressSpace'] = pygame.transform.scale(assets['PressSpace'], (WIDTH,HEIGHT))
    assets['Player1Win'] = pygame.image.load('resources/img/TelaFinalPlayer1Win.png').convert_alpha()
    assets['Player1Win'] = pygame.transform.scale(assets['Player1Win'], (WIDTH,HEIGHT))
    assets['Player2Win'] = pygame.image.load('resources/img/TelaFinalPlayer2Win.png').convert_alpha()
    assets['Player2Win'] = pygame.transform.scale(assets['Player2Win'], (WIDTH,HEIGHT))

    # ------- Imagens para o jogo:
    if CORONA:
        assets['asteroids'] = pygame.image.load('resources/img/asteroid_corona.png').convert_alpha()
    else:
        lista_asteroids = []
        for e in range(0,IMAGEM_ASTEROIDES):
            file_asteroids = 'resources/img/asteroide0{}.png'.format(e)
            asteroid = pygame.image.load(file_asteroids).convert_alpha()
            lista_asteroids.append(asteroid)
        assets['asteroids'] = lista_asteroids

    assets['ship1'] = pygame.image.load('resources/img/NavePlayer1.png').convert_alpha()
    assets['ship1'] = pygame.transform.scale(assets['ship1'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship1'] = pygame.transform.rotate(assets['ship1'], -90)
    assets['ship1_star'] = pygame.image.load('resources/img/NavePlayer1Star.png').convert_alpha()
    assets['ship1_star'] = pygame.transform.scale(assets['ship1_star'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship1_star'] = pygame.transform.rotate(assets['ship1_star'], -90)
    assets['ship2'] = pygame.image.load('resources/img/NavePlayer2.png').convert_alpha()
    assets['ship2'] = pygame.transform.scale(assets['ship2'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship2'] = pygame.transform.rotate(assets['ship2'], 90)
    assets['ship2_star'] = pygame.image.load('resources/img/NavePlayer2Star.png').convert_alpha()
    assets['ship2_star'] = pygame.transform.scale(assets['ship2_star'], (SHIP_SIZE, SHIP_SIZE))
    assets['ship2_star'] = pygame.transform.rotate(assets['ship2_star'], 90)
    assets['laser1'] = pygame.image.load('resources/img/bullet1.png').convert_alpha()
    assets['laser2'] = pygame.image.load('resources/img/bullet2.png').convert_alpha()
    assets['star'] = pygame.image.load('resources/img/PowerStar.png').convert_alpha()
    assets['star'] = pygame.transform.scale(assets['star'], (POWERUP_SIZE,POWERUP_SIZE))
    assets['speed'] = pygame.image.load('resources/img/PowerSpeed.png').convert_alpha()
    assets['speed'] = pygame.transform.scale(assets['speed'], (POWERUP_SIZE,POWERUP_SIZE))
    assets['size'] = pygame.image.load('resources/img/PowerSize.png').convert_alpha()
    assets['size'] = pygame.transform.scale(assets['size'], (POWERUP_SIZE,POWERUP_SIZE))
    assets['heart'] = pygame.image.load('resources/img/Vida.png').convert_alpha()
    assets['heart'] = pygame.transform.scale(assets['heart'], (HEART_SIZE,HEART_SIZE))
    explosion = []
    for e in range(NUMERO_FRAMES):
        file = 'resources/img/regularExplosion0{}.png'.format(e)
        img = pygame.image.load(file).convert_alpha()
        img =  pygame.transform.scale(img, (40, 40))
        explosion.append(img)
    assets['explosion'] = explosion

    # carrega sons
    pygame.mixer.music.load('resources/sounds/background_music.mp3')
    pygame.mixer.music.set_volume(0.4)
    assets['corona_on_sound'] = pygame.mixer.Sound('resources/sounds/coronaon.wav')
    assets['lost1_sound'] = pygame.mixer.Sound('resources/sounds/coronaon.wav')
    assets['lost2_sound'] = pygame.mixer.Sound('resources/sounds/coronaon.wav')
    assets['menu1_sound'] = pygame.mixer.Sound('resources/sounds/menu.wav')
    assets['menu2_sound'] = pygame.mixer.Sound('resources/sounds/menu2.wav')
    assets['explosion_sound'] = pygame.mixer.Sound('resources/sounds/explosion1.wav')
    assets['laser1_sound'] = pygame.mixer.Sound('resources/sounds/coronaon.wav')
    assets['laser2_sound'] = pygame.mixer.Sound('resources/sounds/coronaon.wav')

    return assets