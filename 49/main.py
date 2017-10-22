import os, sys
from copy import deepcopy

lim = 10000

primeDic = {}
primeList = []

for index in range(2, lim):
    if not primeDic.has_key(index):
        if index >= 1000:
            primeList.append(index)
        target = index * 2
        while target < lim:
            primeDic[target] = 1
            target += index

primeDic.clear()
for index in range(0, len(primeList)):
    primeDic[primeList[index]] = 1

def triPermutations(a, b, c):
    checkDic = {
    }

    oriA = a
    oriB = b
    oriC = c
    while a > 0:
        if not checkDic.has_key(a%10):
            checkDic[a%10] = 1
        else:
            checkDic[a%10] = checkDic[a%10] + 1

        a/=10

    tmpDic = deepcopy(checkDic)
    #print oriA, oriB, oriC
    while b > 0:
        if tmpDic.has_key(b%10) and tmpDic[b%10] > 0 :
            tmpDic[b%10] = tmpDic[b%10] - 1
            b/=10
        else:
            return False
    #print "1111"
    tmpDic = deepcopy(checkDic)
    while c > 0:
        if tmpDic.has_key(c%10) and tmpDic[c%10] > 0:
            tmpDic[c%10] = tmpDic[c%10] - 1
            c/=10
        else:
            return False
    #print "222"
    return True

for index in range(0, len(primeList)):
    for subIndex in range(index + 1, len(primeList)):
        if primeDic.has_key( 2 * primeList[subIndex] - primeList[index] ):
            if triPermutations(primeList[index], primeList[subIndex], primeList[subIndex] * 2 - primeList[index]):
                print primeList[index], primeList[subIndex], primeList[subIndex] * 2 - primeList[index]
"""
for index in range(1000, 10000):
    for subIndex in range(index + 1, 10000):
        if primeDic.has_key( 2 * subIndex - index ):
            if triPermutations(index, subIndex, subIndex * 2 - index):
                print index, subIndex, subIndex * 2 - index
"""

print "end"
