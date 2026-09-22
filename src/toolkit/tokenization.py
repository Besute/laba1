from .errors import InvalidExpressionError
from .auxiliary_functions import is_oper

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
            while (get_operation_priority(queue[-1]) >= get_operation_priority(expression[i]) and expression[i] not in "!?") or (expression[i] in "!?" and get_operation_priority(queue[-1]) > get_operation_priority(expression[i])):
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

def tokenize_expression(expression):
    expr = separate_nums_from_opers(expression.replace(",", ".").replace("//", "№"))
    expr = make_expression_queue(expr)
    return expr