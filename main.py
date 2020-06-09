import pygame
import random
import os
import sys

pygame.init()
## GERA TELA PRINCIPAL:

# Resolução da Tela

WIDTH = 960
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')

# Cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ASTEROID_WIDTH=36
ASTEROID_HEIGHT=36
SHIP_SIZE=60
SHIP_AREA=80
SHIP_SPEED=6

#posx = {'cima':0,'baixo':0}
# assets:
assets={}
assets['background'] = pygame.image.load('resources/img/background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
assets['asteroids'] = pygame.image.load('resources/img/asteroids.png').convert_alpha()
assets['asteroids'] = pygame.transform.scale(assets['asteroids'], (ASTEROID_WIDTH,ASTEROID_HEIGHT))
assets['ship1'] = pygame.image.load('resources/img/ship1.png').convert_alpha()
assets['ship1'] = pygame.transform.scale(assets['ship1'], (SHIP_SIZE, SHIP_SIZE))
assets['ship1'] = pygame.transform.rotate(assets['ship1'], -90)
assets['ship2'] = pygame.image.load('resources/img/ship2.png').convert_alpha()
assets['ship2'] = pygame.transform.scale(assets['ship2'], (SHIP_SIZE, SHIP_SIZE))
assets['ship2'] = pygame.transform.rotate(assets['ship2'], 90)

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
    def __init__(self, groups, ):
        pygame.sprite.Sprite.__init__(self)


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
