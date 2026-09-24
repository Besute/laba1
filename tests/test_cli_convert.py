from toolkit.__main__ import main
from toolkit.errors import InvalidValueError


def test_convert_success(capsys, monkeypatch):
    monkeypatch.setattr(
        "toolkit.__main__.convert",
        lambda value, from_, to_: 100,
    )

    exit_code = main(
        [
            "convert",
            "1",
            "--from",
            "m",
            "--to",
            "cm",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "The 1.0m is 100cm\n"


def test_convert_success_2(capsys, monkeypatch):
    monkeypatch.setattr(
        "toolkit.__main__.convert",
        lambda value, from_, to_: 0,
    )

    exit_code = main(
        [
            "convert",
            "273.15",
            "--from",
            "k",
            "--to",
            "c",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "The 273.15k is 0c\n"


def test_convert_unsuccess(capsys, monkeypatch):
    def fake_convert(value, from_, to_):
        raise InvalidValueError("You have temperature below absolute zero")

    monkeypatch.setattr(
        "toolkit.__main__.convert",
        fake_convert,
    )

    exit_code = main(
        [
            "convert",
            "-600",
            "--from",
            "c",
            "--to",
            "k",
        ]
    )

    assert exit_code == 1
    assert "You have temperature below absolute zero"


def test_convert_unsuccess_2(capsys, monkeypatch):
    def fake_convert(value, from_, to_):
        raise InvalidValueError(f"You can't convert {from_} to {to_}")

    monkeypatch.setattr(
        "toolkit.__main__.convert",
        fake_convert,
    )

    exit_code = main(
        [
            "convert",
            "-600",
            "--from",
            "c",
            "--to",
            "k",
        ]
    )

    assert exit_code == 1
    assert "You have temperature below absolute zero"


def test_convert_success_3(capsys, monkeypatch):
    monkeypatch.setattr(
        "toolkit.__main__.convert",
        lambda value, from_, to_: 5555.5,
    )

    exit_code = main(
        [
            "convert",
            "5.5555",
            "--from",
            "kg",
            "--to",
            "g",
        ]
    )

    captured = capsys.readouterr()

    assert exit_code == 0
    assert captured.out == "The 5.5555kg is 5555.5g\n"
