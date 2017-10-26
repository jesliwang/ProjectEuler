import os, sys

lim = 1000

countDic = {}

for index in range(1, lim + 1):
    for sedIndex in range(index, lim + 1):
        for thirdIndex in range(sedIndex, index + sedIndex):
            if index + sedIndex + thirdIndex <= lim:
                if pow(index, 2) + pow(sedIndex, 2) == pow(thirdIndex, 2):
                    sum = index + sedIndex + thirdIndex
                    if not countDic.has_key(sum):
                        countDic[sum] = 0

                    countDic[sum] = countDic[sum] + 1

            else:
                break

length = 0
target = 0
for index in range(1, lim+1):
    if countDic.has_key(index):
        if countDic[index] > length:
            target = index
            length = countDic[index]

print target,length
