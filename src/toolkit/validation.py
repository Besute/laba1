from .errors import InvalidExpressionError
from .auxiliary_functions import REAL_OPERANDS

def validation(expression):
    empty_expression = True
    correct_expression = True
    for i in "0123456789":
        if i in expression:
            empty_expression = False
            break
    for i in expression:
        if i not in REAL_OPERANDS and i not in "0123456789 .,":
            correct_expression = False
            break
    if not(correct_expression):
        raise InvalidExpressionError("Your expression has unsupported symbols")
    if empty_expression:
        raise InvalidExpressionError("Your expression is empty")
