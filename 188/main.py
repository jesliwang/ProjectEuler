'''
m^( a^x*b^y)
= (m^a)^x * (m^b)^y

(a^x*b^y)^(a^x*b^y)
= a^
2 ,4, 8, 16, 32, 64 128, 256, 512, 1024, 2048, 4096, 8192,   16384,    32768,  


'''
import sys

sys.setrecursionlimit(3000)

def fastPow(a, b, mod):
    tmp = b
    cur = a
    ret = 1
    while tmp > 0:
        if tmp & 1 == 1:
            ret = (cur * ret)%mod
        cur = (cur * cur)%mod
        tmp >>= 1
    
    return ret
        

def GetSimpled(a, b, divsor):
    if b == 1:
        return a % divsor
    else:
        #return pow(a, GetSimpled(a, b-1, divsor)) % divsor
        return fastPow(a, GetSimpled(a, b-1, divsor), divsor)

def GetTetration(a, b, mod):
    ansDic = dict()
    p = a
    ansDic[p] = 1
    while (p*a) % mod not in ansDic:
        p = (p*a) % mod
        ansDic[p] = 1

    divor = len(ansDic)

    if b == 2:
        return pow(a,a) % mod
    else:
        return pow(a, GetSimpled(a,b-1, divor)) % mod

print(GetTetration(1777, 1855, 100000000))

    