import os, sys

primeDic = {}

#lim = 1000000
lim = 1000000

primeList = []

for index in range(2, lim):
    if not primeDic.has_key(index):
        primeList.append(index)
        target = index * 2
        while target < lim:
            primeDic[target] = 1
            target += index

ans = 0
preLength = 0

sumDic = { -1 : 0}

for index in range(0, len(primeList)):
    sumDic[index] = sumDic[index - 1] + primeList[index]

    starIndex = 0

    sum = primeList[index]
    subIndex = starIndex

    length = 0
    while subIndex < index and starIndex < index:
        if sum > 0:
            sum -= primeList[subIndex]
            subIndex += 1
            length += 1
        elif sum < 0:
            sum += primeList[starIndex]
            starIndex += 1
            length -= 1

            if length + 2 < preLength:
                break
        else:
            break


    if sum == 0:
        if length > preLength:
            preLength = length
            ans = primeList[index]


print ans,preLength
