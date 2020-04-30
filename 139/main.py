import sys
import math

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    def tri_gcd(self, a,b,c):
        return self.gcd(self.gcd(a,b),c)
    
    def combine(self, a, b, c):
        return (min(a,b), max(a,b),c)

    def Solve(self, limit):
        n = 1
        m = 2

        ret = 0

        check = set()
        #while n*n + (n+1)*(n+1) < limit:
        while 2*n*(n+1)+2*(n+1)*(n+1) < limit:
            while 2*n*m + 2*m*m < limit:
                a = 2*n*m
                b = m*m -n*n
                c = m*m + n*n

                cm = self.tri_gcd(a,b,c)
                if cm != 1:
                    a//=cm
                    b//=cm
                    c//=cm

                if self.combine(a,b,c) not in check:
                    check.add(self.combine(a,b,c))
                    if c % math.fabs(a-b) == 0:
                        #print(self.combine(a,b,c),':', c%math.fabs(a-b))
                        ret += (limit-1)//(a+b+c)

                m+=1
            
            n+=1
            m=n+1
        #print(check)
        return ret

s = Solution()
#print(s.Solve(1000000))
#print(s.Solve(100000000))
print(s.Solve(100000000))