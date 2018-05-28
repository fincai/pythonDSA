import sys
sys.path.append("..")
from pythonds.deque import Deque

dq = Deque()
print(dq.isEmpty())
dq.addRear(4)
dq.addRear('dog')
dq.addFront('cat')
dq.addFront(True)
print(dq.size())
dq.addRear(8.4)
print(dq.removeRear())
print(dq.removeFront())
