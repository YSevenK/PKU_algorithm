"""
递归可视化：分形树
"""

import turtle


def tree(branch_tree):
    if branch_tree > 5:
        t.forward(branch_tree)
        t.right(20)
        tree(branch_tree - 15)
        t.left(40)
        tree(branch_tree - 15)
        t.right(20)
        t.backward(branch_tree)


t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor("green")
t.pensize(2)
tree(75)
t.hideturtle()
turtle.done()
