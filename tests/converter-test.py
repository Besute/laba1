import pytest
from toolkit.errors import InvalidValueError
from toolkit.converter import convert

def test_1():
    assert convert("1000", "g", "kg") == 1.0

def test_2():
    with pytest.raises(InvalidValueError):
        convert("1000", "m", "kg")

def test_3():
    assert convert("1500", "g", "kg") == 1.5

def test_4():
    assert convert("3.5555", "kg", "g") == 3555.5

def test_5():
    with pytest.raises(InvalidValueError):
        convert(-280, "c", "f")

def test_6():
    assert convert(0, "c", "k") == 273.15

def test_7():
    assert convert(100, "cm", "m") == 1.0

def test_8():
    with pytest.raises(InvalidValueError):
        convert(-100, "cm", "m")

def test_9():
    with pytest.raises(InvalidValueError):
        convert(-50, "kg", "g")

def test_10():
    assert  convert(567, "f", "c") == 297.22222222222223

def test_11():
    assert convert(297.22222222222223, "c", "f") == 567