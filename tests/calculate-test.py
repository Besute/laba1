import pytest
from toolkit.calculator import calculate

def test_1():
    assert calculate("-2 -3") == -5.0

def test_2():
    assert calculate("-2-10") == -12.0

def test_3():
    assert calculate("-2-(10)") == -12.0

def test_4():
    assert calculate("-(+10)") == -10.0

def test_5():
    assert calculate("(5) - (-5) * 10") == 55.0

def test_6():
    assert calculate("-(+(-2)) +                     (-(-2)) *               2") == 6.0

def test_7():
    assert calculate("(+(2)) +(+(+(-(-4))))") == 6.0

def test_8():
    assert calculate("5 / 2 * 2") == 5.0

def test_9():
    with pytest.raises(SyntaxError):
        calculate("2 +")

def test_10():
    with pytest.raises(ZeroDivisionError):
        calculate("5 * 11 - (2 + 3) / (5 - 5) * (101 -- 110111)")