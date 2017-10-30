import os, sys

def iterSquare( num ):
    number = 1
    denom = 2

    for index in range(0, num):
        yield (number + denom, denom)

        tmp = number
        number = denom
        denom = 2 * denom + tmp

def checkMore(number, denom):
    tmp = number
    numLength = 0
    while tmp != 0:
        numLength += 1
        tmp/=10

    tmp = denom
    denomLength = 0
    while tmp != 0:
        denomLength += 1
        tmp /= 10
    return numLength > denomLength


    return pointLength > denom


ans = 0
for a,b in iterSquare(1000):
    if checkMore(a, b):
        ans += 1

print ans
