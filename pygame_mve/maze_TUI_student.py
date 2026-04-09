from pygame.game_controller import Game


class TextInterface:
    def __init__(self):
        self.game = Game()
        self.game.set_up()
        self.player = self.game.characters[0]
        self.game_area = []
        self.running = True

    def _create_area(self):
        self.game_area = []
        for r in range(self.game.dimensions[0]):
            curr_row = []
            for c in range(self.game.dimensions[1]):
                present = self.game.get_cell_content((r, c))
                if len(present) > 0:
                    character = False
                    for item in present:
                        if item in self.game.characters and not character:
                            curr_row.append(item.name)
                            character = True
                    if not character:
                        curr_row.append(present[0].name)
                else:
                    curr_row.append('.')
            self.game_area.append(curr_row)


    def _draw_area(self):
        self._create_area()
        print('\u250C' + '─' * len(self.game_area[0]) + '\u2510')

        for row in self.game_area:
            output = '|'
            for item in row:
                if item == 'W':
                    output += '\u2593'
                else:
                    output += item
            output += '|'
            print(output)
        print('\u2514' + '─' * len(self.game_area[0]) + '\u2518')


    def _handle_input(self):
        direction = input()
        if direction == 'Q':
            self.running = False
        if self.running:
            if direction in ('up', 'down', 'left', 'right'):
                self.game.move_character(self.player, direction)
            else:
                print('Invalid input')

    def main_loop(self):
        print("Welcome to The Maze Game")
        while self.running:
            self._draw_area()
            self._handle_input()


if __name__ == "__main__":
    tui = TextInterface()
    tui.main_loop()

