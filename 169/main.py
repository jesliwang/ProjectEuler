'''



'''

#target = 10
target = pow(10,25)
#target = pow(10,18)
#target = 4

unit = [1]


while unit[len(unit)-1] * 2 <= target:
    nt = unit[len(unit)-1] * 2
    unit.append(nt)

hashDic=dict()

def GetAnsFor(n, mx):
    if n == 0:
        return 1

    #print(n)
    ret = 0
    for i in range(mx-1, -1, -1):
        if unit[i] * 4 - 2 >= n and unit[i] <= n:
            nt = n-unit[i]
            if (nt, i) not in hashDic:
                hashDic[(nt,i)] = GetAnsFor(nt, i)

            ret += hashDic[(nt,i)]

            if unit[i] * 2 <= n:
                nt = n -unit[i]*2
                if (nt, i) not in hashDic:
                    hashDic[(nt,i)] = GetAnsFor(nt, i)

                ret += hashDic[(nt,i)]


    return ret


print(GetAnsFor(target, len(unit)))
