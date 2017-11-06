"""
可以数学方法解决，效率要高很多
https://en.wikipedia.org/wiki/Partition_(number_theory)
"""

import os, sys
import time

def solve_78(target, modNum):
    matrix=[[0 for m in range(target+1)] for n in range(target+1)]

    for col in range(1, target+1):
        checkSum = 0
        row = 0
        while row < col + 1:
        #for row in range(0, col + 1):
            tmpSum = 0
            if col > row and col - row >= row:
                #print col-row, row - 1
                tmpSum += (matrix[col-row][col-row] - matrix[row-1][col-row])
                #for tRow in range(row, target+1):
                #    tmpSum += matrix[tRow][col-row]
                tmpSum += 1

            #if col >= 2*row:
            checkSum += tmpSum
            checkSum %= modNum
            matrix[row][col] = checkSum
            row += 1
            #print row, "," , col, "," ,checkSum
        #print col, checkSum
        if checkSum % modNum == 0:
            return col
            break
    return 0

def solve_78_op(target, modNum):
    matrix=[[] for n in range(target+1)]

    for col in range(1, target+1):
        checkSum = 0
        row = 0
        while 2*row <= col:
            tmpSum = 0
            if 0 != len(matrix[col-row]):
                sp = min(len(matrix[col-row])-1, row-1)
                tmpSum += (matrix[col-row][len(matrix[col-row])-1] - matrix[col-row][sp])

            #tmpSum += (matrix[col-row][col-row] - matrix[row-1][col-row])

            tmpSum += 1

            #if col >= 2*row:
            checkSum += tmpSum
            checkSum %= modNum
            matrix[col].append(checkSum)
            row += 1
            #print row, "," , col, "," ,checkSum
        #print col, checkSum

        p = col / 2 - 1
        if p >= 0:
            matrix[p]=[]

        #print col,checkSum
        if checkSum % modNum == 0:
            return col
            break
    return 0


#print solve_78(50,10000000)
print time.asctime( time.localtime(time.time()) )
print solve_78_op(60000,1000000)
print time.asctime( time.localtime(time.time()) )
