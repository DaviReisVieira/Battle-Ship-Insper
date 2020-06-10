import pygame
import random
import assets
from config import *

pygame.init()

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')


assets = assets.load_assets()

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
    def __init__(self, assets,laser_player, centery, posx, vx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[laser_player]
        self.rect = self.image.get_rect()
        self.rect.centery = centery
        self.rect.x = posx
        self.speedx = vx
    def update(self):
        self.rect.x += self.speedx

        if self.rect.x > WIDTH-SHIP_SIZE or self.rect.x < 0:
            self.kill()



class Ship(pygame.sprite.Sprite):
    def __init__(self, groups, assets, ship_player, posx):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[ship_player]
        self.rect = self.image.get_rect()
        self.rect.centery = int(HEIGHT/2)
        self.rect.x = posx
        self.speedy = 0
        self.groups = groups
        self.assets = assets
    
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        self.rect.y += self.speedy

        if self.rect.y > HEIGHT-SHIP_SIZE:
            self.rect.y = HEIGHT-SHIP_SIZE
        if self.rect.y < 0:
            self.rect.y = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now

            new_laser_1 = Laser(self.assets,'laser1', self.rect.centery, self.rect.x, 6)
            new_laser_2 = Laser(self.assets,'laser2', self.rect.centery, self.rect.x, -6)
            self.groups['all_sprites'].add(new_laser_1)
            self.groups['all_sprites'].add(new_laser_2)
            self.groups['all_lasers_1'].add(new_laser_1)
            self.groups['all_lasers_2'].add(new_laser_2)
            



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

for i in range(15):
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
    
    '''
    if game:
        # para o player 1
        hits = pygame.sprite.groupcollide(all_asteroids, all_lasers_1, True, True)
        for asteroids in hits:
            a = Asteroides(assets)
            all_sprites.add(a)
            all_asteroids.add(a)

        hits = pygame.sprite.spritecollide(player_1, all_asteroids, True)
        if hits:
            player_1.kill()
        hits = pygame.sprite.spritecollide(player_1, all_lasers_2, True)
        if hits:
            player_1.kill()

        # para o player 2
        hits = pygame.sprite.groupcollide(all_asteroids, all_lasers_2, True, True)
        for asteroids in hits:
            a = Asteroides(assets)
            all_sprites.add(a)
            all_asteroids.add(a)

        hits = pygame.sprite.spritecollide(player_2, all_asteroids, True)
        if hits:
            player_2.kill()
        hits = pygame.sprite.spritecollide(player_2, all_lasers_1, True)
        if hits:
            player_2.kill()
    else:
        game = False'''


    window.fill(BLACK)
    window.blit(assets['background'], (0,0))

    all_sprites.draw(window)

    pygame.display.update()

pygame.quit()
