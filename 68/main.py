'''
10 + a + b =  x + b + c = y + c + d = z + d+ e = w + e + a

10 + a = x + c
10 + b = w + e
10 a b 


'''

import sys

class Solution:
    def GenNext(self, lt:list):
        ll = len(lt)
        while ll > 1:
            fg = True
            for i in range(lt[ll-1] + 1, 10):
                if i not in lt:
                    fg = False
                    del lt[ll-1]
                    lt.append(i)
                    break
            
            if fg:
                del lt[ll-1]
                ll -= 1
            else:
                break
    
    def Append(self, lt:list):
        for i in range(1, 10):
            if i not in lt:
                lt.append(i)
                break

    def ConvertStr(self, lt:list):
        ring = [(lt[0],lt[1],lt[2]), (lt[3],lt[2],lt[4]),(lt[5],lt[4],lt[6]),(lt[7],lt[6],lt[8]),(lt[9],lt[8],lt[1])]
        
        while True:
            flag = True
            for i in range(1, 5):
                if ring[i][0] < ring[0][0]:
                    flag = False
                    for j in range(i):
                        ring.append(ring[j])
                    tmp = i
                    while tmp > 0:
                        del ring[0]
                        tmp -=1
                    break
            if flag:
                break

        retStr = ""
        for i in range(5):
            retStr += str(ring[i][0]) + str(ring[i][1]) + str(ring[i][2])

        return retStr


    def Solve(self):
        ori = [10]
        ansStr = []
        for i in range(1,10):
            ori.append(i)
            # 3,5,7,9,10
            while len(ori) > 1:
                if len(ori) == 5:
                    if ori[0]+ori[1]+ori[2] != ori[3] + ori[2]+ ori[4] :
                        self.GenNext(ori)
                    else:
                        self.Append(ori)
                elif len(ori) == 7:
                    if ori[0]+ori[1]+ori[2] != ori[5] + ori[4]+ ori[6] :
                        self.GenNext(ori)
                    else:
                        self.Append(ori)
                elif len(ori) == 9:
                    if ori[0]+ori[1]+ori[2] != ori[7] + ori[6]+ ori[8] :
                        self.GenNext(ori)
                    else:
                        self.Append(ori)
                elif len(ori) == 10:
                    if ori[0]+ori[1]+ori[2] != ori[9] + ori[8]+ ori[1] :
                        self.GenNext(ori)
                    else:
                        ansStr.append(self.ConvertStr(ori))
                        self.GenNext(ori)
                else:
                    self.Append(ori)

        ansStr.sort()
        print(ansStr)
        return ansStr[len(ansStr)-1]
        


s=Solution()
print(s.Solve())