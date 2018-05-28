from timeit import Timer
#concat 
def test1():
    l = []
    for i in range(1000):
        l = l + [i]

#append
def test2():
    l = []
    for i in range(1000):
        l.append(i)
# comprehension
def test3():
    l = [i for i in range(1000)]

# list(range()) 
def test4():
    l = list(range(1000))

t1 = Timer("test1()", "from __main__ import test1")
print("concat: ", t1.timeit(number=1000), " seconds")
t2 = Timer("test2()", "from __main__ import test2")
print("append: ", t2.timeit(number=1000), " seconds")
t3 = Timer("test3()", "from __main__ import test3")
print("comprehension: ", t3.timeit(number=1000), " seconds")
t4 = Timer("test4()", "from __main__ import test4")
print("list range: ", t4.timeit(number=1000), " seconds")

popzero = Timer("x.pop(0)", "from __main__ import x")
popend = Timer("x.pop()", "from __main__ import x")
print("%15s    %15s" % ('pop(0)','pop()'))
for i in range(1000000, 100000001, 1000000):
    x = list(range(i))
    popend_t = popend.timeit(number=1000)
    x = list(range(i))
    popzero_t = popzero.timeit(number=1000)
    print("%15.5f   %15.5f" % (popzero_t, popend_t))
    


    



















