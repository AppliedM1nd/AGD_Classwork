import random

def dice_sum(num_dice: int=1,sides: int=6):
    """ returns the sum of num_dice dice each with sides sides"""
    total = sum(random.randint(1, sides) for _ in range(num_dice))
    return total


class Character:
    def __init__(self,name,skill,stamina):
        self.name = name
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None



    def __repr__(self):
        return f"Character('{self.name}', Skill={self.skill}, Stamina={self.stamina})"

    def find_score(self,roll,score):
        self.roll = dice_sum(2,6)
        self.score = self.roll + self.skill
        return self.score

    def take_hit(self, damage=2):
        self.stamina -= damage
        return self.stamina

    def fight_round(self, other):
        self.find_score()
        other.find_score()
        if self.score > other.score:
            result = 'Won'
            other.take_hit(1)
            return result
        elif self.score < other.score:
            result = 'Lost'
            self.take_hit(2)
            return result

    def return_character_status(self):
        return f'{self.name} has skill {self.skill} and {self.stamina} stamina'

    @property
    def is_dead(self):
        return self.stamina <= 0
    @is_dead.setter
    def is_dead(self,dead:bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina,1)

    class PlayerCharacter(Character):
        def __init__(self,skill,stamina, luck):
            super().__init__(skill = 8, stamina = 10)
            self.luck = luck

        @classmethod
        def generate_player_characters(cls,name):
            luck = find_score(2,6)
            stamina = random.randint(1,6)
            return cls(name,skill,stamina,luck)

orc = Character('Orc',15,15)
dragon = Character('Dragon',10,20)


