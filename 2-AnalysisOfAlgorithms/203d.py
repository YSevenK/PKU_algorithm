"""
变位词判断问题

两个词之间的字母相同，只是排列不同，称为变位词。
"""

# 方法4：计数比较
"""
对比两个字符串的字母出现次数，如果相同，则是变位词。
妙妙妙！
"""


def anagramSolution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1
    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1
    j = 0
    stillOk = True
    while j < 26 and stillOk:
        if c1[j] == c2[j]:
            j = j+1
        else:
            stillOk = False
    return stillOk


print(anagramSolution4('abcd', 'acdb'))
