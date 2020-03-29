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
n = 50

f = [[0 for j in range(n+1)] for i in range(n+1)]

f[0][0] = 1

for i in range(1, n+1):
    for j in range(0, i+1):
        if j == 1 or j == 2:
            continue
        f[i][0] += f[i-1][j]
    for j in range(1, i + 1):
        f[i][j] = f[i-1][j-1]
    
#print(f)

ans = 0
for i in range(0, n+1):
    if i == 1 or i == 2:
        continue
    ans += f[n][i]
print(ans)

