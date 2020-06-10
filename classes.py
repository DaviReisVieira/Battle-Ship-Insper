import pygame
import assets
import random
from config import *



pygame.init()

def load_spritesheet(spritesheet, rows, columns):
    sprite_width = spritesheet.get_width() // columns
    sprite_height = spritesheet.get_height() // rows
    
    sprites = []
    for row in range(rows):
        for column in range(columns):
            x = column * sprite_width
            y = row * sprite_height
            dest_rect = pygame.Rect(x, y, sprite_width, sprite_height)

            image = pygame.Surface((sprite_width, sprite_height), pygame.SRCALPHA)
            image.blit(spritesheet, (0, 0), dest_rect)
            sprites.append(image)
            
    return sprites


class Asteroides(pygame.sprite.Sprite):
    def __init__(self, assets):

        pygame.sprite.Sprite.__init__(self)
        explosion_sheet = assets['explosion']
        explosion_sheet = pygame.transform.scale(explosion_sheet, (640, 640))
        spritesheet = load_spritesheet(explosion_sheet, 4, 4)
        self.animations = {
            EXPLOSION: spritesheet[0:16]
        }
        self.state = EXPLOSION
        self.animation = self.animations[self.state]
        self.frame = 0
        self.expl = self.animation[self.frame]
        self.rect = self.expl.get_rect()
        self.last_update = pygame.time.get_ticks()
        self.frame_ticks = 170

        self.image = assets['asteroids']
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SHIP_AREA, WIDTH-ASTEROID_WIDTH-SHIP_AREA)
        self.rect.y = random.randint(-100, -ASTEROID_HEIGHT)
        self.speedy = random.randint(9, 12)

    def update(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_update
        if elapsed_ticks > self.frame_ticks:
            self.last_update = now
            self.frame += 1
            self.animation = self.animations[self.state]
            if self.frame >= len(self.animation):
                self.frame = 0

        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(SHIP_AREA, WIDTH - ASTEROID_WIDTH-SHIP_AREA)
            self.rect.y = random.randint(-100, -ASTEROID_HEIGHT)
            self.speedy = random.randint(9, 12)


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

            new_laser_1 = Laser(self.assets,'laser1', self.rect.centery, self.rect.x, 20)
            new_laser_2 = Laser(self.assets,'laser2', self.rect.centery, self.rect.x, -20)
            self.groups['all_sprites'].add(new_laser_1)
            self.groups['all_sprites'].add(new_laser_2)
            self.groups['all_lasers_1'].add(new_laser_1)
            self.groups['all_lasers_2'].add(new_laser_2)


