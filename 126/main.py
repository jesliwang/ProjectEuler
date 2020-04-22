def Count(n, x, y, z):
    ret = 0

    f1 = 2*(x*y+x*z+y*z)
    ret += f1
    
    if n - 1 >= 0:
        ret += (n-1) * 4 *(x+y + z)
    
    
    if n - 2 >= 1:
        ret += 8 * ( 1 + n-2) * (n-2) / 2
    
    
    return ret


checkDic = dict()

#limit = pow(10,4)*3
limit = 18880
ll = (limit//2-1)//2+1

for x in range(1, ll):
    for y in range(1, x+1):
        for z in range(1, y+1):
            index = 1
            weight = Count(index,x,y,z)
            if weight >= limit:
                break
            while weight < limit:
                if weight not in checkDic:
                    checkDic[weight] = 0
                checkDic[weight] += 1

                index += 1
                weight = Count(index,x,y,z)


for k,v in checkDic.items():
    if v >= 1000 and v <1010:
        print(k,v)
