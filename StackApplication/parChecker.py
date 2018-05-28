import sys
sys.path.append("..")
from pythonds.stack import Stack

def parchecker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()

    return s.isEmpty()


print(parchecker("(((())))"))
print(parchecker("(()"))

