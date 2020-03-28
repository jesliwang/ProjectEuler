'''
0 up
1 down
2 equal
a[0][n][x] = a[0][n-1][0:x]+a[2][n-1][0:x-1]
a[1][n][x] = a[1][n-1][x:9] + a[2][x+1:9]
a[2][n][x] = a[2][n-1][x]

'''

import sys

def GetNonBouncy(arr):
    ret = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            ret += arr[i][j]
    return ret

current = [[0 if row != 2 else 1 for i in range(10)] for row in range(3)]

sumW = 0
sumW += GetNonBouncy(current)
n = 100

for c in range(2,n+1):
    nt = [[0 for j in range(10)] for i in range(3)]
    for i in range(10):
        zero = 0
        for x in range(i+1):
            zero += current[0][x]
        
        for x in range(i):
            if c == 2 and x == 0:
                continue
            zero += current[2][x]
        nt[0][i] = zero

        one = 0
        for x in range(i, 10):
            one += current[1][x]
        for x in range(i+1, 10):
            one += current[2][x]

        nt[1][i] = one

        if not(c == 2 and i == 0):
            nt[2][i] = current[2][i]
    #print(nt)
    current = nt    
    sumW += GetNonBouncy(current)

print(sumW - 1)
