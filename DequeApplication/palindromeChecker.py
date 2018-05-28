import sys
sys.path.append("..")
from pythonds.deque import Deque

def palindrome_checker(aString):
    dq = Deque()
    for ch in aString:
        dq.addFront(ch)
    while dq.size() > 1:
        if dq.removeFront() != dq.removeRear():
            return False
    return True

print(palindrome_checker("loop"))
print(palindrome_checker("radar"))

