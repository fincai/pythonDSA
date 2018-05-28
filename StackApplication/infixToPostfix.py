import sys
sys.path.append("..")
from pythonds.stack import Stack

def infix2postfix(infixexpr):
    prec = {}
    prec['('] = 0
    prec['+'] = prec['-'] = 1
    prec['*'] = prec['/'] = 2
    opstack = Stack()
    postfix_list = []
    for token in infixexpr:
        if token.isalnum():
            postfix_list.append(token)
        elif token == '(':
            opstack.push('(')
        elif token == ')':
            topToken = opstack.pop()
            while topToken != '(':
                postfix_list.append(topToken)
                topToken = opstack.pop()
        else:  # is operator
            while (not opstack.isEmpty()) and \
                    (prec[token] <= prec[opstack.peek()]):
                postfix_list.append(opstack.pop())
            opstack.push(token)

    while not opstack.isEmpty():
        postfix_list.append(opstack.pop())
    return " ".join(postfix_list)

print(infix2postfix("C-(A+B)"))
print(infix2postfix("(A+B*C)-D"))
print(sys.path)
