"""
顺序查找:无序表
"""


def sequentialSearch(alish, item):
    pos = 0
    found = False
    while pos < len(alish) and not found:
        if alish[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found


testlist = [1, 2, 8, 36, 26, 78, 91, 20]

print(sequentialSearch(testlist, 26))
print(sequentialSearch(testlist, 20))
