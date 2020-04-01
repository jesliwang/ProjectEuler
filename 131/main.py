'''
n^3 + n^2*p = n^2(n+p) = x*3   2(ln(n) + l(n+p))=3ln(x)
2^3    2^2 * 3
p + m = x^3
(p+m)*m^2 = x^3*m^2

(p+m+1)=(x+1)^3

n^3+n^2(3*x^2+3*x+1)
n^2*(n+3*x^2+3*x+1)

run 15mini

以下可以优化
https://en.wikipedia.org/wiki/Cuban_prime

'''
import sys
import math
sys.path.append("..")
from Common import PrimeUtil

limit = 1000000
_, primeList = PrimeUtil.get_prime_dic_and_list(limit)

def Test(n, p, pList):
    may = pow(n,3) + pow(n,2) * p

    return may == pow(round(pow(may,1/3)),3)
    


ans = 0
for i in range(len(primeList)):
    #print(primeList[i])
    n = math.ceil(pow(primeList[i], 1/3))
    #maxN = primeList[i]+n
    maxN = n*n#primeList[i]*primeList[i]
    
    #print(n,maxN)
    while n <= maxN:
        tmp = pow(n,3) - primeList[i]
        if Test(tmp,primeList[i],primeList):
            print(primeList[i])
            ans += 1
            break
        n=n+1

print("ans=",ans)

    

