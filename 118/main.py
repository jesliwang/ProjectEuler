import sys
sys.path.append("../Common")

from TimeHelper import timethis
import PrimeUtil

class Solution:
    def __init__(self):
        self.limit = 1000000
        self.ansDic = {}
        
        self.primeDict, self.primeList = PrimeUtil.get_prime_dic_and_list(self.limit)

    def GenerateSeq(self, CheckSet:set, pre:int) -> list:
        if len(CheckSet) == 0:
            return [pre]

        keyList = []
        for key in CheckSet:
            keyList.append(key)

        retList = []
        for i in range(len(keyList)):
            CheckSet.remove(keyList[i])
            retList.extend(self.GenerateSeq(CheckSet, pre*10+keyList[i]))
            CheckSet.add(keyList[i])

        return retList

    def GetSetNumber(self, number) -> int:
        if number in self.ansDic:
            return self.ansDic[number]
        #print(number)
        if number == 0:
            return 1
        tmp = number
        if tmp % 10 == 2:
            return 1 * self.GetSetNumber(number//10)
        if tmp % 2 == 0:
            return 0
        
        ret = 0

        group = 10
        while group < tmp:
            if tmp % group < self.limit:
                if tmp % group in self.primeList:
                    #print("group",tmp%group)
                    ret += self.GetSetNumber(tmp//group)
            else:
                if PrimeUtil.is_mill_rabin_prime(tmp % group):
                    #print("group",tmp%group)
                    ret += self.GetSetNumber(tmp//group)
            
            group *= 10

        if number < self.limit:
            if number in self.primeList:
                ret += 1
        else:
            if PrimeUtil.is_mill_rabin_prime(number):
                #print("sss=",number)
                ret += 1
        
        self.ansDic[number] = ret
        return ret

    @timethis
    def Solve(self) -> int:
        
        keySet = set()
        for i in range(1,10):
            keySet.add(i)

        CheckList = self.GenerateSeq(keySet, 0)

        ret = 0

        for i in range(len(CheckList)):
            setNumber = self.GetSetNumber(CheckList[i])
            ret += setNumber

        return ret

    def IsPrime(self, number):
        if number < self.limit:
            return number in self.primeList
        else:
            return PrimeUtil.is_mill_rabin_prime(number)


    def DPS(self, numList:list, idx:int) ->set:
        cur = 0
        ret = set()

        for i in range(idx, len(numList)):
            cur = cur*10 + numList[i]
            if self.IsPrime(cur):
                if i != len(numList) - 1:
                    after = self.DPS(numList, i+1)
                    if len(after) > 0:
                        for key in after:
                            keyList = list(key)
                            keyList.append(cur)
                            keyList.sort()
                            ret.add(tuple(keyList))

                else:
                    tp = (cur,)
                    ret.add(tp)
        

        return ret
                


    # 1 2 3 7 9
    def GetMaySet(self, number):
        ansSet = set()

        numList = []
        tmp = number
        while tmp > 0:
            numList.append(tmp%10)
            tmp//=10
        numList.reverse()

        return self.DPS(numList, 0)



    @timethis
    def FastSolve(self)->int:
        keySet = set()
        for i in range(1,10):
            keySet.add(i)

        CheckList = self.GenerateSeq(keySet, 0)

        ansSet = set()
        for i in range(len(CheckList)):
            if CheckList[i] % 2 == 0 and CheckList[i] %10 != 2:
                continue

            if CheckList[i] % 5 == 0:
                continue
            
            getSet = self.GetMaySet(CheckList[i])
            #print(CheckList[i])
            #if len(getSet) > 0:
            #    print(CheckList[i], getSet)
                #break
            ansSet = ansSet.union(self.GetMaySet(CheckList[i]))

        return len(ansSet)



s = Solution()
#print(s.GetSetNumber(254789631))
#print(s.GetSetNumber(713825649))
#print(s.Solve())
print(s.FastSolve())
#print(s.GetMaySet(254789631))