import sys
sys.path.append("..")
from Common import PrimeUtil 

def powByMod(num, n, mod):
    pre = num % mod
    m = n
    ret = 1
    while m > 0:
        if m % 2 == 1:
            ret = (pre*ret)%mod
        pre = (pre * pre) % mod
        #print(pre,ret)
        m //= 2
    return ret


limit = 1000000
#MOD = pow(10,9)//1
MOD = pow(10,10)//1
_, primeList = PrimeUtil.get_prime_dic_and_list(limit)

for index in range(len(primeList)):
    mm = primeList[index] * primeList[index]
    tmp = (powByMod(primeList[index] - 1, index + 1, mm) + powByMod(primeList[index] + 1, index + 1, mm))%mm
    if tmp > MOD:
        print((index+1), primeList[index])
        break