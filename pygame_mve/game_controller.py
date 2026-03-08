from pygame.game_objects import GameObject, Character
import csv

class Game:
    def __init__(self):
        self.characters = []
        self.backgrounds = []
        self.dimensions = []
        self.start = ()
        self.exit = ()

    def set_up(self):
        self.set_background_from_file("background_codes.txt")
        char = Character("P",self.start)
        self.characters.append(char)

    def add_background_object(self, btype, pos):
        if btype == 'W':
            objects = GameObject(btype,pos, True)
        else:
            objects = GameObject(btype,pos, False)
        self.backgrounds.append(objects)

    def set_background_from_file(self, backgrounds):
        file = open(backgrounds, 'r')
        read = csv.reader(file)
        for row_index, row in enumerate(read):
            length = len(row)
            for col_index, col in enumerate(row):
                pos = (row_index, col_index)
                self.add_background_object(col,pos)
                if col == "S":
                    self.start = pos
                if col == "E":
                    self.exit = pos
        file.close()
        self.dimensions = (row_index+1, length)

    def check_collisions(self, pos):
        content = self.get_cell_content(pos)
        for item in content:
            if item.solid:
                return True
        return False

    def get_cell_content(self, pos):
        contents = []
        for object in self.backgrounds:
            if object.position == pos:
                contents.append(object)
        for object in self.characters:
            if object.position == pos:
                contents.append(object)
        return contents

    def move_character(self, character, direction):
        pos = character.find_next_location(direction)
        if not self.check_collisions(pos):
            character.move(direction)

    def find_objects_by_name(self, name):
        contents = []
        for object in self.backgrounds:
            if object.name == name:
                contents.append(object)
        for object in self.characters:
            if object.name == name:
                contents.append(object)
        return contents

    def show_game_grid(self):
        grid = ''
        for row in range(self.dimensions[0]):
            for column in range(self.dimensions[1]):
                content = self.get_cell_content((row, column))
                found = False
                for objects in content:
                    if objects in self.characters:
                        grid += objects.name
                        found = True
                if not found:
                    grid += str(content[0].name)
            grid += '\n'
        return grid
