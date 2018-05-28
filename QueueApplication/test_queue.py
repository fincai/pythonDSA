import sys
sys.path.append("..")
from pythonds.queue import Queue

q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print(q.size())
print(q.dequeue())
print(q.dequeue())
print(q.size())
