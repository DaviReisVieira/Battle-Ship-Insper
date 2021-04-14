import pygame
import assets as assets_file
from config import BLACK, FPS, ORIGEM, QUIT, GAME, TELA_FINAL

# ----- Função para gerar a Tela Inicial e Instruções
def tela_final (TELA,vitoria):
    clock = pygame.time.Clock()

    assets = assets_file.load_assets()

    estado = TELA_FINAL
    last_flick = 0  # Press Any Key piscando

    while estado != QUIT and estado != GAME:
        clock.tick(FPS)
      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                estado = QUIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                estado = GAME

        def keepScreenFinal(screen, last_flick):
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

        if estado == TELA_FINAL and vitoria == 1:
            keepScreenFinal("Player1Win", last_flick)

        if estado == TELA_FINAL and vitoria == 2:
            keepScreenFinal("Player2Win", last_flick)

    return estado
