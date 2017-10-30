import os, sys
import copy

def getNumbers(num):
    numDic = {}
    while num > 0:
        if not numDic.has_key(num%10):
            numDic[num%10] = 0

        numDic[num%10] = numDic[num%10] + 1

        num /= 10
    return numDic

def compare(dic, dic2):
    for key in dic.keys():
        if dic2.has_key(key) and dic[key] == dic2[key]:
            del dic2[key]
        else:
            return False
    if len(dic2) == 0:
        return True
    else:
        return False

lim = 1000000

for index in range(1, lim):
    flag = True
    orig = getNumbers(index)
    for subIndex in range(2, 7):
        tmp = getNumbers(subIndex*index)
        p = copy.deepcopy(orig)
        if not compare(p, tmp):
            flag = False
            break

    if flag:
        print index
        break
