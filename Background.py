import pygame
## made by me

pygame.init()

# Resolução da Tela

WIDTH = 960
HEIGHT = 720
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')
lastFlick = 0

# cores:
BLACK = (0,0,0)


assets={}
assets['background'] = pygame.image.load('resources/img/background.png').convert()
assets['background'] = pygame.transform.scale(assets['background'], (WIDTH,HEIGHT))
assets['Letreiro'] = pygame.image.load('resources/img/TelaInicialLetreiro.png').convert_alpha()
assets['PressKey'] = pygame.image.load('resources/img/TelaInicialPressKey.png').convert_alpha()

game = True

clock = pygame.time.Clock()

while game:
    clock.tick(30)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
                
    
    window.fill(BLACK)

    window.blit(assets['background'], (0,0))
    
    window.blit(assets['Letreiro'], (0,0))

    if lastFlick < 30:
        window.blit(assets['PressKey'], (0,0))
        lastFlick += 1
    elif lastFlick == 59:
        lastFlick = 0
    else:
        lastFlick += 1

    pygame.display.update()

pygame.quit()