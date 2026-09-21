import decimal
from .errors import InvalidExpressionError, DivisionByZeroError, InvalidValueError
from decimal import *
from .validation import validation
from .tokenization import tokenize_expression
import json
from pathlib import Path

JSON_FILE = Path(__file__).parent / "calculator-config.json"

def load_json():
    with open(JSON_FILE, "r") as file:
        return json.load(file)

CALC_CONFIG = load_json()
PRECISION = CALC_CONFIG["precision"]

OPERANDS = "+-*/()!?№%"
HAHAHA_CONST = 998244353

# "!" - IS UNAR MINUS (-5), "?" - IS UNAR PLUS (+5)

def is_int(num):
    return int(num) == num

def make_operation(first, second, op):
    if op == "*":
        return first * second
    elif op == "/":
        if second == 0:
            raise DivisionByZeroError("You devised by zero")
        return first / second
    elif op == "-":
        return first - second
    elif op == "+":
        return first + second
    elif op == "%":
        if second == 0:
            raise DivisionByZeroError("You devised by zero")
        return abs(first) % abs(second)
    elif op == "№":
        if second == 0:
            raise DivisionByZeroError("You devised by zero")
        if is_int(first) and is_int(second):
            minus = 1
            if first < 0:
                minus = minus * -1
            if second < 0:
                minus = minus * -1
            return abs(first) // abs(second) * minus
        else:
            raise InvalidValueError("You can't divide evenly float number ")
    return HAHAHA_CONST

def make_unar(first, op):
    if op == "!":
        return -1 * first
    if op == "?":
        return first
    return HAHAHA_CONST

def is_oper(symb):
    return symb in OPERANDS

def execute(expr):
    stack = []
    for i in range(len(expr)):
        if expr[i] in "?!":
            op = expr[i]
            first = stack.pop()
            res = str(make_unar(decimal.Decimal(first), op))
            stack.append(res)
        elif is_oper(expr[i]):
            if len(stack) < 2:
                raise InvalidExpressionError("Probably you have error in your expression")
            second = stack.pop()
            first = stack.pop()
            res = make_operation(decimal.Decimal(first), decimal.Decimal(second), expr[i])
            stack.append(str(res))
        else:
            stack.append(expr[i])
    return stack[0]

def calculate(expression):
    getcontext().prec = PRECISION
    validation(expression)
    expr = tokenize_expression(expression)
    res = execute(expr)
    return decimal.Decimal(res)