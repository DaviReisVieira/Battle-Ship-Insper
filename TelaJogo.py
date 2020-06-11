import pygame
import random
import assets as assets_file
from classes import *
from config import *


def tela_jogo(TELA):

    assets = assets_file.load_assets()

    all_sprites = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_lasers_1 = pygame.sprite.Group()
    all_lasers_2 = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_asteroids'] = all_asteroids
    groups['all_lasers_1'] = all_lasers_1
    groups['all_lasers_2'] = all_lasers_2

    player_1 = Ship(groups, assets,'ship1', 0)
    player_2 = Ship(groups, assets, 'ship2', WIDTH-SHIP_SIZE)

    all_sprites.add(player_1)
    all_sprites.add(player_2)

    for i in range(NUMERO_ASTEROIDES):
        asteroid = Asteroides(assets)
        all_sprites.add(asteroid)
        all_asteroids.add(asteroid)
        
    estado = GAME

    clock = pygame.time.Clock()

    while estado != TELA_FINAL and estado != QUIT:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
            
            # Pressiona a tecla
            if event.type == pygame.KEYDOWN:
                #Player 1
                if event.key == pygame.K_w:
                    player_1.speedy -= SHIP_SPEED
                if event.key == pygame.K_s:
                    player_1.speedy += SHIP_SPEED
                if event.key == pygame.K_SPACE:
                    player_1.shoot()

                #Player 2
                if event.key == pygame.K_UP:
                    player_2.speedy -= SHIP_SPEED
                if event.key == pygame.K_DOWN:
                    player_2.speedy += SHIP_SPEED
                if event.key == pygame.K_RETURN:
                    player_2.shoot()

            # Solta a tecla
            if event.type == pygame.KEYUP:
                #Player 1
                if event.key == pygame.K_w:
                    player_1.speedy += SHIP_SPEED
                if event.key == pygame.K_s:
                    player_1.speedy -= SHIP_SPEED

                #Player 2
                if event.key == pygame.K_UP:
                    player_2.speedy += SHIP_SPEED
                if event.key == pygame.K_DOWN:
                    player_2.speedy -= SHIP_SPEED
                
        all_sprites.update()
        

        if estado == GAME:
            # para o player 1
            hits1 = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True)
            for asteroids in hits1:
                a = Asteroides(assets)
                all_sprites.add(a)
                all_asteroids.add(a)

            hits2 = pygame.sprite.spritecollide(player_1, all_asteroids, True)
            if hits2:
                player_1.kill()
                estado = TELA_FINAL
                vitoria = PLAYER_2
            hits3 = pygame.sprite.spritecollide(player_1, all_lasers_2, True)
            if hits3:
                player_1.kill()
                estado = TELA_FINAL
                vitoria = PLAYER_2


            # para o player 2
            hits4 = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True)
            for asteroids in hits4:
                a = Asteroides(assets)
                all_sprites.add(a)
                all_asteroids.add(a)

            hits5 = pygame.sprite.spritecollide(player_2, all_asteroids, True)
            if hits5:
                player_2.kill()
                estado = TELA_FINAL
                vitoria = PLAYER_1
            hits6 = pygame.sprite.spritecollide(player_2, all_lasers_1, True)
            if hits6:
                player_2.kill()
                estado = TELA_FINAL
                vitoria = PLAYER_1
        else:
            estado = TELA_FINAL


        TELA.fill(BLACK)
        TELA.blit(assets['background'], ORIGEM)

        all_sprites.draw(TELA)

        pygame.display.update()

    resultado = [estado, vitoria]
    return resultado
