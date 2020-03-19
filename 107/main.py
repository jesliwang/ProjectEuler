import os, sys
import math


file = open(os.path.dirname(__file__) + "/network.txt")

def sumArr(numSet):
    sum=0
    for number in numSet:
        sum+=number
    return sum

def FindMinMatrix(matrix):
    minSum = 0
    findSet = {0}
    nCount = len(matrix)

    while len(findSet) < nCount:
        selX = -1
        selY = -1
        for v in range(nCount):
            if v not in findSet:
                f = 0
                while f < nCount:
                    
                    if f != v and f in findSet:
                        if matrix[f][v] > 0:
                            if selX == -1:
                                selX = f
                                selY = v
                            elif matrix[f][v] < matrix[selX][selY]:
                                selX = f
                                selY = v
                        
                    f += 1
                

        if selX != -1:
            #print(selX,":",selY,"#",matrix[selX][selY])
            minSum += matrix[selX][selY]
            findSet.add(selY)
            #print(findSet)

    return minSum

Hmap = None

line = file.readline()

rawSum = 0

index = 0
while line:
    lineSplit = line.strip().split(',')
    mapLen = len(lineSplit)
    if None == Hmap:
        Hmap = [[0 for i in range(mapLen)] for j in range(mapLen)]

    for v in range(mapLen):
        if lineSplit[v] == '-':
            Hmap[index][v] = 0
        else:
            Hmap[index][v] = int(lineSplit[v])
            rawSum += Hmap[index][v]

    index += 1

    line = file.readline()

rawSum = rawSum/2
#print(Hmap)

print(rawSum)
minAttr = FindMinMatrix(Hmap)
print(minAttr)
print(rawSum - minAttr)


