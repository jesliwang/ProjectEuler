
dic = {}

maxLen = 1000000

count = 0

def CountHCF(num, frac):
    counting = set()
    dup = 0
    for val in frac:
        tmpSet = set()
        dup += num/val
        tmpSet.add((val, 1))
        for pre in counting:
            dup += pow(-1, pre[1]) * num/(pre[0]*val)
            tmpSet.add((pre[0]*val, pre[1]+1))
        counting = counting.union(tmpSet)
    
    return num - dup

for index in range(2, maxLen + 1):
    if index not in dic:
        count += index - 1

        mul = 2
        while mul * index <= maxLen:
            if mul * index not in dic:
                dic[mul*index] = set()
            
            dic[mul*index].add(index)
            mul += 1
    else:
        count += CountHCF(index, dic[index])
    

print(count)
