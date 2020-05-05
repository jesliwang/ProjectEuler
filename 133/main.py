import sys
sys.path.append("../Common")
from TimeHelper import timethis

class Solution:
    def __init__(self):
        self.primes = []
        limit = 100000
        checkPrimes = [ 0 for i in range(limit)]

        for i in range(2, limit):
            if checkPrimes[i] == 0:
                self.primes.append(i)
                factor = 2*i
                while factor < limit:
                    checkPrimes[factor] = 1
                    factor+=i
        
    def check(self, number):
        start = 1
        facterLen = 1
        hashCheck = dict()
        while start != 0:
            if start in hashCheck:
                return False, 0
            hashCheck[start] = 1
            if start % number == 0:
                break
            start = (start % number)*10 + 1
            facterLen += 1
            
        
        return True, facterLen

    @timethis
    def Solve(self):
        sumAns = 0
        for i in range(len(self.primes)):
            flag, oneLen = self.check(self.primes[i])
            if flag:
                while oneLen % 2 == 0:
                    oneLen //=2
                while oneLen % 5 == 0:
                    oneLen //=5
                if oneLen == 1:
                    #print(self.primes[i])
                    continue
            
            sumAns += self.primes[i]
        
        return sumAns


s = Solution()
print(s.Solve())
                