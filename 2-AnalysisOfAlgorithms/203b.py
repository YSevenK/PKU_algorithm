"""
变位词判断问题

两个词之间的字母相同，只是排列不同，称为变位词。
"""

# 方法2：排序比较


def anagramSolution(s1, s2):
    alist1 = list(s1)
    alist2 = list(s2)

    alist1.sort()
    alist2.sort()
    pos = 0
    matches = True
    while pos < len(s1) and matches:
        if alist1[pos] == alist2[pos]:
            pos = pos + 1
        else:
            matches = False
    return matches


print(anagramSolution('abcd332', '2a33dcb'))
