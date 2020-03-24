'''
1 2 5 10
1,1   2/10   2
1,2   3/10   2
1,5   6/10   3
1,10  11/10  2
2,2   4/10   1
2,5   7/10   2
2,10  12/10 1/15, 1/3  2
5,5   10/10  2
5,10  15/10 5/10 1 3
10,10 20/10 5/10
      10*(1+1) 1 2 

1,1  *2 * 5 *2*5
1,2  *5
1,5  *2
1,10  
2,5

'''''

def GetAnsSum(m ,n, pre, mul):
    ret = set()
    for i in range(m+1):
        for j in range(n+1): 
            ll = mul//pre
            rr = mul//pre//pow(2,i)//pow(5,j)
            mayKey = (min(ll,rr), max(ll,rr), (pow(2,i)*pow(5,j)+1)*pre)
            #mayKey = (1, pow(2,i)*pow(5,j), 1+pow(2,i)*pow(5,j))
            ret.add(mayKey)
    return ret

def GetSplitSum(m, n, pre,mul):
    #print("=======")
    ret = set()
    for i in range(1, m+1):
        for j in range(1, n+1):
            #print(pre,":", i,j, (pow(2,i)+pow(5,j))*pre)
            #ret.add((pow(2,i)+pow(5,j))*pre)
            lmin = min(mul//pre/pow(2,i), mul//pre//pow(5,j))
            lmax = max(mul//pre//pow(2,i), mul//pre//pow(5,j))
            mayKey = (lmin, lmax, (pow(2,i)+pow(5,j))*pre)
            ret.add(mayKey)
    return ret

def slution(n):
    #ans = 0
    maySet = set()
    for x in range(n+1):
        for y in range(n+1):
            #1. 都在一侧 
            maySet.update(GetAnsSum(n-x,n-y, pow(2,x)*pow(5,y),pow(10,n)))
            #ans += (n-x+1)*(n-y+1)
            #2. 两边分开
            #ans += (n-x) * (n-y)
            maySet.update(GetSplitSum(n-x, n-y, pow(2,x)*pow(5,y),pow(10,n)))

    #print(maySet)

    nSet = set()
    for v in maySet:
        nSet.add(v)
        nSet.add((v[0]*v[2], v[1]*v[2], 1))
        p = v[2]
        i = 2
        #print("=====")
        #print(v)
        while i*i <= p:
            if p%i == 0:
                #print(i)
                nSet.add((v[0]*i, v[1]*i, p//i))
                nSet.add((v[0]*(p//i), v[1]*(p//i), i))
                #print(nSet)
            i += 1
        
    

    # 约数
    return len(nSet)



if __name__=="__main__":
    ans = 0
    for i in range(9):
    #for i in range(1):
       # print(i)
        #print(slution(i+1)*2)
        #print(cal(i+1)*2)
        ans += slution(i+1)
    print(ans)


