import decimal
from .errors import InvalidExpressionError, DivisionByZeroError, InvalidValueError
from decimal import *
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

def get_operation_priority(op):
    if op == "(":
        return 0
    elif op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/" or op == "%" or op == "№":
        return 2
    elif op == "!" or op == "?":
        return 3
    return -1

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

def separate_nums_from_opers(expression):
    final_expr = []
    i = 0
    was_operand = True
    while i < len(expression):
        if expression[i] == " ":
            i += 1
            continue
        elif (is_oper(expression[i]) and not(was_operand)) or expression[i] in "()":
            final_expr.append(expression[i])
            was_operand = True
            if expression[i] in ")":
                was_operand = False
            i += 1
        elif was_operand and is_oper(expression[i]):
            if expression[i] in "-":
                final_expr.append("!")
            elif expression[i] in "+":
                final_expr.append("?")
            else:
                raise InvalidExpressionError("You have a trouble in operands queue")
            i += 1
        else:
            curr_num = ""
            while i < len(expression) and not(is_oper(expression[i])) and expression[i] != " ":
                curr_num += expression[i]
                i += 1
            final_expr.append(curr_num)
            was_operand = False
    return final_expr

def make_expression_queue(expression):
    queue = ["("]
    final_expr = []
    for i in range(len(expression)):
        if expression[i] in "(":
            queue.append("(")
        elif is_oper(expression[i]) and expression[i] not in ")":
            while get_operation_priority(queue[-1]) >= get_operation_priority(expression[i]):
                final_expr.append(queue.pop())
            queue.append(expression[i])
        elif expression[i] in ")":
            while queue[-1] != "(":
                final_expr.append(queue.pop())
            queue.pop()
        else:
            final_expr.append(expression[i])
    if len(queue) == 0:
        raise InvalidExpressionError("You have a trouble in expression queue")
    while queue[-1] != "(":
        final_expr.append(queue.pop())
        if len(queue) == 0:
            raise InvalidExpressionError("You have a trouble in expression queue")
    queue.pop()
    if len(queue) != 0:
        raise InvalidExpressionError("You have an trouble in your expression")
    return final_expr

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
    expr = separate_nums_from_opers(expression.replace(",", ".").replace("//", "№"))
    expr = make_expression_queue(expr)
    res = execute(expr)
    return decimal.Decimal(res)