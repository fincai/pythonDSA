count = 0
def recursiveMC(coinValueList, change, knownResults):
    global count
    count += 1
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    if knownResults[change] > 0:
        return knownResults[change]
    numCoins = 0
    for i in [c for c in coinValueList if c < change]:
        numCoins = 1 + recursiveMC(coinValueList, change-i, knownResults)
        if numCoins < minCoins:
            minCoins = numCoins
            knownResults[change] = minCoins
    return minCoins

print(recursiveMC([1,5,10,25], 13, [0]*14))
print("%d recursive calls" % count)
