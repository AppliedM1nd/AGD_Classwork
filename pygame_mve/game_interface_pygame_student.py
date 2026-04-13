import pygame
from pygame_mve.game_controller import Game

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

SQUARE_SIZE = 50

BACKGROUND_COLORS = {'Wall': 'gray30',
                     'Start': 'gold',
                     'Exit': 'dodgerblue',
                     'Floor': 'white'
                     }
PLAYER_COLOR = 'firebrick'

class GameGUI:
    key_moves = {K_UP: 'up',
                 K_DOWN: 'down',
                 K_RIGHT: 'right',
                 K_LEFT: 'left',
                 }

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Pygame MVC')

        # Set clock so that FPS can be limited
        self.clock = pygame.time.Clock()

        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.move_direction: str | None = None

        self.screen = pygame.display.set_mode([self.game.dimensions[1] * SQUARE_SIZE,
                                                    self.game.dimensions[0] * SQUARE_SIZE])
        self.running = True

    @staticmethod
    def _convert_position(pos, center: bool = False) -> tuple[int, int]:
        if center:
            y = pos[0] * (SQUARE_SIZE) + SQUARE_SIZE / 2
            x = pos[1] * (SQUARE_SIZE) + SQUARE_SIZE / 2
        else:
            y = pos[0] * (SQUARE_SIZE)
            x = pos[1] * (SQUARE_SIZE)
        return (x,y)

    def main_loop(self):
        while self.running:
            self._handle_input()
            self._process_game_logic()
            self._draw()
            self.clock.tick(60)
        pygame.quit()

    def _handle_input(self):
        for event in pygame.event.get():
            if (event.type == QUIT or
                    event.type == KEYDOWN and event.key == K_ESCAPE):
                self.running = False
            elif event.type == KEYDOWN:
                if event.key in self.key_moves:
                    self.move_direction = self.key_moves[event.key]
                else:
                    self.move_direction = None
            else:
                self.move_direction = None

    def _process_game_logic(self):
        self._handle_input()
        if self.move_direction:
            self.game.move_character(self.player, self.move_direction)
        if self.player.position == self.game.exit:
            self.running = False

    def _draw(self):
        pygame.display.flip()
        self._draw_background()
        self._draw_characters()

    def _draw_background(self):
        self.screen.fill(BACKGROUND_COLORS['Floor'])
        for bg in self.game.backgrounds:
            grid_x, grid_y = self._convert_position(bg.position,False)
            if bg.name == 'W':
                color = BACKGROUND_COLORS['Wall']
            elif bg.name == 'S':
                color = BACKGROUND_COLORS['Start']
            elif bg.name == 'E':
                color = BACKGROUND_COLORS['Exit']
            else:
                color = BACKGROUND_COLORS['Floor']
            pygame.draw.rect(self.screen, color, (grid_x, grid_y, SQUARE_SIZE, SQUARE_SIZE))

    def _draw_characters(self):
        for character in self.game.characters:
            grid_x, grid_y = self._convert_position(character.position,True)
            pygame.draw.circle(self.screen, PLAYER_COLOR, (grid_x, grid_y), SQUARE_SIZE//2)

if __name__ == "__main__":
    game = GameGUI()
    game.main_loop()
