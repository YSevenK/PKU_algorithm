"""
递归算法：数列求和
"""


def listsum(numlist):
    if len(numlist) == 1:
        return numlist[0]
    else:
        return numlist[0] + listsum(numlist[1:])


print(listsum([1, 3, 5, 7, 9]))
