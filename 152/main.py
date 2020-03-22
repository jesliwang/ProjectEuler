'''
thanks https://euler.stephan-brumme.com/152/
这里遇到了4个问题。
1。 状态数太多，2^79次方。怎么简化。
2， 左右分裂成2部分后，2^40状态数还是太多了
3.  stephan-brumme 提供的方法，做式子内的简化。 dp方程当成优化参考，值得记录 a/b + 1/(x^2) =  a/b + b/(b*x*x). b 必须包含x的所有因式
4.  最终生成的时候，没有记录数字的重复生成
'''

import sys
sys.path.append("..")
from Common import PrimeUtil


def GetCommonMul(arr):
    _, primes = PrimeUtil.get_prime_dic_and_list(arr[len(arr)-1])
    ans = {}
    for i in range(len(arr)):
        t = arr[i]
        index = 0
        while t != 1 and index < len(primes):
            if t % primes[index] == 0:
                num = 0
                while t % primes[index] == 0:
                    num += 1
                    t //= primes[index]

                if primes[index] not in ans:
                    ans[primes[index]] = 1
                
                ans[primes[index]] = max(ans[primes[index]], num * 2)

            index += 1

    #print(ans)
    ret = 1
    for k, v in ans.items():
        ret *= pow(k, v)
    
    return ret

def GetSumP(m, p):
    ret = 0
    ansSet = set()
    mul = 1
    for i in range(1, m+1):
        mul *= i*i
    #print(mul,"====",m,p)
    for i in range(1, m+1):
        tN = set()
        #print(i)
        for v in ansSet:
            tp = v + mul//i//i
            #print(tp, tp%p)
            if(v+mul//i//i)%(p*p) == 0:
                return False
            tN.add(v+mul//i//i)
        ansSet.update(tN)
        ansSet.add(mul//i//i)

    return True

def GetMayKeys(n):
    _, primes = PrimeUtil.get_prime_dic_and_list(n)
    ret = []
    tR = set()
    for i in range(2, n+1):
        if i in primes and i * 2 > n:
            continue
        
        if i in primes:
            k = n//i
            #print(i, k)
            if k < i:
                if GetSumP(k, i):
                    for j in range(2, k+1):
                        tR.add(j*i)
                    continue

        
        ret.append(i)
    for v in tR:
        ret.remove(v)
    #print(ret)
    return ret


def GetWays(n):
    
    #print(CM)
    #print(CM/2==CM/4+CM/9+CM/16+CM/25+CM/49+CM/12/12+CM/15/15+CM/20/20+CM/28/28+CM/35/35)
    
    validArray = GetMayKeys(n)
    CM = GetCommonMul(validArray)
    print(validArray)
    print(len(validArray))
    ans = 0
    checkSet = {}
    
    for index in range(len(validArray)//2):
        #print(validArray[index])
        i = validArray[index]
        tSet = {}
        #print(i,'--------',len(checkSet),CM)

        for k,v in checkSet.items():
            tv = CM // i // i + int(k)
            #print(tv, CM//2)
            if tv == CM//2:
                ans += 1
            elif tv < CM//2:
                if tv not in tSet:
                    tSet[tv] = 0
                tSet[tv] = tSet[tv] + v
        
        for k,v in tSet.items():
            if k not in checkSet:
                checkSet[k] = 0
            checkSet[k] = checkSet[k]+v

        if CM//i//i not in checkSet:
            checkSet[CM//i//i] = 0
        checkSet[CM//i//i] = checkSet[CM//i//i]+1
        #print(i)

    #print('---------')
    checkSet2 = {}
    for index in range(len(validArray)//2, len(validArray)):
        #print(validArray[index])
        i = validArray[index]
        tSet = {}
        #print(i,'--------',len(checkSet),CM)

        for k,v in checkSet2.items():
            tv = CM // i // i + int(k)
            #print(tv, CM//2)
            if tv == CM//2:
                ans += 1
            elif tv < CM//2:
                if tv not in tSet:
                    tSet[tv] = 0
                tSet[tv] = tSet[tv] + v
            
        for k,v in tSet.items():
            if k not in checkSet2:
                checkSet2[k] = 0
            checkSet2[k] = checkSet2[k]+v

        if CM//i//i not in checkSet2:
            checkSet2[CM//i//i] = 0
        checkSet2[CM//i//i] = checkSet2[CM//i//i]+1

    #print(len(checkSet), len(checkSet2))
    for v in checkSet:
        if CM//2 - v in checkSet2:
            #print(v, checkSet[v], CM//2 - v, checkSet2[CM//2-v], v + CM//2 - v, CM//2)
            ans+=checkSet[v]*checkSet2[CM//2-v]

    return ans
    
#print(GetWays(45))
print(GetWays(80))
#print(GetWays(60))