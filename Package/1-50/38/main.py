import os, sys

def check(number):
    arrangeList = []
    tmp = number
    while tmp > 0:
        arrangeList.append(tmp%10)
        tmp /= 10

    arrangeList.reverse()

    sumNow = 0
    index = 0
    while index < len(arrangeList):
        sumNow = sumNow * 10 + arrangeList[index]
        index += 1
        tmpIndex = index
        for subIndex in range(2, 100):
            mayAns = sumNow * subIndex
            tmpList = []
            while mayAns > 0:
                tmpList.append(mayAns%10)
                mayAns/= 10
            tmpList.reverse()

            while tmpIndex < len(arrangeList) and len(tmpList) > 0 and tmpList[0] == arrangeList[tmpIndex]:
                del tmpList[0]
                tmpIndex += 1

            if len(tmpList) == 0 and tmpIndex == len(arrangeList):
                return True
            elif len(tmpList) > 0:
                break

    return False



def generateNumber(numList, pre):
    if len(numList) == 1:
        tmp = pre * 10 + numList[0]
        #print tmp
        if check(tmp):
            return (True, tmp)
        else:
            return (False, 0)
    else:
        for index in range(0, len(numList)):
            tmp = numList[index]
            del numList[index]
            thisFlag, thisAns = generateNumber(numList, pre * 10 + tmp)
            if thisFlag:
                return (thisFlag, thisAns)
            numList.insert(index, tmp)
        return (False, 0)



def SolveProblem38():
    print generateNumber([9,8,7,6,5,4,3,2,1], 0)


SolveProblem38()
