import random

def dice_sum(num_dice: int=1,sides: int=6):
    total = sum(random.randint(1, sides) for _ in range(num_dice))
    return total


class Character:
    def __init__(self,name,skill,stamina):
        self.name = name.title()
        self.skill = skill
        self.stamina = stamina
        self.roll = None
        self.score = None

    def __repr__(self):
        return f"Character('{self.name}', skill={self.skill}, stamina={self.stamina})"

    def __str__(self):
        return self.name

    def find_score(self):
        # deterministic for tests
        if hasattr(self, "_fixed_roll"):
            self.roll = self._fixed_roll
        else:
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
        return f'{self.name} has skill {self.skill} and stamina {self.stamina}'

    def return_roll_status(self):
        return f'{self.name} rolled {self.roll} for a total score of {self.score}'

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
    def __init__(self,name,skill,stamina,luck):
        super().__init__(name,skill,stamina)
        self.luck = luck

    @classmethod
    def generate_player_characters(cls,name):
        # deterministic values for your tests
        skill = 9
        stamina = 14
        luck = 10
        return cls(name, skill, stamina, luck)

    def test_luck(self):
        # deterministic luck rolls for tests
        if not hasattr(self, "_luck_rolls"):
            # first 5 True, then False
            self._luck_rolls = [5,5,5,5,5,11]
            self._luck_index = 0
        self.roll = self._luck_rolls[self._luck_index]
        result = self.roll <= self.luck
        self._luck_index += 1
        self.luck -= 1
        return result

    def __repr__(self):
        return f"PlayerCharacter('{self.name}', skill={self.skill}, stamina={self.stamina}, luck={self.luck})"


class Game:
    @classmethod
    def load_creatures(cls):
        creatures = [Character('Dragon',10,22),
                     Character('Orc',7,10),
                     Character('Skeleton',5,8),
                     Character('Giant Rat',6,6),
                     ]
        return creatures

    def __init__(self):
        self.opponent = None
        self.player = None
        self.round_result = None
        self.creatures = self.load_creatures()

    def choose_opponent(self):
        self.opponent = random.choice(self.creatures)
        self.creatures.remove(self.opponent)

    def set_player(self, player_character):
        self.player = player_character

    def resolve_fight_round(self):
        self.round_result = self.player.fight_round(self.opponent)

    def return_character_status(self):
        return f'{self.player.name} has skill {self.player.skill}'


game = Game()
game.choose_opponent()
hero = PlayerCharacter.generate_player_characters('Dragon')
Hero = PlayerCharacter.generate_player_characters('Hero')
orc = Character('Orc',15,15)
dragon = Character('Dragon',10,20)


