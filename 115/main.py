'''
f(n) = f(n-4) + f(n-5) + ...f(0)

f(1, 0) = 1  f(1,1) = 0
f(2, 0) = 1  f(2,1) = 0
f(3, 0) = 1  f(3,1) = 1
f(4, 0) = 2  f(4,1) = 1
f(5, 0) = 3  f(5,1) = 2
f(6, 0) = 5  f(6,1) = 3
f(7, 0) = 8  f(7,1) = 5

'''
import sys

#n = 7
m = 50
n = 1000
limit = 1000000

f = [[0 for j in range(n+1)] for i in range(n+1)]

f[0][0] = 1

for i in range(1, n+1):
    for j in range(0, i+1):
        if j >= 1 and j < m:
            continue
        f[i][0] += f[i-1][j]
    for j in range(1, i + 1):
        f[i][j] = f[i-1][j-1]
    
    if f[i][0] > limit:
        print(i-1)
        break
    


