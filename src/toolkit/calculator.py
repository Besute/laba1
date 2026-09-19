OPERANDS = "+-*/()!?"
HAHAHA_CONST = 998244353

# "!" - IS UNAR MINUS (-5), "?" - IS UNAR PLUS (+5)

def get_operation_priority(op):
    if op == "!" or op == "?":
        return 0
    elif op == "+" or op == "-" or op == "!" or op == "?":
        return 1
    elif op == "*" or op == "/":
        return 2
    elif op == "(":
        return 3
    return -1

def make_operation(first, second, op):
    if op == "*":
        return first * second
    elif op == "/":
        return first / second
    elif op == "-":
        return first - second
    elif op == "+":
        return first + second
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
            i += 1
        elif was_operand and is_oper(expression[i]):
            if expression[i] in "-":
                final_expr.append("!")
            elif expression[i] in "+":
                final_expr.append("?")
            else:
                #TODO: Make error raise from errors.py file
                raise SyntaxError("YOU HAVE ERROR IN OPERANDS QUEUE")
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
            while get_operation_priority(queue[-1]) <= get_operation_priority(expression[i]):
                final_expr.append(queue.pop())
            queue.append(expression[i])
        elif expression[i] in ")":
            while queue[-1] != "(":
                final_expr.append(queue.pop())
            queue.pop()
        else:
            final_expr.append(expression[i])
    while queue[-1] != "(":
        final_expr.append(queue.pop())
    queue.pop()
    return final_expr

def execute(expr):
    stack = []
    for i in range(len(expr)):
        if expr[i] in "?!":
            op = expr[i]
            first = stack.pop()
            res = str(make_unar(float(first), op))
            stack.append(res)
        elif is_oper(expr[i]):
            second = stack.pop()
            first = stack.pop()
            res = make_operation(float(first), float(second), expr[i])
            stack.append(str(res))
        else:
            stack.append(expr[i])
    return stack[0]


def calculate(expression):
    expr = separate_nums_from_opers(expression)
    expr = make_expression_queue(expr)
    res = execute(expr)
    return res