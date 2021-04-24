import pygame
import config
from player import Player
from game_state import GameState


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.objects = []
        self.game_state = GameState.NONE
        self.map = []

    def set_up(self):
        player = Player(1, 1)
        self.player = player
        self.objects.append(player)
        print("do setup")
        self.game_state = GameState.RUNNING

        self.load_map("01")

    def update(self):

        self.screen.fill(config.BLACK)
        print("update")
        self.handle_events()

        self.render_map(self.screen)

        for object in self.objects:
            object.render(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_state = GameState.ENDED
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.game_state = GameState.ENDED
                elif event.key == pygame.K_w:  # up
                    self.move_unit(self.player, [0, -1])
                elif event.key == pygame.K_s:  # down
                    self.move_unit(self.player, [0, 1])
                elif event.key == pygame.K_d:  # right
                    self.move_unit(self.player, [1, 0])
                elif event.key == pygame.K_a:  # left
                    self.move_unit(self.player, [-1, 0])

    def load_map(self, file_name):
        with open("maps/" + file_name + ".txt") as map_file:
            for line in map_file:
                tiles = []
                for i in range(0, len(line) - 1, 2):
                    tiles.append(line[i])
                self.map.append(tiles)
            print(self.map)

    def render_map(self, screen):
        y_pos = 0
        for line in self.map:
            x_pos = 0
            for tile in line:
                image = map_tile_image[tile]
                rect = pygame.Rect(
                   x_pos * config.SCALE, y_pos * config.SCALE, config.SCALE, config.SCALE)
                screen.blit(image, rect)
                x_pos = x_pos + 1

            y_pos = y_pos + 1

    def move_unit(self, unit, position_change):
        new_position = unit.position [0] + position_change[0], unit.position[1] + position_change[1]

        if new_position[0] < 0 or new_position[0] > (len(self.map[0]) - 1):
            return

        if new_position[1] < 0 or new_position[1] > (len(self.map) - 1):
            return

        if self.map[new_position[1]] [new_position[0]] == "W":
            return


        unit.update_position(new_position)

map_tile_image = {
    "G": pygame.transform.scale(pygame.image.load("images/grass.png"), (config.SCALE, config.SCALE)),
    "W": pygame.transform.scale(pygame.image.load("images/water.png"), (config.SCALE, config.SCALE)),
    "S": pygame.transform.scale(pygame.image.load("images/sand.png"), (config.SCALE, config.SCALE))
}
