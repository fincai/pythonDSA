import sys
sys.path.append("..")
from pythonds.queue import Queue

def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        print(simqueue.dequeue())
    return simqueue.dequeue()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
print(hotPotato(['Cap', 'Ironman', 'Widow', 'Hulk', 'Thor'], 6))
