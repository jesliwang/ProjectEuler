import sys, os

primeDic = {}

lim = 1000000

preNumber = 1
preDel = 1

for index in range(2, lim):
    if not primeDic.has_key(index):
        facter = 2

        while facter * index < lim:
            if not primeDic.has_key(facter*index):
                primeDic[facter*index] = []

            appendList = [index]
            for subindex in range(0, len(primeDic[facter*index])):
                appendList.append( -1 * primeDic[facter*index][subindex] * index)


            primeDic[facter*index].extend(appendList)

            facter += 1
    else:
        modNumber = 0
        for subindex in range(0, len(primeDic[index])):
            modNumber += index/primeDic[index][subindex]

        #print (index - modNumber), index
        if (index - modNumber) * preDel < preNumber * (index-1):
            preNumber = index - modNumber
            preDel = index
            #break


print preNumber, preDel
