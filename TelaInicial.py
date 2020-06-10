import pygame
import assets as assets_file
from config import BLACK, FPS, ORIGEM, QUIT, TELA_INICIAL, INSTRUCOES, GAME

# ----- Função para gerar a Tela Inicial e Instruções
def tela_inicial (TELA):
    clock = pygame.time.Clock()

    assets = assets_file.load_assets()

    game = TELA_INICIAL
    last_flick = 0  # Press Any Key piscando

    while game != QUIT and game != GAME:
        clock.tick(FPS)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game = QUIT
            elif event.type == pygame.KEYDOWN and game != INSTRUCOES:
                game = INSTRUCOES
            elif event.type == pygame.KEYDOWN:
                game = GAME

                    
        if game == TELA_INICIAL:
            TELA.fill(BLACK)

            TELA.blit(assets['background'], ORIGEM)
            
            TELA.blit(assets['Letreiro'], ORIGEM)

            if last_flick < 30:
                TELA.blit(assets['PressKey'], ORIGEM)
                last_flick += 1
            elif last_flick == 59:
                last_flick = 0
            else:
                last_flick += 1

            pygame.display.update()
        
        elif game == INSTRUCOES:
            TELA.fill(BLACK)

            TELA.blit(assets['background'], ORIGEM)
            
            TELA.blit(assets['Instrucoes'], ORIGEM)

            if last_flick < 30:
                TELA.blit(assets['PressKey'], ORIGEM)
                last_flick += 1
            elif last_flick == 59:
                last_flick = 0
            else:
                last_flick += 1

            pygame.display.update()

    return GAME