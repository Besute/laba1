from calculator import calculate

def main():
    expression = input("Input expression: ")
    result = calculate(expression)
    print(result)


if __name__ == "__main__":
    main()