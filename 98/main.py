import os, sys
import math
from copy import deepcopy

file = open(os.path.dirname(__file__) + "/words.txt")

def checkWords(str):
    minNum = int(math.ceil( pow(pow(10, len(str)-1),0.5) ))
    maxNum = int(math.floor( pow(pow(10, len(str)),0.5) ))

    matchArray = []

    maxValue = -1

    index = minNum
    while index <= maxNum:
        tmp = index * index
        index += 1

        matchDic = {}

        modNum = tmp

        subIndex = len(str)-1
        while tmp > 0 and subIndex >= 0:
            key = tmp % 10

            if not matchDic.has_key(str[subIndex]):
                matchDic[str[subIndex]] = [key]
            elif matchDic[str[subIndex]] == key:
                matchDic[str[subIndex]].append(key)
            else:
                break
            tmp /= 10
            subIndex -= 1

        # sucess
        if subIndex < 0:
            appendItem = {}

            flag = True
            for key,value in matchDic.items():
                if appendItem.has_key(value[0]):
                    flag = False
                    break
                else:
                    appendItem[value[0]] = len(value)

            if not flag:
                continue
            #print modNum
            matchArray.append(appendItem)

    if len(matchArray) == 0:
        return False, 0

    ansDic = {}
    index = minNum
    while index <= maxNum:
        tmp = index * index
        index += 1

        for subindex in range(0, len(matchArray)):
            modNum = tmp
            checkMatch = deepcopy(matchArray[subindex])
            while modNum > 0:
                key = modNum % 10

                if checkMatch.has_key(key) and checkMatch[key] > 0:
                    checkMatch[key] = checkMatch[key] - 1
                else:
                    break
                modNum /= 10

            if 0 == modNum:
                if not ansDic.has_key(subindex):
                    ansDic[subindex] = [tmp]
                else:
                    #print "ev" , subindex, ansDic[subindex][0], ":", tmp
                    maxValue = max(maxValue, tmp)
                    ansDic[subindex].append(tmp)

    if maxValue > 0:
        return True, maxValue
    else:
        return False, 0


def checkWordsNew(str, bak):
    minNum = int(math.ceil( pow(pow(10, len(str)-1),0.5) ))
    maxNum = int(math.floor( pow(pow(10, len(str)),0.5) ))

    maxValue = -1

    index = minNum
    while index <= maxNum :
        tmp = index * index
        if tmp >= pow(10, len(str)):
            break
        index += 1


        matchDic = {}

        modNum = tmp

        subIndex = len(str)-1

        checkssss ={}

        while tmp > 0 and subIndex >= 0:
            key = tmp % 10

            if not matchDic.has_key(str[subIndex]):
                if not checkssss.has_key(key):
                    checkssss[key] = 1
                    matchDic[str[subIndex]] = [key]
                else:
                    break
            elif matchDic[str[subIndex]] == key:
                matchDic[str[subIndex]].append(key)
            else:
                break
            tmp /= 10
            subIndex -= 1

        # sucess
        if subIndex < 0:
            numNew = 0
            for searchIndex in range(len(bak)):
                numNew = numNew * 10 + matchDic[bak[searchIndex]][0]

            if numNew >= pow(10, len(str)-1) and numNew < pow(10, len(str)):
                if pow(math.floor(pow(numNew,0.5)), 2) == numNew and modNum != numNew:
                    #print "mm",pow(10, len(str)-1), pow(10, len(str)),modNum,numNew

                    maxValue = max(maxValue, modNum)
                    maxValue = max(maxValue, numNew)

    if maxValue < 0:
        return False, 0
    else:
        return True, maxValue


#flag, v = checkWords("TRADITIONAL")
#print flag,v
"""
ans = -1

line = file.readline()
while line:
    ss = line.split(',')

    for index in range(len(ss)):
        flag, v = checkWords(ss[index][1:-1])
        if flag:
            print ss[index], v
            ans = max(ans, v)

    line = file.readline()

print ans

"""

def sameString(a,b):
    dic = {}
    for index in range(len(a)):
        if not dic.has_key(a[index]):
            dic[a[index]] = 1
        else:
            dic[a[index]] = dic[a[index]] + 1

    for index in range(len(b)):
        if not dic.has_key(b[index]):
            return False
        elif dic[b[index]]<=0:
            return False
        else:
            dic[b[index]] = dic[b[index]] - 1

    return True

ans = -1

line = file.readline()
while line:
    ss = line.split(',')
    ss.sort(lambda a,b: len(a)-len(b))

    for index in range(len(ss)):
        for subindex in range(index+1,len(ss)):
            if len(ss[index]) != len(ss[subindex]):
                break
            if sameString(ss[index], ss[subindex]):
                flag, v = checkWordsNew(ss[index][1:-1],ss[subindex][1:-1])
                if flag:
                    print ss[index], ss[subindex], v
                    ans = max(ans, v)
            #print ss[index], ss[subindex]


        #flag, v = checkWords(ss[index][1:-1])
        #if flag:
        #    print ss[index], v
        #    ans = max(ans, v)

    line = file.readline()

print ans
