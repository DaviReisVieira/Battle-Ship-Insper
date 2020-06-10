import pygame
from TelaInicial import tela_inicial
from config import HEIGHT, WIDTH, QUIT, TELA_INICIAL, GAME

# ------ inicia pygame
pygame.init()

# ------ Gera a Tela de jogo
TELA = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Battle Ship')

#===== Rotina principal o jogo:
estado = TELA_INICIAL

while estado != QUIT:
    if estado == TELA_INICIAL:
        estado = tela_inicial(TELA)
    if estado == GAME:
        estado == tela_jogo(TELA)



# ----- Finaliza o jogo
pygame.quit()
