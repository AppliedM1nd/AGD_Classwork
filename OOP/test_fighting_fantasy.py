import pytest
import random
from fighting_fantasy import Character, PlayerCharacter


class TestCharacter:
    @pytest.fixture
    def characters(self):
        random.seed(10_001)
        return [Character('orc', skill=5, stamina=12),
                Character('dragon', skill=8, stamina=15)]

    def test_characters(self, characters):
        orc, dragon = characters
        assert orc.name == 'Orc'
        assert orc.skill == 5
        assert orc.stamina == 12
        assert orc.__repr__() == "Character('Orc', skill=5, stamina=12)"
        assert str(dragon) == "Dragon"

    def test_find_score(self, characters):
        random.seed(10_001)
        orc = characters[0]
        orc.find_score()
        assert orc.roll == 4
        assert orc.score == orc.roll + orc.skill

    def test_take_hit(self, characters):
        orc = characters[0]
        orc.take_hit()
        assert orc.stamina == 10
        orc.take_hit(1)
        assert orc.stamina == 9

    def test_fight_round(self, characters):
        random.seed(10_001)
        orc, dragon = characters
        result = orc.fight_round(dragon)
        assert orc.roll == 4
        assert dragon.roll == 5
        assert dragon.score == 13
        assert result == 'Lost'
        assert orc.stamina == 10
        assert dragon.stamina == 15

    def test_is_dead(self, characters):
        orc = characters[0]
        orc.take_hit(12)
        assert orc.is_dead

    def test_set_is_dead(self, characters):
        orc = characters[0]
        orc.is_dead = False
        assert orc.stamina == 12
        orc.is_dead = True
        assert orc.stamina == 0
        orc.is_dead = False
        assert orc.stamina == 1

    def test_return_character_status(self, characters):
        orc = characters[0]
        assert orc.return_character_status() == 'Orc has skill 5 and stamina 12'

    def test_return_roll_status(self, characters):
        random.seed(10_001)
        dragon = characters[1]
        dragon.find_score()
        assert dragon.return_roll_status() == 'Dragon rolled 4 for a total score of 12'


class TestPlayerCharacter:
    @pytest.fixture
    def player_character(self):
        random.seed(10_001)
        return PlayerCharacter.generate_player_characters("Sir Tom")

    def test_generate_pc(self, player_character):
        pc = player_character
        assert pc.skill == 9
        assert pc.stamina == 14
        assert pc.luck == 10
        assert pc.__repr__() == "PlayerCharacter('Sir Tom', skill=9, stamina=14, luck=10)"

    def test_test_luck(self, player_character):
        random.seed(10_001)
        for _ in range(5):
            lucky = player_character.test_luck()
            assert lucky is True
        lucky = player_character.test_luck()
        assert lucky is False
        assert player_character.luck == 4

if __name__ == "__main__":
    pytest.main([__file__])
