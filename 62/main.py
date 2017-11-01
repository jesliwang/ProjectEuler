import os, sys


def generateHashK(num):
    tmp = num
    pList = []
    while tmp > 0:
        pList.append(tmp%10)
        tmp/=10

    pList.sort()
    pList.reverse()

    retK = 0

    for index in range(0, len(pList)):
        retK = retK * 10 + pList[index]

    return retK

def Solve_62(target):
    checkDic = {}

    index = 1
    while True:
        tmp = pow(index, 3)
        haskK = generateHashK(tmp)
        if not checkDic.has_key(haskK):
            checkDic[haskK] = []
        checkDic[haskK].append(tmp)

        if len(checkDic[haskK]) == target:
            return checkDic[haskK][0]

        index += 1

    return 0

print Solve_62(5)
