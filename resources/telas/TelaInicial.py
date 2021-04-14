import pygame
import assets as assets_file
from config import BLACK, FPS, ORIGEM, QUIT, TELA_INICIAL, INSTRUCOES, GAME

# ----- Função para gerar a Tela Inicial e Instruções
def tela_inicial (TELA):
    clock = pygame.time.Clock()

    assets = assets_file.load_assets()

    estado = TELA_INICIAL
    last_flick = 0  # Press Any Key piscando

    while estado != QUIT and estado != GAME:
        clock.tick(FPS)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
            elif event.type == pygame.KEYDOWN and estado != INSTRUCOES:
                estado = INSTRUCOES
            elif event.type == pygame.KEYDOWN:
                estado = GAME

        def keepScreen(screen, last_flick):
            TELA.fill(BLACK)

            TELA.blit(assets['background'], ORIGEM)
            
            TELA.blit(assets[screen], ORIGEM)

            if last_flick < 30:
                TELA.blit(assets['PressKey'], ORIGEM)
                last_flick += 1
            elif last_flick == 59:
                last_flick = 0
            else:
                last_flick += 1

            pygame.display.update()

        if estado == TELA_INICIAL:
            keepScreen("Letreiro", last_flick)
        
        elif estado == INSTRUCOES:
            keepScreen("Instrucoes", last_flick)

    return estado