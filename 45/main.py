import os, sys

Tri = 2
Pen = 2
Hex = 2

def Triangle(num):
    return num * (num + 1) / 2

def Pentagonal(num):
    return num * (3 * num - 1) / 2

def Hexagonal(num):
    return num * (2 * num - 1)

start = 2
number = 0

while 1:
    while Triangle(Tri) < start:
        Tri += 1

    while Pentagonal(Pen) < start:
        Pen += 1

    while Hexagonal(Hex) < start:
        Hex += 1

    if Triangle(Tri) == Pentagonal(Pen) and Hexagonal(Hex) == Pentagonal(Pen):
        print Triangle(Tri)
        number += 1

        start += 1
    else:
        start += 1
        start = max(start, Hexagonal(Hex))
        start = max(start, Triangle(Tri))
        start = max(start, Pentagonal(Pen))

    if number > 1:
        break
