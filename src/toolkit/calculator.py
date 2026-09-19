OPERANDS = "+-*/()"

def get_operation_priority(op):
    if op == "+" or op == "-":
        return 1
    elif op == "*" or op == "/":
        return 2
    elif op == "(":
        return 3
    return None

def make_operation(first, second, op):
    if op == "*":
        return first * second
    elif op == "/":
        return first / second
    elif op == "-":
        return first - second
    elif op == "+":
        return first + second
    return None

def is_oper(symb):
    return symb in OPERANDS

def separate_nums_from_opers(expression):
    final_expr = []
    i = 0
    was_operand = False
    while i < len(expression):
        if expression[i] == " ":
            i += 1
            continue
        elif (is_oper(expression[i]) and not(was_operand)) or expression[i] in "()":
            final_expr.append(expression[i])
            was_operand = True
            i += 1
        elif was_operand and is_oper(expression[i]):
            curr_num = ""
            if expression[i] in "+-":
                curr_num = expression[i]
            else:
                #TODO: Make error raise from errors.py file
                raise SyntaxError("YOU HAVE ERROR IN OPERANDS QUEUE")
            i += 1
            while i < len(expression) and not (is_oper(expression[i])):
                if expression[i] == " ":
                    i += 1
                    continue
                curr_num += expression[i]
                i += 1
            was_operand = False
            final_expr.append(curr_num)
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
        if expression[i] == "(":
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
        if is_oper(expr[i]):
            second = stack.pop()
            first = stack.pop()
            res = make_operation(int(first), int(second), expr[i])
            stack.append(res)
        else:
            stack.append(expr[i])
    print(f"STACK IS: {stack}")
    return stack[0]


def calculate(expression):
    expr = separate_nums_from_opers(expression)
    print(expr)
    expr = make_expression_queue(expr)
    print(expr)
    res = execute(expr)
    return res