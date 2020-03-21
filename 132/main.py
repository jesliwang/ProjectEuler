import sys
sys.path.append("..")
from Common import PrimeUtil

# 测试素数多少个1可以形成循环

def CanPrimeBeFactor(n):
    uni = {}
    now = 1
    index = 1
    while True:
        if now % n == 0:
            return True, index
        else:
            if now in uni:
                return False, None
            
            uni[now] = True
            index += 1
            
            now = now%n
            now = now*10 + 1

_, primes = PrimeUtil.get_prime_dic_and_list(1000000)
#print(primes)

target = 1000000000

ans = 0
cc = 0
for i in range(len(primes)):
    flag, n = CanPrimeBeFactor(primes[i])
    #print(i,primes[i],flag,n)
    if flag and target % n == 0:
        ans += primes[i]
        cc += 1
        print(cc,primes[i])
    #print(cc)
    if cc >= 40:
        break

print(ans)


#print(CanPrimeBeFactor(2))
#print(CanPrimeBeFactor(3))
#print(CanPrimeBeFactor(7))
#print(CanPrimeBeFactor(11))
#print(CanPrimeBeFactor(41))
#print(CanPrimeBeFactor(271))
#print(CanPrimeBeFactor(9091))

