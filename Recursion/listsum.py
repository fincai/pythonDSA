def listsum_iterative(numlist):
    theSum = 0
    for i in numlist:
        theSum += i
    return theSum


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])

print(listsum_iterative([i for i in range(1, 101)]))
print(listsum([i for i in range(1, 101)]))

