import os, sys

primeDic = {}
primeList = []

powDic = { 1: 1}

lim = 100000

def checkChristian(num):
    if num % 2 == 0:
        return False

    for index in range(0, len(primeList)):
        if primeList[index] > num:
            break
        else:
            sub = num - primeList[index]
            if sub % 2 == 0 and powDic.has_key(sub/2):
                return True

    return False

for index in range(2, lim):
    if pow(index, 2) < lim:
        powDic[pow(index,2)] = 1

    if not primeDic.has_key(index):
        primeList.append(index)
        facter = 2
        while facter * index < lim:
            primeDic[facter*index] = 1
            facter += 1
    else:
        if index % 2 == 1 and (not checkChristian(index)):
            print index
            break
