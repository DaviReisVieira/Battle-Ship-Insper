import pygame
import random
import assets as assets_file
import os
import sys
from config import WIDTH, HEIGHT, BLACK, WHITE, ASTEROID_HEIGHT, ASTEROID_WIDTH, SHIP_AREA, SHIP_SIZE, SHIP_SPEED

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')


assets= assets_file.load_assets()

game = True

class Asteroides(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)

        self.image = assets['asteroids']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SHIP_AREA, WIDTH-ASTEROID_WIDTH-SHIP_AREA)
        self.rect.y = random.randint(-50, -ASTEROID_HEIGHT)
        self.speedy = random.randint(12, 15)

    def update(self):
        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(SHIP_AREA, WIDTH - ASTEROID_WIDTH-SHIP_AREA)
            self.rect.y = random.randint(-50, -ASTEROID_HEIGHT)
            self.speedy = random.randint(12, 15)


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, assets, centery, posx, vx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['laser']
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.x = posx
        self.speedx = vx
    
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x > WIDTH or self.rect.x < 0:
            self.kill()



class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets, ship_player, posx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ship_player]
        self.rect = self.image.get_rect()
        self.rect.centery = HEIGHT/2
        self.rect.x = posx
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    
    def update(self):
        self.rect.y += self.speedy

        if self.rect.y > HEIGHT-SHIP_SIZE:
            self.rect.y = HEIGHT-SHIP_SIZE
        if self.rect.y < 0:
            self.rect.y = 0



all_sprites = pygame.sprite.Group()
all_asteroids = pygame.sprite.Group()

groups = {}
groups['all_sprites'] = all_sprites
groups['all_asteroids'] = all_asteroids

player_1 = Ship(groups, assets,'ship1' , 0)
player_2 = Ship(groups, assets, 'ship2', WIDTH-SHIP_SIZE)

all_sprites.add(player_1)
all_sprites.add(player_2)

for i in range(30):
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

            #Player 2
            if event.key == pygame.K_UP:
                player_2.speedy -= SHIP_SPEED
            if event.key == pygame.K_DOWN:
                player_2.speedy += SHIP_SPEED

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
    
    window.fill(BLACK)
    window.blit(assets['background'], (0,0))

    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
