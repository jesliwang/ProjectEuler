import sys
import math

class Solution:
    def __init__(self):
        self.dic = dict()

    def GetNumber(self, k):
        if k in self.dic:
            return self.dic[k]
        ret = 0
        if k >= 1 and k <= 55:
            ret =  (100003 - 200003*k + 300007*k*k*k)%1000000 - 500000
        elif k >= 56 and k <= 4000000:
            ret = (self.GetNumber(k-24) + self.GetNumber(k-55) + 1000000)%1000000-500000
        else:
            ret = 0

        self.dic[k] = ret
        return ret

    def Solve(self):
        width = 2000
        # 0 \ 1 | 2 /
        cur = [ [self.GetNumber(i+1) for j in range(3)] for i in range(width)] 
        
        lineSum = 0
        maxSum = self.GetNumber(1)
        for i in range(width):
            if lineSum <= 0:
                lineSum = self.GetNumber(i+1)
            else:
                lineSum += self.GetNumber(i+1)
            
            maxSum = max(maxSum, lineSum)

        maxSum = lineSum
        #print(cur,lineSum)
        for y in range(1, width):
        
            lineSum = 0
            nxt = [ [0 for j in range(3)]for i in range(width)]
            for i in range(width):
                posNum = self.GetNumber(width*y + i+1)
                
                if lineSum <= 0:
                    lineSum = posNum
                else:
                    lineSum += posNum
                maxSum = max(maxSum, lineSum)

                if i - 1 >= 0:
                    if cur[i-1][0] > 0:
                        nxt[i][0] = cur[i-1][0]+posNum
                    else:
                        nxt[i][0] = posNum
                else:
                    nxt[i][0] = posNum

                if cur[i][1] > 0:
                    nxt[i][1] = cur[i][1] + posNum
                else:
                    nxt[i][1] = posNum

                if i + 1 < width:
                    if cur[i-1][2] > 0:
                        nxt[i][2] = cur[i-1][2] + posNum
                    else:
                        nxt[i][2] = posNum
                else:
                    nxt[i][2] = posNum

                maxSum = max(maxSum, nxt[i][0])
                maxSum = max(maxSum, nxt[i][1])
                maxSum = max(maxSum, nxt[i][2])
        
            cur = nxt

        return maxSum



    

s = Solution()
#print(s.GetNumber(10))
#print(s.GetNumber(100))
print(s.Solve())