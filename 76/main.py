import os, sys

def solve_76(target):
    matrix=[[0 for m in range(target+1)] for n in range(target+1)]

    for col in range(1, target+1):
        for row in range(1, target+1):
            tmpSum = 0
            if col > row:
                for tRow in range(row, target+1):
                    tmpSum += matrix[tRow][col-row]

            if col >= 2*row:
                tmpSum += 1

            matrix[row][col] = tmpSum

    ret = 0
    for index in range(1, target+1):
        ret += matrix[index][target];
    return ret

print solve_76(100)
