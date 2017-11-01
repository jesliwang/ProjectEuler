import os, sys

def squareDigit(num):
    tmp = num
    ret = 0
    while tmp > 0:
        ret += pow(tmp%10, 2)
        tmp/=10
    return ret

def Solve_92():
    checkDic = { 1:1, 89:2}

    maxLim = 81*7


    for index in range(1, maxLim + 1):
        if not checkDic.has_key(index):
            checkList = [index]
            while not checkDic.has_key(checkList[len(checkList)-1]):
                checkList.append(squareDigit(checkList[len(checkList)-1]))

            target = checkDic[checkList[len(checkList)-1]]
            while len(checkList) > 0:
                checkDic[checkList[0]] = target
                del checkList[0]
    ret = 0
    lim = 1000000 * 10
    #lim = 10000

    for index in range(1, lim):
        if checkDic.has_key(index):
            if 2 == checkDic[index]:
                ret += 1
        else:
            p = squareDigit(index)
            if checkDic.has_key(p):
                if 2 == checkDic[p]:
                    ret += 1

            else:
                print "Wrong"

    return ret

print Solve_92()
