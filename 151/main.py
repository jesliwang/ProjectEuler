'''
state A2,A3,A4,A5

只有1个的概率
1 5
2 4
4 3
8 2

4 * 

1/3    +     1/4

       +     1/5

1/3 *1/ 4 * 2 + 1/3*1/4*2


'''

import sys

class Solution:
    def __init__(self):
        self.found = dict()
        self.found[1] = {0:1}

    def GetKey(self, lt, index, appendList):
        nList = list()
        for i in range(len(lt)):
            if i != index:
                nList.append(lt[i])
        for i in range(len(appendList)):
            nList.append(appendList[i])
        nList.sort()
        key = 0
        for i in range(len(nList)):
            key = key * 10 + nList[i]
        return key

    def CutDown(self, n):
        if n == 1:
            return []
        elif n == 2:
            return [1]
        elif n == 3:
            return [1,2]
        elif n == 4:
            return [1,2,3]
        else:
            return []

    def GetFind(self, n):
        if n in self.found:
            return self.found[n]
        
        convert = []
        tmp = n
        while tmp > 0:
            convert.insert(0, tmp % 10)
            tmp //=10
        
        pre = 0
        if len(convert) == 1:
            pre = 1
        
        ansSet = {}

        for i in range(len(convert)):
            k = self.GetKey(convert, i, self.CutDown(convert[i]))
            y = self.GetFind(k)

            if len(y) != 0: 
                for number,val in y.items():
                    if number + pre not in ansSet:
                        ansSet[number+pre] = 0

                    ansSet[number+pre] = ansSet[number+pre] + val /len(convert)
            
                
            
        
        self.found[n] = ansSet

        return self.found[n]

    def GetAns(self, n):
        dic = self.GetFind(n)
        ans = 0
        for k,v in dic.items():
            ans += k*v
        return ans


s = Solution()
print('%.6f' % s.GetAns(1234))


