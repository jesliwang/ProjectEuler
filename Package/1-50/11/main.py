
import os, sys

def Left(data, row, col):

    result = 1
    if col >= 3 and col < len(data[row]):
        for index in range(0, 4):
            result *= int(data[row][col-index].strip())
    else:
        result = 0
    return result

def Up(data, row, col):
    result = 1
    if row >= 3 and row < len(data):
        for index in range(0, 4):
            result *= int(data[row-index][col].strip())
    else:
        result = 0
    return result

def LeftUp(data, row, col):
    result = 1
    if row >= 3 and row < len(data) and col >= 3 and col < len(data[row]):
        for index in range(0, 4):
            result *= int(data[row-index][col-index].strip())
    else:
        result = 0
    return result

def RightUp(data, row, col):
    result = 1
    if row >= 3 and row < len(data) and (col + 3 ) < len(data[row]):
        for index in range(0, 4):
            result *= int(data[row-index][col+index].strip())
    else:
        result = 0
    return result

print __file__
print os.path.dirname(__file__)
file = open(os.path.dirname(__file__) + "/data.txt")

data = []

line = file.readline()


while line:
    tmp = line.split(" ")
    data.append(tmp)
    line = file.readline()

result = 0

for i in range(0, len(data)):
    for j in range(0, len(data[i])):
        result = max( result, Up(data, i, j) )
        result = max( result, Left(data, i, j) )
        result = max( result, LeftUp(data, i, j) )
        result = max( result, RightUp(data, i, j) )


print result

file.close()
