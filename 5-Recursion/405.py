"""
递归应用：谢尔宾斯基三角形
"""

import turtle


def sierpinski_triangle(size, depth):
    if depth == 0:
        turtle.begin_fill()
        for _ in range(3):
            turtle.forward(size)
            turtle.left(120)
        turtle.end_fill()
    else:
        colors = ['blue', 'red', 'green', 'white', 'yellow', 'orange']
        color = colors[depth % len(colors)]
        turtle.color(color)
        sierpinski_triangle(size / 2, depth - 1)
        turtle.forward(size / 2)
        sierpinski_triangle(size / 2, depth - 1)
        turtle.backward(size / 2)
        turtle.left(120)
        turtle.forward(size / 2)
        turtle.right(120)
        sierpinski_triangle(size / 2, depth - 1)
        turtle.left(120)
        turtle.backward(size / 2)
        turtle.right(120)


if __name__ == "__main__":
    turtle.speed(0)
    sierpinski_triangle(400, 5)
    turtle.done()
