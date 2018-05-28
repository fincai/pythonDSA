import sys
sys.path.append("..")
from pythonds.stack import Stack

def symbol_balance_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol in "{[(":
            s.push(symbol)
        elif symbol in "}])":
            if s.isEmpty():
                return False
            if "{[(".index(s.pop()) != "}])".index(symbol):
                return False

    return s.isEmpty()

print(symbol_balance_checker("{{([][])}()}"))

