import time
from vis import *


def check(m, x, y):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):

            if i | j:

                xcord, ycord = x + i, y + j
                if xcord == -1:
                    xcord = SIZE - 1
                if xcord == SIZE:
                    xcord = 0

                if ycord == -1:
                    ycord = SIZE - 1
                if ycord == SIZE:
                    ycord = 0

                if m[xcord][ycord]:
                    count += 1

    return count


def create(x, y):
    c.create_polygon((450 + x * 10, 50 + y * 10), (460 + x * 10, 50 + y * 10), (460 + x * 10, 60 + y * 10), (450 + x * 10, 60 + y * 10), fill='red', outline='black')
    m[x][y] = 1


def destroy(x, y):
    c.create_polygon((450 + x * 10, 50 + y * 10), (460 + x * 10, 50 + y * 10), (460 + x * 10, 60 + y * 10), (450 + x * 10, 60 + y * 10), fill='white', outline='black')
    m[x][y] = 0
