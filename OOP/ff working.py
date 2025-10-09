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
        pass

