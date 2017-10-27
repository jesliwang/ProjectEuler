import os, sys

index = 1
penDic = {}
penList = []

def Pentagon(num):
    return num * ( 3 * num - 1) / 2

result = 0
while True:
    penDic[Pentagon(index)] = index
    penList.append(Pentagon(index))
    index += 1

    if len(penList) >= 4:
        subIndex = len(penList) - 2

        flag = False
        while subIndex > 1:
            if penDic.has_key(penList[len(penList)-1] - penList[subIndex]) and penDic.has_key(2*penList[subIndex] - penList[len(penList)-1]):
                result = penDic[2*penList[subIndex] - penList[len(penList)-1]]
                print result
                print penDic[penList[len(penList)-1] - penList[subIndex]]
                print penDic[penList[subIndex]]
                print penDic[penList[len(penList)-1]]
                flag = True
                break

            subIndex -= 1

        if flag:
            break

print Pentagon(1020),Pentagon(1912),Pentagon(2167),Pentagon(2395)

if flag:
    print result
else:
    print "wrong"
