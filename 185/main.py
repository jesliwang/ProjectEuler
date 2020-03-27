# https://en.wikipedia.org/wiki/Simulated_annealing

import sys
import random

def diff(key, mached):
    num = 0
    for i in range(len(key)):
        if key[i] == mached[0][i]:
            num += 1
    return abs(mached[1] - num)

def weight(key, template):
    wt = 0
    for v in template:
        wt += diff(key, v)
    return wt

def Accept(nowW, nextW):
    if nextW <= nowW :
        return True
    return False#random.randint(1, 100) >= 80

def shuffle(ch):
    ret = random.randint(0,9)
    while ret == int(ch):
        ret = random.randint(0,9)

    return str(ret)

def Simulated_annealing(template):
    initT = template[0][0]
    initW = weight(initT, template)

    nowT = initT
    nowW = initW
    checkCount = 0
    while nowW > 0:
        preW = nowW
        #print("-------")
        #print(nowT, nowW)
        for i in range(len(initT)):
            #print(nowT, nowW)
            #print(nowT,nowT[0:i], nowT[i+1:len(initT)])
            preT = nowT[0:len(initT)]
            nextT = nowT[0:i] + shuffle(nowT[i]) + nowT[i+1:len(initT)]

            nextW = weight(nextT, template)
            #print(nowT, nowW, nextT, nextW)
            if Accept(nowW, nextW):
                #print(nextW, nextT)
                nowT = nextT[0:len(initT)]
                nowW = nextW


        if preW == nowW:
            checkCount += 1
            #print(checkCount)
            if checkCount >= 20:
                #break
                np = random.randint(0, len(initT)-1)
                #print('---------', nowT, nowW, np)
                nowT = nowT[0:np] + shuffle(nowT[np]) + nowT[np+1:len(initT)]
                nowW = weight(nowT, template)
                checkCount = 0
                #print(nowT,nowW)
        else:
            checkCount = 0
        
        #break
    print(nowT, nowW, weight(nowT, template))
    return nowT


def main(argv=None):
    '''rawData = [
        ("90342", 2),
        ("70794", 0),
        ("39458", 2),
        ("34109", 1),
        ("51545", 2),
        ("12531", 1)
    ]'''
    rawData = [
        ("5616185650518293", 2),
        ("3847439647293047", 1),
        ("5855462940810587", 3),
        ("9742855507068353", 3),
        ("4296849643607543", 3),
        ("3174248439465858", 1),
        ("4513559094146117", 2),
        ("7890971548908067", 3),
        ("8157356344118483", 1),
        ("2615250744386899", 2),
        ("8690095851526254", 3),
        ("6375711915077050", 1),
        ("6913859173121360", 1),
        ("6442889055042768", 2),
        ("2321386104303845", 0),
        ("2326509471271448", 2),
        ("5251583379644322", 2),
        ("1748270476758276", 3),
        ("4895722652190306", 1),
        ("3041631117224635", 3),
        ("1841236454324589", 3),
        ("2659862637316867", 2)
    ]

    ans = Simulated_annealing(rawData)
    
    print(ans)

if __name__ == "__main__":
    exit(main())