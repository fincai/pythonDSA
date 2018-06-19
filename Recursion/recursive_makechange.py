# optimal number of coins to make change
def recursiveMC(coinValueList, change):
    if change in coinValueList:
        return 1
    minCoins = change
    for i in [c for c in coinValueList if c < change]:
        numCoins = 1 + recursiveMC(coinValueList, change-i)
        if numCoins < minCoins:
            minCoins = numCoins
    return minCoins

print(recursiveMC([1, 5, 10, 25], 63))
        

