import pytest
from tdd.grade_boundaries import calc_grade

test_data_max = [(49,'U'),
             (149,'E'),
             (249,'D'),
             (299,'C'),
             (399,'B'),
             (449,'A'),
             (500,'A*'),
             ]

test_data_min = [(0,'U'),
             (50,'E'),
             (150,'D'),
             (250,'C'),
             (300,'B'),
             (400,'A'),
             (450,'A*'),
             ]

def test_calc_grade():
    assert calc_grade(475)=='A*'
    assert calc_grade(310)=='B'


@pytest.mark.parametrize('score, grade', test_data_max)
def test_calc_grade_min_boundary(score, grade):
    assert calc_grade(score) == grade
    # assert False

@pytest.mark.parametrize('score, grade', test_data_min)
def test_calc_grade_max_boundary(score, grade):
    assert calc_grade(score) == grade
    # assert False

def test_calc_grade_invalid():
    with pytest.raises(ValueError):
        calc_grade(-1)
    with pytest.raises(ValueError):
        calc_grade(501)
    with pytest.raises(TypeError):
        calc_grade('A')