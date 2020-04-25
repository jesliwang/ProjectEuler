import math

checkDic = dict()
for i in range(1,2000000):
    checkDic[i*i] = 1

for x in range(3, 1000000):
    start = math.ceil(math.sqrt(x))
    matchList = list()
    while start*start < 2 * x:
        tmp = start*start - x
        if x - tmp in checkDic:
            matchList.append(tmp)
        start +=1
    if len(matchList) > 1:
        #print(matchList)
        for i in range(len(matchList)):
            for j in range(i+1,len(matchList)):
                if matchList[i]+matchList[j] in checkDic and (matchList[j]-matchList[i]) in checkDic:
                    print(matchList[i],matchList[j],x, matchList[i]+matchList[j]+x)