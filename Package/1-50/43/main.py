#!/bin/python

import os, sys
primeDic={}

def checkThreeDiff(num):
    checkDic = {}
    if num < 10:
        return False
    elif num < 100:
        checkDic[0]=1

    tmp = num
    while tmp > 0:
        if checkDic.has_key(tmp%10):
            return False
        else:
            checkDic[tmp%10] = 1
        tmp /= 10

    return True

for index in range(2,1000):
    if not primeDic.has_key(index):
        #print index

        primeDic[index]=[]
        facter = 2
        while facter * index < 1000:
            if checkThreeDiff(facter * index):
                primeDic[index].append(facter*index)

            primeDic[facter*index] = 1
            facter +=1

checkList = [17,13,11,7,5,3,2]

divSum = []

def checkDivisible(depth, pre, dic, number):
    if depth == len(checkList):
        for index in range(0, 10):
            if not dic.has_key(str(index)):
                target = number + int(index)*pow(10, depth + 2)
                divSum.append(target)
                tmp = str.format("{0:010}", target)
                print tmp
                return


    for index in range(0,len(primeDic[checkList[depth]])):
        if depth == 0:
            tmp = str.format("{0:03}", primeDic[checkList[depth]][index]);
            dic = {}
            dic[tmp[0]]=1
            dic[tmp[1]]=2
            dic[tmp[2]]=3
            checkDivisible(depth+1, primeDic[checkList[depth]][index], dic, primeDic[checkList[depth]][index])
            dic.clear()
        else:
            preStr = str.format("{0:03}", pre);
            tmp = str.format("{0:03}", primeDic[checkList[depth]][index]);
            #print tmp
            if tmp[1] == preStr[0] and tmp[2] == preStr[1] and (not dic.has_key(tmp[0])):
                dic[tmp[0]] = 1
                target = number + int(tmp[0])*pow(10, depth + 2)
                checkDivisible(depth+1, primeDic[checkList[depth]][index], dic, target)
                del dic[tmp[0]]

checkDivisible(0, 0, {}, 0)

ans = 0
for index in range(0, len(divSum)):
    ans += divSum[index]

print ans
