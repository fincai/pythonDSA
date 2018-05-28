import timeit
import random

for i in range(10000, 1000001, 10000):
    t = timeit.Timer("random.randrange(%d) in x" % (i),
                     "from __main__ import random, x")
    x = list(range(i))
    list_time = t.timeit(number=1000)
    x = {k:None for k in range(i)}
    dic_time = t.timeit(number=1000)
    print("size:%d %10.3f %10.3f" % (i, list_time, dic_time))
