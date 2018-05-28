import time
from random import randrange

def findMin_Quadratic(alist):
    smallest = alist[0]
    for i in alist:
        ismin = True
        for j in alist:
            if j < i:
                ismin = False
                break
        if ismin == True:
            smallest = i
            break
    return smallest


def findMin(alist):
    minsofor = alist[0]
    for i in alist:
        if i < minsofar:
            minsofor = i
    return minsofor

for listSize in range(100000, 1000001, 100000):
    alist = [randrange(100000) for x in range(listSize)]
    start = time.time()
    print("min: %d" % findMin(alist))
    end = time.time()
    print("size: %d time: %f seconds" % (listSize, end-start))
