import pytest
from toolkit.errors import InvalidExpressionError, DivisionByZeroError
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
    with pytest.raises(InvalidExpressionError):
        calculate("2 +")

def test_10():
    with pytest.raises(DivisionByZeroError):
        calculate("5 * 11 - (2 + 3) / (5 - 5) * (101 -- 110111)")

def test_11():
    with pytest.raises(InvalidExpressionError):
        calculate("(5) - (5) *")

def test_12():
    with pytest.raises(InvalidExpressionError):
        calculate("((5 - 4)")

def test_13():
    with pytest.raises(InvalidExpressionError):
        calculate("(5 - 4))")

def test_14():
    assert calculate("2 + 2 * 2 / 2") == 4.0

def test_15():
    assert calculate("2 / 2 * 2 + 2 - 2") == 2.0

def test_16():
    assert calculate("2 / (2 + 2)") == 1/2

def test_17():
    assert calculate("2+ 2 -4") == 0

def test_18():
    assert calculate("+2+ (+2 + +2)") == 6.0

def test_19():
    assert calculate("-2-2-2-2") == -8.0

def test_20():
    assert calculate("0.5 + 1.5 * 0.5 / 0.5") == 2.0

def test_21():
    assert calculate("3/7") == 3/7

def test_22():
    assert calculate("3/7 + 5/7") == 8/7

def test_23():
    assert calculate("0,5 - 0.5") == 0

def test_24():
    assert calculate("+0 - -0") == 0

def test_25():
    assert calculate("5.676767 - 0 + 0 --0+(-0)*0") == 5.676767

def test_26():
    with pytest.raises(DivisionByZeroError):
        calculate("(5 + 0 - 5 ++4 -5.5 -3 +3.656456465 - 6/7*9*0/12 + 13/5*0) + 14/0")