

def convert(num):
    fracDic={}
    fracDic[0] = 1
    for i in range(1, 10):
        fracDic[i] = fracDic[i-1] * i

    tmp = num
    result = 0
    while tmp > 0:
        last = tmp%10
        tmp = int(tmp /10)
        result = result + fracDic[last]

    
    return result



resultDic = {}

def GetTerm(num):
    found = []
    tmp = num
    while not ( tmp in found ):
        found.append(tmp)
        if tmp in resultDic:
            tmp = resultDic[tmp]
        else:
            n = convert(tmp)
            resultDic[tmp] = n
            tmp = n
    return len(found)

ans = 0
for i in range(1, 1000000):
    if GetTerm(i) == 60:
        ans += 1
    #if GetTerm(i) > 60:
    #    print("warn:",i,":",GetTerm(i))

print("ans=",ans)
