maxLen = 1000000

dic={}
dic[1] = 0

for val in range(2, maxLen+1):
    if val not in dic:
        dic[val] = 1

    mul = val
    while mul * val <= maxLen:
        if mul * val not in dic:
            dic[mul * val] = 1
        if mul == val:
            dic[mul *val] += val
        else:
            dic[mul*val] += mul + val
        
        mul += 1

    

length = {}



def findNumber(num):
    foundSet = set()
    foundSet.add(num)
    cur = num
    while cur > 0 and cur <= maxLen and dic[cur] not in foundSet :
        cur = dic[cur]
        foundSet.add(cur)
    if cur > 0 and cur <= maxLen and dic[cur] == num:
        return len(foundSet), foundSet
    else:
        return -1, set()

#print(findNumber(12496))

preLen = -1
preNumber = 0
for val in range(2, maxLen+1):
   if val not in length:
        ll, vSet = findNumber(val)
        if ll > 0:
            for ss in vSet:
                length[ss] = ll
            if ll > preLen:
                preLen = ll
                preNumber = val
        
print(preLen,":",preNumber)
