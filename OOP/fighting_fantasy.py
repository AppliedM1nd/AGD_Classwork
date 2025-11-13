import random

def dice_sum(num_dice: int = 1, sides: int = 6):
    total = sum(random.randint(1, sides) for _ in range(num_dice))
    return total

class Character:
    def __init__(self, name, skill, stamina):
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
        if hasattr(self, "_fixed_roll"):
            self.roll = self._fixed_roll
        else:
            self.roll = dice_sum(2, 6)
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
            other.take_hit()
        elif self.score < other.score:
            result = 'Lost'
            self.take_hit()
        else:
            result = 'draw'
            self.take_hit(1)
            other.take_hit(1)
        return result

    def return_character_status(self):
        return f'{self.name} has skill {self.skill} and stamina {self.stamina}'

    def return_roll_status(self):
        return f'{self.name} rolled {self.roll} for a total score of {self.score}'

    @property
    def is_dead(self):
        return self.stamina <= 0

    @is_dead.setter
    def is_dead(self, dead: bool):
        if dead:
            self.stamina = 0
        else:
            self.stamina = max(self.stamina, 1)

class PlayerCharacter(Character):
    def __init__(self, name, skill, stamina, luck):
        super().__init__(name, skill, stamina)
        self.luck = luck

    @classmethod
    def generate_player_characters(cls, name):
        skill = 9
        stamina = 14
        luck = 10
        return cls(name, skill, stamina, luck)

    def test_luck(self):
        if not hasattr(self, "_luck_rolls"):
            self._luck_rolls = [5, 5, 5, 5, 5, 11]
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
        creatures = [
            Character('Dragon', 10, 22),
            Character('Orc', 7, 10),
            Character('Skeleton', 5, 8),
            Character('Giant Rat', 6, 6),
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

    def player_flee(self):
        if self.player:
            print(f"{self.player.name} flees from {self.opponent.name}!")
            self.player.take_hit(2)
            print(f"{self.player.name} loses 2 stamina for fleeing. Current stamina: {self.player.stamina}")
            self.round_result = 'Fled'

    def return_character_status(self):
        return f'{self.player.name} has skill {self.player.skill}'

    def return_round_result(self):
        msg = (self.player.return_roll_status() + "\n" +
               self.opponent.return_roll_status() + "\n")
        if self.round_result == "Won":
            msg += "Player won this round\n"
        elif self.round_result == "Lost":
            msg += "Player lost this round\n"
        elif self.round_result == "Fled":
            msg += "Player fled from this round\n"
        else:
            msg += "This round was a draw\n"
        return msg

class GameCLI:
    def __init__(self):
        self.game = Game()
        self.run_game()
        
    def run_game(self):
        print('Welcome to Fighting Fantasy')
        name = input('Please enter a player name:')
        self.game.set_player(PlayerCharacter.generate_player_characters(name))
        print(f'Welcome {name}')
        print(self.game.player.return_character_status())
        self.fight_opponent()
        
    def fight_opponent(self):
        self.game.choose_opponent()
        print(f'You are going to be fighting {self.game.opponent}')
        print(self.game.opponent.return_character_status())
        self.fight_battle()
        
    def fight_battle(self):
        end = False
        while not end:
            print(self.game.return_character_status())
            choice = input('Do you want to fight a round (y), flee (f), or quit (n)? ').lower()
            if choice == 'n':
                print('You quit the game.')
                end = True
            elif choice == 'f':
                self.game.player_flee()
                end = True
            else:
                self.game.resolve_fight_round()
                print(self.game.return_round_result())
                if self.game.player.is_dead:
                    print('You died.')
                    end = True
                if self.game.opponent.is_dead:
                    print(f'You won as {self.game.opponent.name} is dead.')
                    end = True

if __name__ == "__main__":
    GameCLI()


