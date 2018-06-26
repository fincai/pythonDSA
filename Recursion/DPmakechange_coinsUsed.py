def DPmakechange(change, coinValueList, minCoins, lastCoinUsed):
    for amount in range(change+1):
        numCoins = amount
        for i in [c for c in coinValueList if c <= amount]:
            if minCoins[amount-i] + 1 < numCoins:
                numCoins = minCoins[amount-i] + 1
                lastCoinUsed[amount] = i
        minCoins[amount] = numCoins
    return minCoins[change]


def printCoins(change, lastCoinUsed):
    amount = change
    while amount > 0:  
        print(lastCoinUsed[amount])
        amount = amount - lastCoinUsed[amount]


def main():
    amount = 63
    cvlist = [1, 5, 10, 21, 25]
    minCoins = [0]*(amount+1)
    lastCoinUsed = [0]*(amount+1)
    print("making change for", amount, "requires")
    print(DPmakechange(amount, cvlist, minCoins, lastCoinUsed), "coins.")
    print("They are:")
    printCoins(amount, lastCoinUsed)

main()
    



