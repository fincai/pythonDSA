import sys
sys.path.append("..")
from pythonds.stack import Stack

def postfixEval(expr):
    operandstack = Stack()
    token_list = expr.split()
    for token in token_list:
        if token.isnumeric():
            operandstack.push(int(token))
        else:
            op2 = operandstack.pop()
            op1 = operandstack.pop()
            result = do_math(token, op1, op2)
            operandstack.push(result)
    return operandstack.pop()

def do_math(op, op1, op2):
    if op == '+':
        return op1 + op2
    elif op == '-':
        return op1 - op2
    elif op == '*':
        return op1 * op2
    else:
        return op1 / op2

            
print(postfixEval('7 8 + 3 2 + /'))
print(postfixEval('15 3 2 + /'))
