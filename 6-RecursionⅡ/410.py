"""
找零兑换问题：递归
"""


def recMC(coinValueList, change, knowResults):
    minCoins = change
    if change in coinValueList:
        knowResults[change] = 1  # 改进 1
        return 1
    elif knowResults[change] > 0:  # 改进 2
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knowResults[change] = minCoins  # 改进 3
    return minCoins


print(recMC([1, 5, 10, 25], 63, [0]*64))
