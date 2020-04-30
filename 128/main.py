import sys
import math
sys.path.append("../Common")
import PrimeUtil

class Solution:
    def __init__(self):
        '''
        primeLimit = 1000000
        self.primeList = [0 for i in range(primeLimit)]
        self.primeList[1] = 1
        for i in range(2, primeLimit):
            if self.primeList[i] == 1:
                continue
            factor = 2
            while i * factor < primeLimit:
                self.primeList[i*factor] = 1
                factor += 1
        '''

    def GetNumber(self, n, m):
        if n == 1:
            return 1
        if n == 2:
            return m+1
        preSum = 1 + 6 * (n-1) * (n-2) / 2
        return preSum + m


    def FindDiffereences(self, n, m):
        bb = self.GetNumber(n, m)

        ret = []
        if n == 1:
            return [1,2,3,4,5,6]
        else:
            # top
            if m == 1:
                ret.append( math.fabs(self.GetNumber(n+1, m) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, 6*n) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, 6*(n-1)) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m) - bb)//1 )
            elif m < 1 + (n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-1) - bb)//1 )

            elif m == 1 + (n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+2) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-1) - bb)//1 )

            elif m < 1 + 2*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+2) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-2) - bb)//1 )
            
            elif m == 1+2*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+2) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+3) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-2) - bb)//1 )
            
            elif m < 1+3*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+2) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+3) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-2) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-3) - bb)//1 )
            
            elif m == 1+3*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+2) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+3) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+4) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-3) - bb)//1 )

            elif m < 1+4*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+3) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+4) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-3) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-4) - bb)//1 )
            
            elif m == 1+4*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+3) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+4) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+5) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-4) - bb)//1 )
            
            elif m < 1 + 5*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+4) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+5) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-4) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-5) - bb)//1 )
            
            elif m == 1+5*(n-1):
                ret.append( math.fabs(self.GetNumber(n+1, m+4) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+5) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+6) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                if m == 6*(n-1):
                    ret.append( math.fabs(self.GetNumber(n, 1) - bb)//1 )
                else:
                    ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n-1, m-5) - bb)//1 )
            else:
                ret.append( math.fabs(self.GetNumber(n+1, m+5) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n+1, m+6) - bb)//1 )

                ret.append( math.fabs(self.GetNumber(n, m-1) - bb)//1 )
                if m == 6*(n-1):
                    ret.append( math.fabs(self.GetNumber(n, 1) - bb)//1 )
                else:
                    ret.append( math.fabs(self.GetNumber(n, m+1) - bb)//1 )

                if m == 6*(n-1):
                    ret.append( math.fabs(self.GetNumber(n-1, 1) - bb)//1 )
                else:
                    ret.append( math.fabs(self.GetNumber(n-1, m-5) - bb)//1 )
                ret.append( math.fabs(self.GetNumber(n-1, m-6) - bb)//1 )

        return ret

    def Sol(self, n):
        find = 0

        x = 1
        m = 1
        while True:
            diffs = self.FindDiffereences(x,m)
            primes = 0
            for i in range(len(diffs)):
                if self.primeList[int(diffs[i])] == 0:
                    primes += 1
            #print(x,m, diffs, primes)
            if primes == 3:
                print(x,m,self.GetNumber(x,m),diffs)
                find += 1
            
            if find == n:
                return self.GetNumber(x,m)
            
            if x == 1:
                x += 1
                m = 1
            else:
                if m == 6*(x-1):
                    x+=1
                    m = 1
                else:
                    m+=1

        return "ssss"

    def FastSol(self, m):
        '''
        1) [6*(n-1)+1, 6*(n-1)-1, 6*(2*n-1)-1]    n,1   2+3*(n-1)*(n-2)
        2) [6*(n-1)-1, 6*(2*n-3)-1, 6*n-1]   n, m    1+3*n*(n-1)

        '''

        n = 2
        ct = 0
        while True:
            a = 6*(n-1)+1
            b = 6*(n-1)-1
            c = 6*(2*n-1)-1
            #if self.primeList[int(a)] == 0 and self.primeList[int(b)] == 0 and self.primeList[int(c)] == 0:
            if PrimeUtil.is_mill_rabin_prime(a) and PrimeUtil.is_mill_rabin_prime(b) and PrimeUtil.is_mill_rabin_prime(c):
                ct += 1
                print(2+3*(n-1)*(n-2))
            

            a = b
            b = 6*(2*n-3)-1
            c = 6*n -1
            #if self.primeList[int(a)] == 0 and self.primeList[int(b)] == 0 and self.primeList[int(c)] == 0:
            if PrimeUtil.is_mill_rabin_prime(a) and PrimeUtil.is_mill_rabin_prime(b) and PrimeUtil.is_mill_rabin_prime(c):
                ct += 1
                print(1+3*n*(n-1))
            
            if ct == m:
                break
            n+=1

        
s = Solution()

#print(s.FindDiffereences(3,1))
#print(s.Sol(10))
#print(s.Sol(50))

#print(s.FastSol(50))
print(s.FastSol(2000))



