'''
16 * 8 * 16
'''
def GetNewBit(n, num):
    if num == 0 :
        return n | 1
    elif num == 1:
        return n | 2
    elif num == 10:
        return n | 4
    else:
        return n

def GetHexNumber(n):
    ret = 0
    base = 16
    head = [ [ 0 for j in range(8)] for i in range(base)]
    head[1][1<<1] = 1
    head[10][1<<2] = 1
    for i in range(1, 16):
        if i != 1 and i != 10:
            head[i][0] = 1
    
    for i in range(1, n):
        end = [ [ 0 for y in range(8)] for x in range(base)]

        for x in range(base):
            for y in range(8):
                for z in range(base):
                    end[z][GetNewBit(y,z)] += head[x][y]    

        head = end
        for x in range(base):
            ret += head[x][7]
    
    return ret

#print(GetHexNumber(3))
ans = GetHexNumber(16)
print(ans)
print("%X"%ans)
