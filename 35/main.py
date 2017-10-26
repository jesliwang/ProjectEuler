import os, sys

primeDic = {}

lim = 1000000

def searchListNumber(numList , preNum):
    if None == numList or len(numList) == 0:
        return False

    if len(numList) == 1:
        ans = preNum*10 + numList[0]
        return not primeDic.has_key(ans)
    else:
        index = 0;

        flag = True

        while index < len(numList):
            tmp = numList[index]
            del numList[index]
            ansFlag = searchListNumber(numList, preNum*10+tmp)
            if not ansFlag:
                flag = False
                break

            numList.insert(index, tmp)
            index += 1

        return flag


def generateRotatins(num):
    tmp = num
    digitList = []
    while tmp > 0:
        digitList.append(tmp%10)
        tmp/=10

    digitList.sort()
    digitList.reverse()

    maxNum = 0
    for index in range(0, len(digitList)):
        maxNum = maxNum*10 + digitList[index]
    if maxNum > num:
        return False

    retList = searchListNumber(digitList, 0)

    return retList

altCount = 0
ansList = []



for index in range(2,lim):
    if not primeDic.has_key(index):
        facter = 2
        while facter * index < lim:
            primeDic[facter*index] = 1
            facter += 1
        """
        flag = generateRotatins(index)
        if flag:
            altCount += 1
            ansList.append(index)
            print index
        """

#print "ans=", altCount

#print generateRotatins(197)

def rotatPrime(num):
    tmp = num
    dList = []
    while tmp > 0:
        dList.append(tmp%10)
        tmp/=10
    dList.reverse()

    flag = True
    for index in range(0, len(dList)):
        sum = 0
        for subIndex in range(0, len(dList)):
            sum = sum * 10 + dList[(index + subIndex)%len(dList)]

        if primeDic.has_key(sum):
            flag = False
            break
    return flag


rotateP = 0

for index in range(2,lim):
    if not primeDic.has_key(index):
        if rotatPrime(index):
            rotateP += 1
            print index

print "rotateP",rotateP

print rotatPrime(197)

"""
2
3
5
7
11
31
13
71
17
73
37
97
79
311
113
131
733
373
337
991
919
199
"""
