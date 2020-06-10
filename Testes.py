import pygame
import assets as assets_file
from config import WIDTH, HEIGHT, BLACK

pygame.init()

# Resolução da Tela
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')
lastFlick = 0

QUIT = 0
TELA_INICIAL = 1
INSTRUCOES = 2


assets = assets_file.load_assets()

game = TELA_INICIAL

clock = pygame.time.Clock()

while game != QUIT:
    clock.tick(30)
      
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = QUIT
        if event.type == pygame.KEYDOWN:
            game = INSTRUCOES

                
    if game == TELA_INICIAL:
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
    
    elif game == INSTRUCOES:
        window.fill(BLACK)

        window.blit(assets['background'], (0,0))
        
        window.blit(assets['Instrucoes'], (0,0))

        if lastFlick < 30:
            window.blit(assets['PressKey'], (0,0))
            lastFlick += 1
        elif lastFlick == 59:
            lastFlick = 0
        else:
            lastFlick += 1

        pygame.display.update()


pygame.quit()