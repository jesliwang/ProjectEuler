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

def FindSet(sLen, start, sum, preset):
    #if sLen > 3:
    #    print(sLen,"====",start,":",sum,"#",preset)
    if sLen < len(preset) and sum >= sumArr(preset):
        return None
    
    if sLen == 1:
        if sum >= start:
            dSet = set()
            dSet.update(preset)
            dSet.add(sum)
            #print(dSet)
            if test_set(list(dSet)):
                return dSet
    else:
        nNum = start
        while nNum * sLen < sum:

            dSet = set()
            dSet.update(preset)
            dSet.add(nNum)
            nextSet = FindSet(sLen - 1, nNum + 1, sum - nNum, dSet)
            #print(nextSet)
            if None != nextSet:
                return nextSet
            
            nNum += 1


    #print(dSet)        
    return None

def sumArr(numSet):
    sum=0
    for number in numSet:
        sum+=number
    return sum

#print(FindSet(6,1, 115, set()))
#7 20313839404245
tLen = 7
target = tLen
while True:
    #print(target)
    maySet = FindSet(tLen,1, target, set())
    #print(target)
    if None != maySet:
        print(maySet)
        break
    target += 1

print(target)

'''
pLen = 6
base = list(FindSet(pLen,1))
base.sort()
ss = sumArr(base)
#print(ss)

while True:
    flag = True
    for x in range(pLen):
        preSet = set()
        for y in range(x):
            preSet.add(base[y])

        preSet.update(FindSet(pLen-x, base[x] + 1))
        print(preSet)
        ns = sumArr(preSet)
        if ns < ss:
            flag = False
            base = list(preSet).sort()
            ss = ns
            break
    if flag:
        break

print(base)

'''
