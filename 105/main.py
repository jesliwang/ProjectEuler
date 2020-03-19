import os, sys
import math


file = open(os.path.dirname(__file__) + "/sets.txt")

line = file.readline()

def test_set(numSet):
    numSet.sort()
    # 1. 不能有相同元素
    for index in range(len(numSet)):
        if index + 1 < len(numSet):
            if numSet[index] == numSet[index+1]:
                return False

    # 2. 满足条件2
    for slen in range(2, len(numSet)):
        if slen + slen - 1 <= len(numSet):
            left = 0
            right = 0
            for leftIndex in range(slen):
                left += int(numSet[leftIndex])
            for rightIndex in range(slen - 1):
                right += int(numSet[len(numSet)-1-rightIndex])
            if left <= right:
                return False

    # 3. 条件1 abs(pre)+/-new
    dicSet = set()
    for index in range(len(numSet)):
        if numSet[index] in dicSet:
            return False
        dicSet.update({ abs(x+numSet[index]) for x in dicSet})
        dicSet.update({ abs(x-numSet[index]) for x in dicSet})
        dicSet.add(numSet[index])
        #print(dicSet)
    
    return True


def sumArr(numSet):
    sum=0
    for number in numSet:
        sum+=number
    return sum

sumAns = 0
while line:
    numSet = line.strip().split(',')
    numSet = list(map(int,numSet))
    if test_set(numSet):
        sumAns += sumArr(numSet)

    line = file.readline()

print(sumAns)


