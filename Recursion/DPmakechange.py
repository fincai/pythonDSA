def DPmakechange(change, coinValueList, minCoins):
    for amount in range(change+1):
        numCoins = amount
        for i in [c for c in coinValueList if c <= amount]:
            if minCoins[amount-i] + 1 < numCoins:
                numCoins = minCoins[amount-i] + 1
        minCoins[amount] = numCoins
    return minCoins[change]

print(DPmakechange(63, [1, 5, 10, 21, 25], [0]*64))

