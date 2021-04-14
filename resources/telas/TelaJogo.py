import pygame
import random
import assets as assets_file
from classes import *
from config import *


def tela_jogo(TELA):

    assets = assets_file.load_assets()

    pygame.mixer.music.load('resources/music/background_music.wav')
    pygame.mixer.music.set_volume(1.0)

    pygame.mixer.music.play(loops =- 1)

    if CORONA:
        assets['corona_on_sound'].play()

    all_sprites = pygame.sprite.Group()
    all_asteroids = pygame.sprite.Group()
    all_lasers_1 = pygame.sprite.Group()
    all_lasers_2 = pygame.sprite.Group()
    all_star = pygame.sprite.Group()
    all_speed = pygame.sprite.Group()
    all_size = pygame.sprite.Group()
    all_powerups = pygame.sprite.Group()

    groups = {}
    groups['all_sprites'] = all_sprites
    groups['all_asteroids'] = all_asteroids
    groups['all_lasers_1'] = all_lasers_1
    groups['all_lasers_2'] = all_lasers_2
    groups['all_star'] = all_star
    groups['all_speed'] = all_speed
    groups['all_size'] = all_size
    groups['all_powerups'] = all_powerups

    player_1 = Ship(groups, assets,'ship1', 0)
    player_2 = Ship(groups, assets, 'ship2', WIDTH-SHIP_SIZE)

    all_sprites.add(player_1)
    all_sprites.add(player_2)

    for i in range(NUMERO_ASTEROIDES):
        asteroid = Asteroides(assets)
        all_sprites.add(asteroid)
        all_asteroids.add(asteroid)
        
    lista_Sprites = [all_sprites, all_asteroids, all_lasers_1, all_lasers_2]
    estado = GAME
    delta_tempo = 0

    score_player_1 = 0
    score_player_2 = 0

    player_1_lives = NUMERO_VIDAS
    player_2_lives = NUMERO_VIDAS

    star_player_1 = False
    star_player_2 = False

    player_1_dead = False
    player_2_dead = False

    def addPowerUpToGroups(powerUp):
        all_sprites.add(powerUp)
        all_powerups.add(powerUp)

    def createStar(powerUp):
        addPowerUpToGroups(powerUp)
        all_star.add(powerUp)

    def createSpeed(powerUp):
        addPowerUpToGroups(powerUp)
        all_speed.add(powerUp)

    def createSize(powerUp):
        addPowerUpToGroups(powerUp)
        all_size.add(powerUp)

    def createPowerUp(player):
        powerUpList=['star','speed','size']
        powerUpSelected=powerUpList[random.randint(0,2)]

        if powerUpSelected == 'star':
            createStar(PowerUp(assets, player, powerUpSelected))
        if powerUpSelected == 'speed':
            createSpeed(PowerUp(assets, player, powerUpSelected))
        if powerUpSelected == 'size':
            createSize(PowerUp(assets, player, powerUpSelected))
    
    clock = pygame.time.Clock()
    keys_down = {}
    while estado != TELA_FINAL and estado != QUIT:
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
            
            # Pressiona a tecla
            if event.type == pygame.KEYDOWN:
                keys_down[event.key] = True
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
                if event.key in keys_down and keys_down[event.key]:
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
            hits_laser_1_laser_2 = pygame.sprite.groupcollide(all_lasers_1, all_lasers_2, True, True, pygame.sprite.collide_mask)

            # ======= player 1 ========
            # ------ Power Ups ----------
            hits_player_1_estrelinha = pygame.sprite.spritecollide(player_1, all_star, True, pygame.sprite.collide_mask)
            if hits_player_1_estrelinha:
                assets['powerup_sound'].play()
                star_player_1 = True
                player_1.star_ship(True)
                tick_star_player_1 = pygame.time.get_ticks()

            agora = pygame.time.get_ticks()
            if star_player_1 and (agora - tick_star_player_1 > STAR_TIME):
                star_player_1 = False
                player_1.star_ship(False)

      
            hits_player_1_speed = pygame.sprite.spritecollide(player_1, all_speed, True, pygame.sprite.collide_mask)
            if hits_player_1_speed:
                assets['powerup_sound'].play()
                player_1.speed_multiplier()

            hits_player_1_size = pygame.sprite.spritecollide(player_1, all_size, True, pygame.sprite.collide_mask)
            if hits_player_1_size:
                assets['powerup_sound'].play()
                player_1.size_multiplier()

            hits_laser_1_powerups = pygame.sprite.groupcollide(all_lasers_1, all_powerups, True, True, pygame.sprite.collide_mask)

            #--------- Closisões ----------
            hits_asteroid_laser_1 = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True, pygame.sprite.collide_mask)
            for asteroid in hits_asteroid_laser_1: # colisão entre asteroids e lasers 1
                assets['explosion_sound'].play()
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

                score_player_1 += 100

                if score_player_1 % 1000 == 0:
                    createPowerUp(PLAYER_1)

            if star_player_1 == True:
                hits_player_1_asteroid = pygame.sprite.spritecollide(player_1, all_asteroids, True, pygame.sprite.collide_mask)
                for asteroid in  hits_player_1_asteroid: # colisão entre asteroids e player 1 com estrela
                    assets['explosion_sound'].play()
                    novo_asteroid = Asteroides(assets)
                    all_sprites.add(novo_asteroid)
                    all_asteroids.add(novo_asteroid)

                    explode_asteroid = Explode(assets, asteroid.rect.center)
                    all_sprites.add(explode_asteroid)
                hits_player_1_laser_2 = pygame.sprite.spritecollide(player_1, all_lasers_2, True, pygame.sprite.collide_mask)
            else:
                hits_player_1_asteroid = pygame.sprite.spritecollide(player_1, all_asteroids, True, pygame.sprite.collide_mask)
                if hits_player_1_asteroid: # colisão entre asteroids e player 1
                    assets['explosion_sound'].play()
                    explode_player_1 = Explode(assets, player_1.rect.center)
                    all_sprites.add(explode_player_1)
                    player_1.kill()
                    estado = EXPLODING 
                    
                    player_1_dead = True
                    player_1_lives -= 1
                    tick_explosao = pygame.time.get_ticks()
                    
                hits_player_1_laser_2 = pygame.sprite.spritecollide(player_1, all_lasers_2, True, pygame.sprite.collide_mask)
                if hits_player_1_laser_2: # colisão entre laser 2 e player 1
                    assets['explosion_sound'].play()
                    explode_player_1 = Explode(assets, player_1.rect.center)
                    all_sprites.add(explode_player_1)
                    player_1.kill()
                    estado = EXPLODING
                    player_1_dead = True
                    player_1_lives -=1
                    tick_explosao = pygame.time.get_ticks()


            # ======= player 2 ========
            # ------ Power Ups ----------
            hits_player_2_estrelinha = pygame.sprite.spritecollide(player_2, all_star, True, pygame.sprite.collide_mask)
            if hits_player_2_estrelinha:
                assets['powerup_sound'].play()
                star_player_2 = True
                player_2.star_ship(True)
                tick_star_player_2 = pygame.time.get_ticks()

            agora = pygame.time.get_ticks()
            if star_player_2 and (agora - tick_star_player_2 > STAR_TIME):
                star_player_2 = False
                player_2.star_ship(False)
                
            hits_player_2_speed = pygame.sprite.spritecollide(player_2, all_speed, True, pygame.sprite.collide_mask)
            if hits_player_2_speed:
                assets['powerup_sound'].play()
                player_2.speed_multiplier()

            hits_player_2_size = pygame.sprite.spritecollide(player_2, all_size, True, pygame.sprite.collide_mask)
            if hits_player_2_size:
                assets['powerup_sound'].play()
                player_2.size_multiplier()

            hits_laser_2_powerups = pygame.sprite.groupcollide(all_lasers_2, all_powerups, True, True, pygame.sprite.collide_mask)
            
            # -------- Colisões ------------
            hits_asteroid_laser_2 = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True, pygame.sprite.collide_mask)
            for asteroid in hits_asteroid_laser_2: # colisão entre asteroids e lasers 2
                assets['explosion_sound'].play()
                novo_asteroid = Asteroides(assets)
                all_sprites.add(novo_asteroid)
                all_asteroids.add(novo_asteroid)

                explode_asteroid = Explode(assets, asteroid.rect.center)
                all_sprites.add(explode_asteroid)

                score_player_2 += 100

                if score_player_2 % 1000 == 0:
                    createPowerUp(PLAYER_2)

            if star_player_2:
                hits_player_2_asteroid = pygame.sprite.spritecollide(player_2, all_asteroids, True, pygame.sprite.collide_mask)
                for asteroid in  hits_player_2_asteroid: # colisão entre asteroids e player 1 com estrela
                    assets['explosion_sound'].play()
                    novo_asteroid = Asteroides(assets)
                    all_sprites.add(novo_asteroid)
                    all_asteroids.add(novo_asteroid)

                    explode_asteroid = Explode(assets, asteroid.rect.center)
                    all_sprites.add(explode_asteroid)
                hits_player_2_laser_2 = pygame.sprite.spritecollide(player_2, all_lasers_1, True, pygame.sprite.collide_mask)
            else:
                hits_player_2_asteroid = pygame.sprite.spritecollide(player_2, all_asteroids, True, pygame.sprite.collide_mask)
                if hits_player_2_asteroid: # colisão entre asteroids e player 2
                    assets['explosion_sound'].play()
                    explode_player_2 = Explode(assets, player_2.rect.center)
                    all_sprites.add(explode_player_2)
                    player_2.kill()
                    estado = EXPLODING
                    
                    player_2_dead = True
                    player_2_lives -= 1
                    tick_explosao = pygame.time.get_ticks()
                    
                hits_player_2_laser_1 = pygame.sprite.spritecollide(player_2, all_lasers_1, True, pygame.sprite.collide_mask)
                if hits_player_2_laser_1: # colisão entre laser 1 e player 2
                    assets['explosion_sound'].play()
                    explode_player_2 = Explode(assets, player_2.rect.center)
                    all_sprites.add(explode_player_2)    
                    player_2.kill()
                    estado = EXPLODING 
                    player_2_dead = True
                    player_2_lives -=1
                    tick_explosao = pygame.time.get_ticks()
        
        # ---------- rotina de explosão do player
        elif estado == EXPLODING:
            agora = pygame.time.get_ticks()
            if agora - tick_explosao > DURACAO_EXPLOSAO:
                if player_1_dead:
                    if player_1_lives == 0:
                        estado = TELA_FINAL
                        vitoria = PLAYER_2
                    else:
                        player_2.kill()
                        player_1 = Ship(groups, assets,'ship1', 0)
                        player_2 = Ship(groups, assets, 'ship2', WIDTH-SHIP_SIZE)
                        all_sprites.add(player_1)
                        all_sprites.add(player_2)
                        keys_down = {}
                        player_1_dead = False
                        estado = GAME
                
                if player_2_dead:
                    if player_2_lives == 0:
                        estado = TELA_FINAL
                        vitoria = PLAYER_1
                    else:
                        player_1.kill()
                        player_1 = Ship(groups, assets,'ship1', 0)
                        player_2 = Ship(groups, assets, 'ship2', WIDTH-SHIP_SIZE)
                        all_sprites.add(player_1)
                        all_sprites.add(player_2)
                        keys_down = {}
                        player_2_dead = False
                        estado = GAME

        else:
            estado = TELA_FINAL


        TELA.fill(BLACK)
        TELA.blit(assets['background'], ORIGEM)

        all_sprites.draw(TELA)

        # ---------- Vidas dos players -----------
        if player_1_lives > 0:
            for lives in range(player_1_lives):
                TELA.blit(assets['heart'],(20 + 35 * lives, HEIGHT - 50))

        if player_2_lives > 0:
            for lives in range(player_2_lives):
                TELA.blit(assets['heart'],(WIDTH-55-35*lives,HEIGHT-50))

        # --------- Score do player 1 ------------- 
        text_surface = assets['font_score'].render("{:07d}".format(score_player_1), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (WIDTH / 4,  5)
        TELA.blit(text_surface, text_rect)    

        # --------- Score do player 2 ------------- 
        text_surface = assets['font_score'].render("{:07d}".format(score_player_2), True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (3*WIDTH / 4,  5)
        TELA.blit(text_surface, text_rect)   

        pygame.display.update()

    resultado = [estado, vitoria]
    return resultado
