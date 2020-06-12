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
        
    lista_Sprites = [all_sprites,all_asteroids,all_lasers_1,all_lasers_2]
    estado = GAME
    delta_tempo = 0
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
                if event.key == pygame.K_a:
                    player_1.speedx -= SHIP_SPEED
                if event.key == pygame.K_d:
                    player_1.speedx += SHIP_SPEED
                if event.key == pygame.K_SPACE:
                    player_1.shoot()

                #Player 2
                if event.key == pygame.K_UP:
                    player_2.speedy -= SHIP_SPEED
                if event.key == pygame.K_DOWN:
                    player_2.speedy += SHIP_SPEED
                if event.key == pygame.K_LEFT:
                    player_2.speedx -= SHIP_SPEED
                if event.key == pygame.K_RIGHT:
                    player_2.speedx += SHIP_SPEED
                if event.key == pygame.K_RETURN:
                    player_2.shoot()

            # Solta a tecla
            if event.type == pygame.KEYUP:
                #Player 1
                if event.key == pygame.K_w:
                    player_1.speedy += SHIP_SPEED
                if event.key == pygame.K_s:
                    player_1.speedy -= SHIP_SPEED
                if event.key == pygame.K_a:
                    player_1.speedx += SHIP_SPEED
                if event.key == pygame.K_d:
                    player_1.speedx -= SHIP_SPEED

                #Player 2
                if event.key == pygame.K_UP:
                    player_2.speedy += SHIP_SPEED
                if event.key == pygame.K_DOWN:
                    player_2.speedy -= SHIP_SPEED
                if event.key == pygame.K_LEFT:
                    player_2.speedx += SHIP_SPEED
                if event.key == pygame.K_RIGHT:
                    player_2.speedx -= SHIP_SPEED
                
        all_sprites.update()
        

        if estado == GAME:
            # -------- player 1:
            hits_asteroid_laser_1 = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True)
            for asteroid in hits_asteroid_laser_1:
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

            hits_player_1_asteroid = pygame.sprite.spritecollide(player_1, all_asteroids, True)
            if hits_player_1_asteroid:
                explode_player_1 = Explode(assets, player_1.rect.center)
                all_sprites.add(explode_player_1)
                player_1.kill()
                estado = EXPLODING 
                vitoria = PLAYER_2
                tick_explosao = pygame.time.get_ticks()
                
            hits_player_1_laser_2 = pygame.sprite.spritecollide(player_1, all_lasers_2, True)
            if hits_player_1_laser_2:
                explode_player_1 = Explode(assets, player_1.rect.center)
                all_sprites.add(explode_player_1)
                player_1.kill()
                estado = EXPLODING
                vitoria = PLAYER_2
                tick_explosao = pygame.time.get_ticks()


            # ------- player 2
            hits_asteroid_laser_2 = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True)
            for asteroid in hits_asteroid_laser_2:
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

            hits_player_2_asteroid = pygame.sprite.spritecollide(player_2, all_asteroids, True)
            if hits_player_2_asteroid:
                explode_player_2 = Explode(assets, player_2.rect.center)
                all_sprites.add(explode_player_2)
                player_2.kill()
                estado = EXPLODING
                vitoria = PLAYER_1
                tick_explosao = pygame.time.get_ticks()
                
            hits_player_2_laser_1 = pygame.sprite.spritecollide(player_2, all_lasers_1, True)
            if hits_player_2_laser_1:
                explode_player_2 = Explode(assets, player_2.rect.center)
                all_sprites.add(explode_player_2)
                player_2.kill()
                estado = EXPLODING 
                vitoria = PLAYER_1
                tick_explosao = pygame.time.get_ticks()
        
        elif estado == EXPLODING:
            agora = pygame.time.get_ticks()
            if agora - tick_explosao > DURACAO_EXPLOSAO:
                estado = TELA_FINAL
        else:
            estado = TELA_FINAL


        TELA.fill(BLACK)
        TELA.blit(assets['background'], ORIGEM)

        all_sprites.draw(TELA)

        pygame.display.update()

    resultado = [estado, vitoria]
    return resultado
