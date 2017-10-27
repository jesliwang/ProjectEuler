import os, sys

primeDic = {}

lim = 2000000

primeList = []
for index in range(2, lim):
    if not primeDic.has_key(index):
        if index <= 1000:
            primeList.append(index)

        facter = 2
        while facter * index < lim:
            primeDic[facter*index] = 1
            facter += 1

maxLength = 0
targetA = 0
targetB = 0

for index in range(0, len(primeList)):
    for sumIndex in range(0, len(primeList)):
        # 1 + a  +  b = sumIndex
        # a = sumIndex - b - 1
        b = primeList[index]
        a = primeList[sumIndex] - b - 1
        if not (a >= -1000 and a <= 1000):
            continue

        if maxLength < 2:
            maxLength = 2
            targetA = a
            targetB = b

        n = 2
        while n*n + a*n + b > 0 and (not primeDic.has_key(n*n + a*n + b)):
            n+=1

        print n,a,b, n*n + a*n + b > lim

        if n > maxLength:
            maxLength = n
            targetA = a
            targetB = b

print "======"
print maxLength,targetA,targetB
print targetA * targetB

for index in range(0, maxLength):
    print index * index + targetA * index + targetB, primeDic.has_key(index * index + targetA * index + targetB)
