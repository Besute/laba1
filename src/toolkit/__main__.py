import argparse
from .calculator import calculate

def main():
    parser = argparse.ArgumentParser(
        prog="toolkit",
        description="This program calculates the result of a given expression or convert one measure to another"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    calc_parser = subparsers.add_parser("calc", help="calculate expression")
    calc_parser.add_argument("value", type=str, help="expression")

    convert_parser = subparsers.add_parser("convert", help="convert one measure to another")
    convert_parser.add_argument("value", type=str, help="expression")
    convert_parser.add_argument("--from", type=str, dest="from_unit", required=True)
    convert_parser.add_argument("--to", type=str, dest="to_unit", required=True)

    args = parser.parse_args()
    result = ""
    if args.command == "calc":
        result = calculate(args.value)
    elif args.command == "convert":
        print(args.value, args.from_unit, args.to_unit)
    print("Result of your expression:", result)


if __name__ == "__main__":
    main()