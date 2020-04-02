import sys

'''
4(width - 1) + 4(width-3) + 4(width-4)
32 = 4 * 8
3 + 5 + 7 + 9

n + n - 2 + n - 4 + ... + n-2*k = f
(k+1)n -2(1+2+..+k)=f
(k+1)n = f + (k+1)*k
n =  

40 =  11   
48 = 13
48 = 8,6 = 28,20
48 = 7,5,3 = 24,16, 8

84 = 22
84 = 10, 8, 6 = 36, 28, 20 = 84


4n + 4(n-2) + 4(n-4) + ... + 4(n-2*k) = limit
4n - 4*2(1+2+...+k) = limit
n - 2(1+2+...+k) = limit //4
(k+1) n = limit //4 + k * (k+1)
n = (limit//4 + m * (m-1)) / m
'''


#blocks = 100
#limit = 1000000

nDic = dict()
for limit in range(1, 1000000):
    ans = 0
    if limit >= 8 and limit % 4 == 0:
        tmp = limit // 4
        minus = 1
        fn = (tmp + minus * (minus - 1)) // minus
        #print(limit,fn,"...")
        while fn>= 2*minus:
            if (tmp + minus * (minus - 1)) % minus == 0:
                ans += 1
            minus += 1
            fn = (tmp + minus * (minus - 1)) // minus
            
    if ans not in nDic:
        nDic[ans] = 0
    nDic[ans] = nDic[ans] + 1

print(nDic[15])

one2ten = 0
for i in range(1,11):
    if i in nDic:
        one2ten += nDic[i]
print(one2ten)
    