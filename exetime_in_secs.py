import time

def sumOfN2(n):
    start = time.time()

    theSum = 0
    for i in range(1, n+1):
        theSum =theSum + i

    end = time.time()
    return theSum, end-start

def sumOfN3(n):
    theSum = n*(n+1)/2
    

for i in range(5):
    print("Sum is %d. Required %10.7f seconds." % sumOfN2(10000))

