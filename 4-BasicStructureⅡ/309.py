"""
队列应用：
热土豆问题：
    有n个人围成一圈，从第一个人开始报数，报数到m的人出局，
    然后从下一个人开始报数，直到剩下最后一个人，求出最后一个人的编号。
"""

from pythonds.basic.queue import Queue


def hotPotato(namelist, num):
    simqueue = Queue()
    for name in namelist:
        simqueue.enqueue(name)

    while simqueue.size() > 1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()

    return simqueue.dequeue()


print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
