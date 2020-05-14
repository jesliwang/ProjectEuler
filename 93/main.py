import sys
import copy

class Solution:

    def GenerateAllSeq(self, nums:list):
        cur = []
        for i in range(len(nums)):
            if len(cur) == 0:
                cur.append([nums[i]])
            else:
                nt = []
                for j in range(len(cur)):
                    item = cur[j]
                    for x in range(len(item)):
                        nw = copy.deepcopy(item)
                        nw.insert(x, nums[i])
                        nt.append(nw)

                    nw = copy.deepcopy(item)
                    nw.append(nums[i])
                    nt.append(nw)
                
                cur = nt
        return cur
    
    def Cal(self, atom:list):
        
        strList = [ '(({3}{0}{4}){1}{5}){2}{6}',
            '({3}{0}{4}){2}({5}{1}{6})',
            '({3}{1}({4}{0}{5})){2}{6}',
            '{3}{2}({4}{1}({5}{0}{6}))']
        f = ['+','-','*','/']

        ret = set()
        for x in range(4):
            for y in range(4):
                for z in range(4):
                    for i in range(len(strList)):
                        try:
                            num = eval( strList[i].format(f[x],f[y],f[z], atom[0], atom[1], atom[2], atom[3]) )
                            if num >= 1 and num == num//1:
                                ret.add(num)
                        except:
                            pass
                        
        
        return ret
                    
                    
    def FindMax(self, a, b, c, d):

        nums = [a,b,c,d]
        checkList = self.GenerateAllSeq(nums)
        
        ret = set()
        for x in range(len(checkList)):
            ret.update(self.Cal(checkList[x]))

                
        retList = list(ret)
        retList.sort()

        cur = -10
        for i in range(len(retList)):
            if retList[i] == i+1:
                cur = i
        return cur+1

    def Solve(self):
        cur = [1,2,3,4]
        mx = 28
        start = 1
        limit = 10
        for x in range(start,limit):
            for y in range(x+1, limit):
                for z in range(y+1, limit):
                    for m in range(z+1, limit):
                        nt = [x,y,z,m]
                        tmp = self.FindMax(x,y,z,m)
                        if tmp > mx:
                            cur = nt
                            mx = tmp
        return mx, cur


s = Solution()
#print(s.FindMax(1,2,3,4))
#print(s.FindMax(1,2,5,6))
print(s.Solve())