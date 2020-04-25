'''
(x+2a)^2-(x+a)^2-x^2
=x^2+4ax+4aa-x^2-2ax-aa-x^2
=2ax+3aa-x*x
=4aa-(x-a)^2

2a > x-a
3a > x
'''
import math

limit = pow(10,6)
ansDic = dict()

for x in range(1, 2000000):
    a = x // 3
    a = max(a, 1)
    m = 2*a*x+3*a*a-x*x
    while m < limit:
        if m not in ansDic:
            ansDic[m] = 0
        ansDic[m] += 1

        a += 1
        m = 2*a*x+3*a*a-x*x


ansSum = 0
for k,v in ansDic.items():
    if v == 10:
        ansSum += 1

print('ans=',ansSum)