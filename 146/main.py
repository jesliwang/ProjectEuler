
import sys
sys.path.append("../Common")
import PrimeUtil


class Solution:
    def GetSum(self,limit):
        ret = 0
        appendSet = [1,3,7,9,13,27]
        ccSet = [11,17,19,21,23]
        for i in range(0,limit, 10):
            if i % 3 == 0 or i % 7 == 0 or i % 13 == 0:
                continue
            pw = i*i
            if pw % 2 == 1:
                continue
            
            if pw % 10  == 5 or pw%10 == 4 or pw%10 == 2 or pw%10 == 8 or pw%10 == 6:
                continue
            
            flag = True
            for j in range(len(appendSet)):
                if not PrimeUtil.is_mill_rabin_prime(pw+appendSet[j]):
                    flag = False
                    break

            if flag:
                for j in range(len(ccSet)):
                    if PrimeUtil.is_mill_rabin_prime(pw+ccSet[j]):
                        flag = False
                        break

            if flag:
                ret += i
            
        return ret
    

s = Solution()
#print(s.GetSum(1000000))
print(s.GetSum(150000000))
                       