import os, sys
from copy import deepcopy


def checkInfo(fact, factDic, ans):

    checkDic = {}

    for fIndex in range(0, len(fact)):
        for index in range(factDic[fact[fIndex]][0], factDic[fact[fIndex]][1]):
            n = index
            tmp = eval(fact[fIndex])

            pv = tmp / 100
            nt = tmp % 100

            if not checkDic.has_key(pv):
                checkDic[pv] = {}
                checkDic[pv][0] = {}
                checkDic[pv][1] = {}

            if not checkDic[pv][0].has_key(tmp):
                checkDic[pv][0][tmp] = []

            checkDic[pv][0][tmp].append(fIndex)

            if not checkDic.has_key(nt):
                checkDic[nt] = {}
                checkDic[nt][0] = {}
                checkDic[nt][1] = {}

            if not checkDic[nt][1].has_key(tmp):
                checkDic[nt][1][tmp] = []

            checkDic[nt][1][tmp].append(fIndex)

    searchList = []
    searchDic = {}
    for index in range(factDic[fact[0]][0], factDic[fact[0]][1]):
        n = index
        tmp = eval(fact[0])

        searchList.append(tmp)
        searchDic[tmp] = { 0:[[0]], 1:[[tmp]]}


    mayAns = []

    while len(searchList) > 0:
        checkVal = searchList[0]
        del searchList[0]

        nt = checkVal % 100

        fk = deepcopy(searchDic[checkVal])
        del searchDic[checkVal]

        if nt < 10:
            continue

        for mIndex in range(0, len(fk[0])):
            if len(fk[0][mIndex]) == len(fact):
                if fk[1][mIndex][len(fact) - 1] % 100 == fk[1][mIndex][0] / 100:
                    tmp = deepcopy(fk[1][mIndex])
                    mayAns.append(tmp)

        for k,v in checkDic[nt][0].items():
            for subIndex in range(0, len(v)):
                for mIndex in range(0, len(fk[0])):
                    if v[subIndex] not in fk[0][mIndex]:
                        newList = deepcopy(fk[0][mIndex])
                        newList.append(v[subIndex])

                        newPP = deepcopy(fk[1][mIndex])
                        newPP.append(k)

                        if k not in searchList:
                            searchList.append(k)

                        if not searchDic.has_key(k):
                            searchDic[k] = {0:[], 1:[]}

                        searchDic[k][0].append(newList)
                        searchDic[k][1].append(newPP)

    for index in range(0, len(mayAns)):
        return True, mayAns[index]


    return False, []

def Solve_61():
    fact = ["n*(n+1)/2", "n*n", "n*(3*n-1)/2", "n*(2*n-1)", "n*(5*n-3)/2", "n*(3*n-2)"]
    factDic = {}

    for index in range(0, len(fact)):
        start = 1

        while True:
            n = start
            num = eval(fact[index])
            if num >= 1000 and num < 10000:
                if not factDic.has_key(fact[index]):
                    factDic[fact[index]] = [start]
            elif num >= 10000 :
                if factDic.has_key(fact[index]):
                    factDic[fact[index]].append(start)
                else:
                    print "Error"
                break

            start += 1


    flag, ansList = checkInfo(fact, factDic, [])

    retSum = 0
    if flag:
        print len(ansList), "==="
        for index in range(0, len(ansList)):
            print ansList[index]
            retSum += ansList[index]

    return retSum

print Solve_61()
