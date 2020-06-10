import pygame
import assets as assets_file
from config import WIDTH, HEIGHT, BLACK, FPS, ORIGEM

pygame.init()

# Resolução da Tela
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Space Battle')
lastFlick = 0

QUIT = 0
TELA_INICIAL = 1
INSTRUCOES = 2
GAME = 3
TELA_FINAL = 4

WIN = 2

assets = assets_file.load_assets()

clock = pygame.time.Clock()
game = TELA_FINAL
last_flick = 0  # Press Any Key piscando

while game != QUIT and game != GAME:
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = QUIT
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game = GAME

    if game == TELA_FINAL and WIN == 1:
        TELA.fill(BLACK)

        TELA.blit(assets['background'], ORIGEM)

        TELA.blit(assets['TelaFinal'], ORIGEM)

        TELA.blit(assets['Player1Win'],ORIGEM)

        if lastFlick < FPS:
            TELA.blit(assets['PressSpace'], ORIGEM)
            lastFlick += 1
        elif lastFlick == FPS*2-1:
            lastFlick = 0
        else:
            lastFlick += 1

    if game == TELA_FINAL and WIN == 2:

        TELA.fill(BLACK)

        TELA.blit(assets['background'], ORIGEM)

        TELA.blit(assets['TelaFinal'], ORIGEM)

        TELA.blit(assets['Player2Win'],ORIGEM)

        if lastFlick < FPS:
            TELA.blit(assets['PressSpace'], ORIGEM)
            lastFlick += 1
        elif lastFlick == FPS*2-1:
            lastFlick = 0
        else:
            lastFlick += 1

    pygame.display.update()


pygame.quit()