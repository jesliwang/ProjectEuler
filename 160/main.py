'''
1 3 7 9 11 13 17 19 21 23 27 29

1 3 7 9 11 13(2,6,14,18,22,26)

1 3 7(4,12,28)

1 3 (8, 24)

1(16)

1(20)

1,3(10,30)
'''

class Solution:
    def PowMod(self, n, m, mod):
        ret = 1
        tmp = m
        mul = n%mod
        while tmp > 0:
            if tmp % 2 == 1:
                ret = (ret * mul) % mod
            
            tmp //= 2
            mul = (mul * mul) % mod

        return ret
        
    def CoPrime(self, n, m, flag = True):
        #print(n,m)
        tmp = n
        state = tmp // m
        mod = tmp % m
        ret = 1
        for i in range(1, m):
            if i % 2 == 0 or i % 5 == 0:
                continue
            
            ret = (ret * Solution.PowMod(self, i, state, m))%m

        
        for i in range(1, mod+1):
            if i % 2 == 0 or i % 5 == 0:
                continue

            ret = (ret * i)%m

        if not flag:
            return ret
        sk = list()
        sk.append(n)
        tmp = n
        while tmp // 2> 0:
            tmp//=2
            sk.append(tmp)
            ret = (ret * Solution.CoPrime(self,tmp,m, False))%m


        while len(sk) > 0:
            tmp = sk[len(sk)-1]
            sk.pop(len(sk)-1)
            while tmp // 5 > 0:
                #print("--",tmp)
                tmp //= 5
                ret = (ret * Solution.CoPrime(self,tmp,m,False))%m
            

        return ret


    def SolveTwos(self, n, m):
        ret = 1
        tmp = n
        while tmp > 0:
            state = tmp // m
            mod = tmp % m
            for i in range(1, m):
                if i % 2 == 0 or i % 5 == 0:
                    continue
                
                #print(ret, i,state,Solution.PowMod(self, i, state, m))
                
                ret = (ret * Solution.PowMod(self, i, state, m))%m

            
            for i in range(1, mod):
                if i % 2 == 0 or i % 5 == 0:
                    continue
                print('---',i,ret,mod)
                ret = (ret * i)%m
                #print(i,ret)
            
            
            tmp //=2
        print('2=',ret)
        return ret
    
    def SolveFives(self, n, m):
        ret = 1
        tmp = n
        while tmp > 0:
            state = tmp // m
            mod = tmp % m
            for i in range(1, m):
                if i % 2 == 0 or i % 5 == 0:
                    continue
                ret = (ret * Solution.PowMod(self, i, state, m))%m
            
            for i in range(1, mod):
                if i % 2 == 0 or i % 5 == 0:
                    continue
                ret = (ret * i)%m
            
            tmp //=5
        print('5=',ret)
        return ret


    def Solve(self, n, m):
        fivesN = 0
        tmp = n
        while tmp > 0:
            tmp = tmp//5
            fivesN += tmp
        
        twosN = 0
        tmp = n
        while tmp > 0:
            tmp = tmp//2
            twosN += tmp
        
        twosN -= fivesN

        ret = 1
        ret *= Solution.PowMod(self, 2,twosN, m)
        #print(ret)
        #ret = (ret * Solution.SolveTwos(self, n, m))%m
        #ret = (ret*Solution.SolveFives(self, n//5, m))%m
        #print('--------')
        ret = (ret * Solution.CoPrime(self, n, m))%m
        return ret

    
s = Solution()
#print(s.Solve(20,100000))
#print(s.Solve(100001, 100000))
print(s.Solve(pow(10,12),pow(10,5)))

