import argparse
from .calculator import calculate
from .converter import convert
import json
from pathlib import Path
from .errors import InvalidExpressionError, InvalidValueError, DivisionByZeroError

JSON_FILE = Path(__file__).parent / "calculator-config.json"

def save_data(data, path):
    with open(path, "w") as file:
        json.dump(data, file, indent=2)

def build_parser():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="This program calculates the result of a given expression or convert one measure to another"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    calc_parser = subparsers.add_parser("calc", help="calculates given expression")
    calc_parser.add_argument("value", help="expression")

    convert_parser = subparsers.add_parser("convert", help="convert one measure to another")
    convert_parser.add_argument("value", help="your initial value of 'from' unit")
    convert_parser.add_argument("--from", dest="from_unit", required=True, help="from unit")
    convert_parser.add_argument("--to", dest="to_unit", required=True, help="to unit")

    precision_parser = subparsers.add_parser("setprecision", help="set precision of the calc expression")
    precision_parser.add_argument("value", help="value of precision", type=int)

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    try:
        if args.command == "calc":
            result = calculate(args.value)
            print("Result of your expression:", result)
        elif args.command == "convert":
            result = convert(args.value, args.from_unit, args.to_unit)
            print(f"The {args.value}{args.from_unit} is {result}{args.to_unit}")
        elif args.command == "setprecision":
            print(args.value)
            save_data({
                "precision": args.value,
            }, JSON_FILE)

    except InvalidExpressionError as error:
        print(f"Error: {error}")

    except InvalidValueError as error:
        print(f"Error: {error}")

    except DivisionByZeroError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()