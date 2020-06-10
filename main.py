import pygame
import assets
from config import *
from classes import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_icon(pygame.image.load('resources/img/gameicon.png'))
pygame.display.set_caption('Space Battle')


assets = assets.load_assets()


game = True


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

for i in range(7):
    asteroid = Asteroides(assets)
    all_sprites.add(asteroid)
    all_asteroids.add(asteroid)
    
game = True

clock = pygame.time.Clock()

while game:
    clock.tick(30)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        
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
    

    if game:
        # para o player 1
        hits1 = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True)
        for asteroids in hits1:
            a = Asteroides(assets)
            all_sprites.add(a)
            all_asteroids.add(a)

        hits2 = pygame.sprite.spritecollide(player_1, all_asteroids, True)
        if hits2:
            player_1.kill()
        hits3 = pygame.sprite.spritecollide(player_1, all_lasers_2, True)
        if hits3:
            player_1.kill()

        # para o player 2
        hits4 = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True)
        for asteroids in hits4:
            a = Asteroides(assets)
            all_sprites.add(a)
            all_asteroids.add(a)

        hits5 = pygame.sprite.spritecollide(player_2, all_asteroids, True)
        if hits5:
            player_2.kill()
        hits6 = pygame.sprite.spritecollide(player_2, all_lasers_1, True)
        if hits6:
            player_2.kill()
    else:
        game = False


    window.fill(BLACK)
    window.blit(assets['background'], (0,0))

    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
