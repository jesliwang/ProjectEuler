import sys
import math

class Solution:
    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a%b)

    def GetPeriod(self, n):
        blockList = list()
        y = 1
        a = ((math.sqrt(n))/y)//1
        x = a

        while (a,x,y) not in blockList:     
            blockList.append((a,x,y))
            # y / (s_n - a)
            na = (y / (math.sqrt(n)-x))//1
            ny = n - x*x
            # s_n + a - y*na
            x = ny*na - x*y
            a = na
            md = y
            y = ny
            #print(a,x,y)
            #break
            #md = self.gcd(x,y)
            x = x//md
            y = y//md
            #print(a,x,y)

        
        return len(blockList) - blockList.index((a,x,y))
        
        #return blockList

    def Solve(self, n):
        ret = 0
        for i in range(2,n+1):
            if pow(math.sqrt(i)//1,2) == i:
                continue
            period = self.GetPeriod(i)
            #print(i,period)
            if period % 2 == 1:
                ret +=1
        
        return ret



s = Solution()
#print(s.GetPeriod(23))
#print(s.GetPeriod(13))
#print(s.GetPeriod(7))
#print(s.GetPeriod(8))
#print(s.Solve(13))
print(s.Solve(10000))

