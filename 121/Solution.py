
class Solution:
    def gcd(self, a:int, b:int):
        #print(a,b)
        return a if b == 0 else self.gcd(b, a%b)

    def minDown(self, dn):
        while self.gcd(dn[0],dn[1]) != 1:
            t = self.gcd(dn[0], dn[1])
            dn = (dn[0]//t, dn[1]//t)
        
        return dn

    def GetAns(self, n):
        if n == 1:
            return 1,2

        pre = [(1,2), (1,2)]
        for i in range(2, n+1):
            nxt = []
            for x in range(i+1):
                now = i+1
                s1 = (0, 1)
                if x < len(pre):
                    s1 = (pre[x][0]*(now-1), pre[x][1]*now)
                
                s2 = (0, 1)
                if x > 0:
                    s2 = (pre[x-1][0], pre[x-1][1]*now)

                #print(x,s1,s2)
                s = (s1[0]*s2[1]+s1[1]*s2[0], s1[1]*s2[1])
                s = self.minDown(s)
                nxt.append(s)

            pre = nxt    
            #print(i, pre)    

        ans = (0, 1)
        for i in range(n//2 + 1, n+1):
            ans = (ans[0]*pre[i][1]+ans[1]*pre[i][0], ans[1]*pre[i][1])
            #print(pre[i])

        return self.minDown(ans)


s = Solution()
ff = s.GetAns(4)
print(ff)
print(ff[1]/ff[0])
ff = s.GetAns(15)
print(ff)
print(ff[1]/ff[0])



                
