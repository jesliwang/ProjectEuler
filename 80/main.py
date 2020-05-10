import sys
import math

class Solution:


    def GetSqurt(self, number):
        nowNumber  = int(number)
        cur = int(nowNumber)

        cur = int(math.sqrt(nowNumber))
        if cur * cur == nowNumber:
            return False, 0, 0
        
        for i in range(100):
            tmp = cur * 10
            nowNumber *= 100
            for j in range(10):
                check = tmp + j
                if check * check <= nowNumber:
                    cur = check
                else:
                    break
            
        ret = 0
        helper = str(cur)
        for i in range(100):
            ret += int(helper[i])
        return True, ret, cur
    
    def Solve(self):
        ret = 0
        flag = False
        num = 0
        holder = 0
        for i in range(1,101):
            flag, num, holder = self.GetSqurt(i)
            if flag:
                ret += num
        
        return ret


s = Solution()
#print(s.GetSqurt(99))
#print(s.GetSqurt(2))
print(s.Solve())
