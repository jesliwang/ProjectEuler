import os, sys

data = {}
data[1] = 1

def SetCollatzChina(num):
    if data.has_key(num):
        return

    if num % 2 == 0:
        SetCollatzChina(num/2)
        data[num] = data[num/2] + 1
    else:
        SetCollatzChina(3*num + 1)
        data[num] = data[3*num+1] + 1

nowLen = 0
result = 0

for index in range(1, 1000000):
    SetCollatzChina(index)
    if data[index] > nowLen:
        nowLen = data[index]
        result = index


print result, nowLen
