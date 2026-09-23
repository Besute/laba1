from toolkit.__main__ import main
from toolkit.errors import InvalidExpressionError, DivisionByZeroError

def test_calc_success(capsys, monkeypatch):
    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        lambda expression: 4,
    )
    res = main(["calc", "+2+ 2"])

    assert res == 0
    assert "Result of your expression: 4\n"

def test_calc_unsuccess(capsys, monkeypatch):
    def fake_calculate(expression):
        raise InvalidExpressionError("Probably you have error in your expression")

    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        fake_calculate,
    )
    res = main(["calc", "+2+ 2 -"])

    assert res == 1
    assert "Probably you have error in your expression"

def test_calc_unsuccess_zero_div(capsys, monkeypatch):
    def fake_calculate(expression):
        raise DivisionByZeroError("You devised by zero")

    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        fake_calculate,
    )
    res = main(["calc", "2+2/(2-2)"])

    assert res == 1
    assert "You devised by zero"

def test_calc_success_one(capsys, monkeypatch):
    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        lambda expression: 15,
    )
    res = main(["calc", "15"])

    assert res == 0
    assert "Result of your expression: 15\n"

def test_success_validation_error(capsys, monkeypatch):
    def fake_calculate(expression):
        raise InvalidExpressionError("Your expression has unsupported symbols")

    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        fake_calculate,
    )
    res = main(["calc", "15 * 13c"])
    assert res == 1
    assert "Your expression has unsupported symbols"


def test_success_validation_error_empty(capsys, monkeypatch):
    def fake_calculate(expression):
        raise InvalidExpressionError("Your expression is empty or doesn't make any sense")

    monkeypatch.setattr(
        "toolkit.__main__.calculate",
        fake_calculate,
    )
    res = main(["calc", "*"])
    assert res == 1
    assert "Your expression is empty or doesn't make any sense"