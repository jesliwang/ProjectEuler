import sys
import math

class Solution:
    def Solve(self, limit):
        # a = 2mn b=mm-nn c = mm+nn        
        m = 2
        ansSet = set()
        while 2*m*m < limit:
            n = 1
            while n < m and 2*(m*m+n*n) < limit:
                c = m*m+n*n
                a = 2*m*n
                b = m*m-n*n
                if math.fabs(c-2*a) == 1 and 2*(a+c)<limit:
                    ansSet.add((2*c,2*a))
                
                if math.fabs(c-2*b) == 1 and 2*(b+c)<limit:
                    ansSet.add((2*c,2*b))
                n+=1
            m+=1
        
        #print(ansSet)
        sumRet = 0
        for item in iter(ansSet):
            sumRet += item[0] + item[1]
        return sumRet

s = Solution()
#print(s.Solve(17))
print(s.Solve(1000000000))