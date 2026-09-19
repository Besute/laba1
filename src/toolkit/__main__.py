import argparse
from calculator import calculate

def main():
    # parser = argparse.ArgumentParser(
    #     prog="toolkit",
    #     description="This program calculates the result of a given expression or convert one measure to another"
    # )
    # subparsers = parser.add_subparsers(dest="command", required=True)
    #
    # calc_parser = subparsers.add_parser("calc", help="calculate expression")
    # calc_parser.add_argument("value", type=str, help="expression")
    #
    # args = parser.parse_args()
    # result = ""
    # if args.command == "calc":
    #     result = calculate(args.value)
    result = calculate(input())
    print(result)


if __name__ == "__main__":
    main()