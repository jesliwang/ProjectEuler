'''
abcdef
     a
---------

'''
import sys
sys.path.append("..")
from Common import PrimeUtil 

def FindN(p1, p2, pre = 0):
    for i in range(10):
        sm = p2 * i + pre
        if sm % 10 == p1 % 10:
            if p1 // 10 == 0:
                return True, i
            else:
                testMin, div = FindN(p1//10, p2, sm // 10)
                if testMin:
                    return True, div * 10 + i

    return False, None

_, primeList = PrimeUtil.get_prime_dic_and_list(1001000)

Nsum = 0
for i in range(len(primeList)):
    if primeList[i] > 1000000:
        breakpoint
    elif primeList[i]>=5:
        flag, divsor = FindN(primeList[i], primeList[i+1], 0)
        if flag:
            Nsum += primeList[i+1]*divsor
        else:
            print(primeList[i], None)
            
print(Nsum)
