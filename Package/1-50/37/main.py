import os, sys

import os, sys
from copy import deepcopy

lim = 1000000

primeDic = {}
primeList = []

for index in range(2, lim):
    if not primeDic.has_key(index):
        primeList.append(index)
        target = index * 2
        while target < lim:
            primeDic[target] = 1
            target += index

primeDic.clear()
for index in range(0, len(primeList)):
    primeDic[primeList[index]] = 1

def truncPrime(num):
    tmp = num
    flag = True

    sum = 0
    pp = 0
    while tmp > 0:
        #print tmp
        if not primeDic.has_key(tmp):
            flag = False
            break

        sum += (tmp%10)*pow(10, pp)
        pp += 1

        #print tmp, sum
        if not primeDic.has_key(sum):
            flag = False
            break

        tmp /= 10

    return flag

#print truncPrime(3797)
sum = 0
for index in range(0, len(primeList)):
    if primeList[index] >= 10 and truncPrime(primeList[index]):
        sum += primeList[index]
        print primeList[index]

print "sum=", sum
