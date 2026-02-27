
class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = []
        self.start = ()
        self.exit = ()

    def set_up(self):
        pass

    def add_background_object(self, btype, pos):
        if btype == 'W':
            GameObject(btype,pos, True)
        else:
            GameObject(btype,pos, False)

    def set_background_from_file(self, backgrounds):
        file = open('background_codes.txt', 'r')
        for line in file:
            line.strip().split()
            backgrounds.append(line)
        file.close()

    def check_collisions(self, pos):
        pass

    def get_cell_content(self, pos):
        pass

    def move_character(self, character):
        pass

    def find_objects_by_name(self, name):
        pass

    def show_game_grid(self):
        pass