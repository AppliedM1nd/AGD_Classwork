import pytest
from tdd.code_shift import code

def test_cipher_function():
    assert code('abc',3) == 'def'
    assert code('TEST', 3) == 'whvw'
    assert code('123', 3) == '123'

@pytest.mark.parametrize("message, shift, expected", [
    ("def", -3, "abc"),
    ("abc", 27, "bcd"),
    ("abc", 52, "abc"),
    ("AbZ", 1, "bca"),
    ("abc", 'two', "cde"),
])
def test_negative_and_large_shifts(message, shift, expected):
    assert code(message, shift) == expected

def test_non_letters_unchanged():
    assert code("Test, 123", 2) == "vguv, 123"

def test_string_errors():
    with pytest.raises(TypeError):
        code(2, 3)

def test_shift_errors():
    with pytest.raises(TypeError):
        code("abc", "1")

