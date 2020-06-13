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
    all_star = pygame.sprite.Group()
    all_speed = pygame.sprite.Group()
    all_size = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_asteroids'] = all_asteroids
    groups['all_lasers_1'] = all_lasers_1
    groups['all_lasers_2'] = all_lasers_2
    groups['all_star'] = all_star
    groups['all_speed'] = all_speed
    groups['all_size'] = all_size

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

    star_player_1 = False
    star_player_2 = False
    
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
            hits_player_1_estrelinha = pygame.sprite.spritecollide(player_1, all_star, True, pygame.sprite.collide_mask)
            if hits_player_1_estrelinha:
                star_player_1 = True
                tick_star_player_1 = pygame.time.get_ticks()
                nova_star = Star(assets)
                all_sprites.add(nova_star)
                all_star.add(nova_star)

            agora = pygame.time.get_ticks()
            if star_player_1 and tick_star_player_1 - agora > STAR_TIME:
                star_player_1 = False
      
            ##hits_player_1_speed = pygame.sprite.spritecollide(player_1, all_speed, True, pygame.sprite.collide_mask)
            #if hits_player_1_speed:

           # for speed in hits_player_1_speed:
               # novo_speed = Speed(assets)
               ## all_sprites.add(novo_speed)
                #all_speed.add(novo_speed)

            #hits_player_1_size = pygame.sprite.spritecollide(player_1, all_size, True, pygame.sprite.collide_mask)
            #if hits_player_1_size:

            #for size in hits_player_1_size:
                #novo_size = Size(assets)
                #all_sprites.add(novo_size)
                #all_size.add(novo_size)
            #--------------------
            hits_asteroid_laser_1 = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True, pygame.sprite.collide_mask)
            for asteroid in hits_asteroid_laser_1: # colisão entre asteroids e lasers 1
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

            hits_player_1_asteroid = pygame.sprite.spritecollide(player_1, all_asteroids, True, pygame.sprite.collide_mask)
            if hits_player_1_asteroid: # colisão entre asteroids e player 1
                explode_player_1 = Explode(assets, player_1.rect.center)
                all_sprites.add(explode_player_1)
                if star_player_1 == False:
                    player_1.kill()
                estado = EXPLODING 
                vitoria = PLAYER_2
                tick_explosao = pygame.time.get_ticks()
                
            hits_player_1_laser_2 = pygame.sprite.spritecollide(player_1, all_lasers_2, True, pygame.sprite.collide_mask)
            if hits_player_1_laser_2: # colisão entre laser 2 e player 1
                explode_player_1 = Explode(assets, player_1.rect.center)
                all_sprites.add(explode_player_1)
                if star_player_1 == False:
                    player_1.kill()
                player_1.kill()
                estado = EXPLODING
                vitoria = PLAYER_2
                tick_explosao = pygame.time.get_ticks()


            # ------- player 2
            hits_player_2_estrelinha = pygame.sprite.spritecollide(player_2, all_star, True, pygame.sprite.collide_mask)
            if hits_player_2_estrelinha:
                star_player_2 = True
                
            for star in hits_player_2_estrelinha:
                nova_star = Star(assets)
                all_sprites.add(nova_star)
                all_star.add(nova_star)
                
            #hits_player_2_speed = pygame.sprite.spritecollide(player_2, all_speed, True, pygame.sprite.collide_mask)
            #if hits_player_2_speed:

            ''' 
            for speed in hits_player_2_speed:
                novo_speed = Speed(assets)
                all_sprites.add(novo_speed)
                all_speed.add(novo_speed)

            hits_player_2_size = pygame.sprite.spritecollide(player_2, all_size, True, pygame.sprite.collide_mask)
            if hits_player_2_size:

            for size in hits_player_2_size:
                novo_size = Size(assets)
                all_sprites.add(novo_size)
                all_size.add(novo_size)'''
            #--------------------
            hits_asteroid_laser_2 = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True, pygame.sprite.collide_mask)
            for asteroid in hits_asteroid_laser_2: # colisão entre asteroids e lasers 2
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

            hits_player_2_asteroid = pygame.sprite.spritecollide(player_2, all_asteroids, True, pygame.sprite.collide_mask)
            if hits_player_2_asteroid: # colisão entre asteroids e player 2
                explode_player_2 = Explode(assets, player_2.rect.center)
                all_sprites.add(explode_player_2)
                if star_player_2 == False:
                    player_2.kill()
                estado = EXPLODING
                vitoria = PLAYER_1
                tick_explosao = pygame.time.get_ticks()
                
            hits_player_2_laser_1 = pygame.sprite.spritecollide(player_2, all_lasers_1, True, pygame.sprite.collide_mask)
            if hits_player_2_laser_1: # colisão entre laser 1 e player 2
                explode_player_2 = Explode(assets, player_2.rect.center)
                all_sprites.add(explode_player_2)
                if star_player_2 == False:
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
