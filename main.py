import pygame
import config
from game import Game
from game_state import GameState

try:
    pygame.init()
except:
    print("Foi não, truta")

icon = pygame.image.load("images/icon.ico")
screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))

clock = pygame.time.Clock()

game = Game(screen)
game.set_up()

pygame.display.set_caption("Pokémon Clone")
pygame.display.set_icon(icon)


while game.game_state == GameState.RUNNING:
    clock.tick(50)
    game.update()
    pygame.display.update()


