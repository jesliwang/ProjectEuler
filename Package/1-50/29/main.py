import os, sys


def forceDistinct(a, b):
    li = []
    for row in range(2, a+1):
        for col in range(2, b+1):
            li.append(pow(row, col))
    li.sort()
    result = 0
    for index in range(0, len(li)):
        if index + 1 < len(li):
            #print li[index]
            if li[index] != li[index + 1]:

                result += 1
        else:
            #print li[index]
            result += 1

    return result

print forceDistinct(8, 8)
print forceDistinct(100, 100)
