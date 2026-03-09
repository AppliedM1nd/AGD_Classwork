class GameObject:
    def __init__(self, name, position, solid):
        self.name = name
        self.position = position
        self.solid = solid

    def __str__(self):
        return f'{self.name} is at position {self.position}, solid {self.solid}'

    def is_solid(self):
        return self.solid

class Character(GameObject):
    def __init__(self, name, position):
        super().__init__(name,position,True)

    def find_next_location(self, direction):
        row,col = self.position
        if direction == 'up':
            return row-1, col
        elif direction == 'down':
            return row+1, col
        elif direction == 'left':
            return row, col-1
        elif direction == 'right':
            return row, col+1

    def move(self, direction):
        self.position = self.find_next_location(direction)
class GameObject:
    def __init__(self, name, position, solid):
        self.name = name
        self.position = position
        self.solid = solid

    def __str__(self):
        return f'{self.name} is at position {self.position}, solid {self.solid}'

    def is_solid(self):
        return self.solid

class Character(GameObject):
    def __init__(self, name, position):
        super().__init__(name,position,True)

    def find_next_location(self, direction):
        row,col = self.position
        if direction == 'up':
            return row-1, col
        elif direction == 'down':
            return row+1, col
        elif direction == 'left':
            return row, col-1
        elif direction == 'right':
            return row, col+1

    def move(self, direction):
        self.position = self.find_next_location(direction)
