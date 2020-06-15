import pygame
import assets
import random
from config import *



pygame.init()
pygame.mixer.init()

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

class Star(pygame.sprite.Sprite):
    def __init__(self, assets, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = assets['star']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if player == PLAYER_1:
            self.rect.x = random.randint(SHIP_AREA, WIDTH/2-SHIP_SIZE) # ajeitar
        else:
            self.rect.x = random.randint(WIDTH/2+SHIP_SIZE, WIDTH-SHIP_AREA) # ajeitar
        self.rect.y = random.randint(-820, -100) # ajeitar
        self.speedy = POWERUP_SPEED

    def update(self):

        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.kill()

class Speed(pygame.sprite.Sprite):
    def __init__(self, assets, player):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['speed']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if player == PLAYER_1:
            self.rect.x = random.randint(SHIP_AREA, WIDTH/2-SHIP_SIZE) # ajeitar
        else:
            self.rect.x = random.randint(WIDTH/2+SHIP_SIZE, WIDTH-SHIP_AREA) # ajeitar
        self.rect.y = random.randint(-820, -100) # ajeitar
        self.speedy = POWERUP_SPEED

    def update(self):

        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.kill()

class Size(pygame.sprite.Sprite):
    def __init__(self, assets, player):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets['size']
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        if player == PLAYER_1:
            self.rect.x = random.randint(SHIP_AREA, WIDTH/2-SHIP_SIZE) # ajeitar
        else:
            self.rect.x = random.randint(WIDTH/2+SHIP_SIZE, WIDTH-SHIP_AREA) # ajeitar
        self.rect.y = random.randint(-820, -100) # ajeitar
        self.speedy = POWERUP_SPEED

    def update(self):

        self.rect.y += self.speedy

        if self.rect.top > HEIGHT:
            self.kill()
            
class Asteroides(pygame.sprite.Sprite):
    def __init__(self, assets):
        pygame.sprite.Sprite.__init__(self)

        if CORONA:
            imagem_asteroide = assets['asteroids']
        else:
            imagem_asteroide = assets['asteroids'][random.randint(0,3)]

        self.image = imagem_asteroide
        self.random =random.randint(75,125)
        self.original_image = pygame.transform.scale(self.image, (self.random,self.random))
        self.image = self.original_image
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(SHIP_AREA, WIDTH-ASTEROID_WIDTH-SHIP_AREA)
        self.rect.y = random.randint(-820, -100)
        self.speedy = random.randint(4, 5)
        #self.rotate = 0

    def update(self):

        self.rect.y += self.speedy
        #self.image = pygame.transform.rotate(self.original_image,self.rotate)
        #self.rotate += 1%360
        

        if self.rect.top > HEIGHT:
            self.rect.x = random.randint(SHIP_AREA, WIDTH - ASTEROID_WIDTH-SHIP_AREA)
            self.rect.y = random.randint(-100, -ASTEROID_HEIGHT)
            self.speedy = random.randint(4, 5)
            self.image = pygame.transform.scale(self.image, (self.random,self.random))


class Laser(pygame.sprite.Sprite):
    def __init__(self, assets, laser_player, centery, posx, vx, scale):
        pygame.sprite.Sprite.__init__(self)

        self.image = assets[laser_player]
        self.image = pygame.transform.scale(self.image, (int(LASER_SIZE*scale), int(LASER_SIZE*scale)))
        self.mask = pygame.mask.from_surface(self.image)
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
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.centery = int(HEIGHT/2)
        self.rect.x = posx
        self.speedx = 0
        self.speedy = 0
        self.player = ship_player
        self.groups = groups
        self.assets = assets
        self.scale = 1
    
        self.last_shot = pygame.time.get_ticks()
        self.shoot_ticks = 500

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy


        if self.rect.x > WIDTH-SHIP_SIZE:
            self.rect.x = WIDTH-SHIP_SIZE
        if self.rect.x < 0:
            self.rect.x = 0
        if self.player == 'ship1' and self.rect.x > int(WIDTH/2) - SHIP_SIZE:
            self.rect.x = int(WIDTH/2)-SHIP_SIZE
        if self.player == 'ship2' and self.rect.x < int(WIDTH/2) + SHIP_SIZE:
            self.rect.x = int(WIDTH/2)+SHIP_SIZE
        
        if self.rect.y > HEIGHT-SHIP_SIZE:
            self.rect.y = HEIGHT-SHIP_SIZE
        if self.rect.y < 0:
            self.rect.y = 0

    def shoot(self):
        now = pygame.time.get_ticks()
        elapsed_ticks = now - self.last_shot

        if elapsed_ticks > self.shoot_ticks:
            self.last_shot = now

            if self.player == 'ship1':
                new_laser_1 = Laser(self.assets,'laser1', self.rect.centery, self.rect.x, LASER_SPEED, self.scale)
                self.groups['all_sprites'].add(new_laser_1)
                self.groups['all_lasers_1'].add(new_laser_1)
                #self.assets['laser1_sound'].play()

            if self.player == 'ship2':
                new_laser_2 = Laser(self.assets,'laser2', self.rect.centery, self.rect.x, -LASER_SPEED, self.scale)
                self.groups['all_sprites'].add(new_laser_2)
                self.groups['all_lasers_2'].add(new_laser_2)            
                #self.assets['laser2_sound'].play()

    def star_ship(self, state):
        if state:
            if self.player == 'ship1':
                self.image = self.assets['ship1_star']
            if self.player == 'ship2':
                self.image = self.assets['ship2_star']
        else:
            self.image = self.assets[self.player]

    def speed_multiplier(self):
        if self.shoot_ticks > 100:
            self.shoot_ticks -= 100

    def size_multiplier(self):
        if self.scale < 5:
            self.scale += 0.5



class Explode(pygame.sprite.Sprite):
    def __init__(self, assets, center):
        pygame.sprite.Sprite.__init__(self)

        self.explosion = assets['explosion']

        self.frame = 0
        self.image = self.explosion[self.frame]
        self.rect = self.image.get_rect()
        self.rect.center = center

        self.last = pygame.time.get_ticks()

    def update(self):

        now = pygame.time.get_ticks()

        elapsed_ticks = now - self.last

        if elapsed_ticks > FRAME_TICKS:
            self.last = now
            self.frame += 1

            if self.frame == len(self.explosion):
                self.kill()
            else:
                center = self.rect.center
                self.image = self.explosion[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


