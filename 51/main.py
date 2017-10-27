import os, sys

primeDic = {}
primeList = {}
lim = 1000000


def genPattern(num):
    if num < 10:
        return []

    tmp = num
    tmpList = []

    while tmp > 0:
        tmpList.append(tmp%10)
        tmp /= 10

    tmpList.reverse()
    ret = []
    preStr = ""
    for index in range(0, len(tmpList)):
        preStr += str(tmpList[index])


    index = 0
    while index < len(tmpList):
        nextIndex = index + 1
        testStr = preStr[0:index] + "*" + preStr[index + 1:len(tmpList)]

        searchList = [testStr]
        while nextIndex < len(tmpList):
            if tmpList[nextIndex] == tmpList[index]:
                aLen = len(searchList)
                for sp in range(0, aLen):
                    searchList.append(searchList[sp][0:nextIndex] + "*" + searchList[sp][nextIndex + 1:len(tmpList)])

            nextIndex += 1

        for retIndex in range(0, len(searchList)):
            ret.append(searchList[retIndex])

        index += 1

    return ret




for index in range(2, lim):
    if not primeDic.has_key(index):
        facter = 2
        while facter * index < lim:
            primeDic[facter*index] = 1
            facter += 1

        pat = genPattern(index)

        for subIndex in range(0, len(pat)):
            if not primeList.has_key(pat[subIndex]):
                primeList[pat[subIndex]] = []

            primeList[pat[subIndex]].append(index)

print "out"
for key, vale in primeList.items():
    if len(vale) >= 8:
        print "============"
        for index in range(0,len(vale)):
            print vale[index], len(vale), key
