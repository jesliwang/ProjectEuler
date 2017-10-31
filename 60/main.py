import sys,os
sys.path.append( os.path.dirname(__file__) + "/../Common")

import PrimeUtil

def lengthNumber(num):
    tmp = num
    length = 0
    while tmp > 0:
        length += 1
        tmp/=10
    return length

def concatNumber(a, b):
    aLen = lengthNumber(a)
    bLen = lengthNumber(b)

    return a*pow(10,bLen)+b, b*pow(10,aLen)+a

def checkMatch(lt, target, checkDic):

    if target == 1:
        if len(lt) >= target:
            return True, [lt[0]]
        else:
            return False, []


    for index in range(0, len(lt)):
        nextList = []
        for subIndex in range(0, len(lt)):
            if lt[subIndex] in checkDic[lt[index]]:
                nextList.append(lt[subIndex])

        if len(nextList) >= target - 1:
            flag, retList = checkMatch(nextList, target - 1, checkDic)
            if flag:
                retList.insert(0, lt[index])
                return flag, retList

    return False, []


def Solve_60(target):

    maxNumber = 10000

    primeDic, PrimeList = PrimeUtil.get_prime_dic_and_list(maxNumber)

    matchDic = {}

    for index in range(0, len(PrimeList)):
        for subIndex in range(index + 1, len(PrimeList)):
            a,b = concatNumber(PrimeList[index], PrimeList[subIndex])
            #print a, b, PrimeList[index], PrimeList[subIndex]
            if PrimeUtil.is_mill_rabin_prime(a) and PrimeUtil.is_mill_rabin_prime(b):
                if not matchDic.has_key(PrimeList[index]):
                    matchDic[PrimeList[index]] = []

                matchDic[PrimeList[index]].append(PrimeList[subIndex])

                if not matchDic.has_key(PrimeList[subIndex]):
                    matchDic[PrimeList[subIndex]] = []

                matchDic[PrimeList[subIndex]].append(PrimeList[index])


    ansRet = sys.maxint

    for (k,v) in matchDic.items():
        if len(v) >= target - 1:
            flag, ans = checkMatch(v, target - 1, matchDic)
            if flag:
                nowSum = k
                #print "===="
                #print k
                for index in range(0, len(ans)):
                #    print ans[index]
                    nowSum += ans[index]

                #print "sum=",nowSum
                ansRet = min(ansRet, nowSum)

    return ansRet
print Solve_60(5)
