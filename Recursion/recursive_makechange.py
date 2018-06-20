# optimal number of coins to make change
count = 0 
def recursiveMC(coinValueList, change):
    global count
    count += 1
    if change in coinValueList:
        return 1
    minCoins = change
    for i in [c for c in coinValueList if c < change]:
        numCoins = 1 + recursiveMC(coinValueList, change-i)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins

print(recursiveMC([1, 5, 10, 25], 63))
print("%d recursive calls." % count)
        

