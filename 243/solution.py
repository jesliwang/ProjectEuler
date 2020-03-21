import sys, os
import random
import heapq

class Solution:
    def is_prime(self, num, primeList):
        #print(num)
        if len(primeList) == 0:
            return True
        
        for v in primeList:
            if num % v == 0 :
                return False
        
        return True
        
    def GetNumer(self, num, primeList):
        findList = []
        numer = 0
        for i in range(len(primeList)):
            if num % primeList[i] == 0:
                numer += int(num/primeList[i])
                slen = len(findList)
                findList.append(primeList[i])
                for v in range(slen):
                    nt = findList[v] * primeList[i] * (-1)
                    numer += int(num/nt)
                    findList.append(nt)
                
        return numer

    def GetSmallestDen(self, numer, denomi):
        primeList = []
        testNumber = 2
        while True:
            if self.is_prime(testNumber, primeList):
                if (testNumber - 1) * denomi < (testNumber-1) * numer:
                    return testNumber
                
                primeList.append(testNumber)
            else:
                nm = self.GetNumer(testNumber, primeList)
                if (testNumber - nm) * denomi < (testNumber-1) * numer:
                    #print((testNumber - nm),"===", testNumber)
                    return testNumber
                
            testNumber += 1

    def mulMod(self, a:int, b:int, n:int) -> int: # a*b % n
        ans = 0
        a %= n
        while b > 0:
            if b&1 > 0:
                ans = (ans + a) % n
            
            b //= 2
            a = (a + a) % n
        
        return ans % n

    def powMod(self, a:int, b:int, n:int) ->int: # a^b % n
        ans = 1
        a %= n
        while b > 0:
            if b&1 > 0:
                ans = self.mulMod(a, ans, n)
            
            b //= 2
            a = self.mulMod(a, a, n)

        return ans % n

    #a^(p−1)=1(mod p)
    #x^2 = 1(mod p)  
    def miller_rabin(self, n:int, times = 50):
        if n == 2 or n ==3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        u:int = n - 1
        # n - 1 = 2^s * p
        s = 0
        while( not (u & 1) ):
            s += 1
            u >>= 1

        for _ in range(times):
            a = random.randint(2, n - 1)
            t = self.powMod(a, u, n)
            for _n in range(s):
                p = self.mulMod(t, t, n)
                if p == 1 and t != 1 and t != n-1:
                    return False
                t = p

            if t != 1:
                return False

        return True
        
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a%b)  
      

    def pollard_rho(self, n:int, m:int):
        #print(n,m)
        y = random.randint(1, n-1)
        i = 1
        k = 2
        x = y
        while True:
            x = self.mulMod(x, x, n) + m
            d = self.gcd(y - x, n)
            if d > 1 and d < n:
                return d
            
            #print(y,x,"=====")
            if y == x:
                return n
            i += 1
            if k == i:
                y = x
                k <<= 1

    
    def FindFactor(self, n:int, c, mp:set):
        if n == 1:
            return
        
        if self.miller_rabin(n):
            mp.add(n)
            return

        t = n
        while t >= n:
            t = self.pollard_rho(n, c)
            c = c-1
        
        self.FindFactor(t, c, mp)
        self.FindFactor(n//t, c, mp)

    def FactorSet(self, n:int):
        target = n
        tt = random.randint(1, target - 1)
        ans = set()
        s.FindFactor(target, tt, ans)
        return ans
    
    def GetNumerBig(self, num, primeList):
        findList = []
        numer = 0
        for i in range(len(primeList)):
            if num % primeList[i] == 0:
                numer += int(num/primeList[i])
                slen = len(findList)
                findList.append(primeList[i])
                for v in range(slen):
                    nt = findList[v] * primeList[i] * (-1)
                    numer += int(num/nt)
                    findList.append(nt)

        return numer

    def GetSmallestDenBig(self, numer, denomi):
        testNumber = denomi
        while True:
            
            primeList = list(self.FactorSet(testNumber))

            nm = self.GetNumerBig(testNumber, primeList)
            #print(testNumber - nm,testNumber-1)
            if (testNumber - nm) * denomi < (testNumber-1) * numer:
                print((testNumber - nm),"===", testNumber)
                return testNumber
                
            testNumber = testNumber +1

    def FindMinForSet(self, cc:set):
        mm = 1
        for v in cc:
            mm *= v
        
        de = self.GetNumer(mm, list(cc))
        return de,mm
    
    def FindAns(self, numer, denomi, testSet:set):

        tNumer, tDenomi = self.FindMinForSet(testSet)
        if (tDenomi - tNumer) * denomi < tDenomi * numer:
            # 可能有值
            hq = [tDenomi]
            heapq.heapify(hq)
            while len(hq) > 0:
                test = heapq.heappop(hq)
                #print(list(testSet))
                nm = self.GetNumer(test, list(testSet))
                if (test - nm) * denomi < (test-1) * numer:
                    return True, test
                
                for prime in testSet:
                    heapq.heappush(hq, test * prime)
        return False, None      

    def FindSmall(self, numer, denomi):
        primeList = [3,5,7,11,13,17,19,23,29,31,37,41,43,47]
        myset = set()
        myset.add(2) 
        findNumer = 10000000000
        for i in range(len(primeList)):
            myset.add(primeList[i])

            flag, num = self.FindAns(numer, denomi, myset)
            if flag and num < findNumer:
                findNumer = num
        return findNumer




s = Solution()
#print(s.FindSmall(4,10))
mayAns = s.FindSmall(15499, 94744)
print(mayAns)
print(s.FactorSet(mayAns))
#print(s.FindAns(4,10))
#print(s.GetSmallestDenBig(4, 10))
#print(s.GetSmallestDenBig(15499, 94744))
#print(s.miller_rabin(100))




        


