import pytest
from toolkit.errors import InvalidExpressionError, DivisionByZeroError, InvalidValueError
from toolkit.calculator import calculate
from decimal import *

def test_1():
    assert calculate("-2 -3") == Decimal("-5.0")

def test_2():
    assert calculate("-2-10") == Decimal("-12.0")

def test_3():
    assert calculate("-2-(10)") == Decimal("-12.0")

def test_4():
    assert calculate("-(+10)") == Decimal("-10.0")

def test_5():
    assert calculate("(5) - (-5) * 10") == Decimal("55.0")

def test_6():
    assert calculate("-(+(-2)) +                     (-(-2)) *               2") == Decimal("6.0")

def test_7():
    assert calculate("(+(2)) +(+(+(-(-4))))") == Decimal("6.0")

def test_8():
    assert calculate("5 / 2 * 2") == Decimal("5.0")

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
    assert calculate("2 + 2 * 2 / 2") == Decimal("4.0")

def test_15():
    assert calculate("2 / 2 * 2 + 2 - 2") == Decimal("2.0")

def test_16():
    assert calculate("2 / (2 + 2)") == Decimal("0.5")

def test_17():
    assert calculate("2+ 2 -4") == Decimal("0")

def test_18():
    assert calculate("+2+ (+2 + +2)") == Decimal("6.0")

def test_19():
    assert calculate("-2-2-2-2") == Decimal("-8.0")

def test_20():
    assert calculate("0.5 + 1.5 * 0.5 / 0.5") == Decimal("2.0")

def test_21():
    assert calculate("3/7") == Decimal("3") / Decimal("7")

def test_22():
    assert calculate("3/7 + 5/7") == Decimal(8) / Decimal(7)

def test_23():
    assert calculate("0,5 - 0.5") == Decimal("0")

def test_24():
    assert calculate("+0 - -0") == Decimal("0")

def test_25():
    assert calculate("5.676767 - 0 + 0 --0+(-0)*0") == Decimal("5.676767")

def test_26():
    with pytest.raises(DivisionByZeroError):
        calculate("(5 + 0 - 5 ++4 -5.5 -3 +3.656456465 - 6/7*9*0/12 + 13/5*0) + 14/0")

def test_27():
    assert calculate("3 // 2") == Decimal("1")

def test_28():
    assert calculate("5 % 3") == Decimal("2")

def test_29():
    assert calculate("5 % 3 // 3") == Decimal("0")

def test_30():
    assert calculate("5 % (3 // 2)") == Decimal("0")

def test_31():
    with pytest.raises(DivisionByZeroError):
        calculate("51111 % (133 * 0)")

def test_32():
    with pytest.raises(InvalidValueError):
        calculate("5 / 7 // 3")

def test_33():
    assert calculate("5 / (7 // 3)") == Decimal("5") / Decimal("2")

def test_34():
    assert calculate("((((5 / (7 // 3)))))") == Decimal("5") / Decimal("2")

def test_35():
    assert calculate("5 % 3 % 2") == Decimal("0")

def test_36():
    assert calculate("1----5") == Decimal("6")

def test_37():
    with pytest.raises(InvalidExpressionError):
        calculate("($#")

def test_38():
    with pytest.raises(InvalidExpressionError):
        calculate("12 + 7b")

def test_39():
    with pytest.raises(InvalidExpressionError):
        calculate("++++---")

def test_40():
    with pytest.raises(InvalidExpressionError):
        calculate("(())")

def test_41():
    with pytest.raises(InvalidExpressionError):
        calculate("5 ** 4")

def test_42():
    assert calculate("123 / 7") == Decimal("123") / Decimal("7")