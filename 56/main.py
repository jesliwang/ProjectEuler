import os, sys

def sumDigital(num):
    tmp = num
    sumRet = 0
    while tmp > 0:
        sumRet += (tmp%10)
        tmp /= 10

    return sumRet

ans = 0
for a in range(1, 100):
    for b in range(1, 100):
        ans = max(ans, sumDigital(pow(a,b)))

print ans
