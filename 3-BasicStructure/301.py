"""
使用 py 实现 ADT Stack（Abstract Data Type，抽象数据类型）
栈：后进先出 LIFO: Last In First Out
"""

# 实现栈的ADT
from pythonds.basic.stack import Stack


s = Stack()

print(s.isEmpty())

s.push(4)
s.push('dog')

# peek()方法用于查看栈顶元素
print(s.peek())

s.push(True)

print(s.size())
print(s.isEmpty())

s.push(8.4)

# 删除并返回最后一个元素，同时数组的长度也会减1
print(s.pop())
print(s.pop())
print(s.size())
