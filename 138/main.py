# 勾股数 https://baike.baidu.com/item/%E5%8B%BE%E8%82%A1%E6%95%B0/2674064?fr=aladdin
import math

n = 1
ct = 0
ans = 0
while True:

    m2n = 5*n*n+1
    m2nsqrt = math.sqrt(m2n)//1
    if m2nsqrt * m2nsqrt == m2n:
        m = m2nsqrt + 2*n
        a = 2*m*n
        b = m*m - n*n
        c = m*m +n *n
        print(a,b,c)
        ans += c
        ct += 1
    
    m2n = 5*n*n-1
    m2nsqrt = math.sqrt(m2n)//1
    if m2nsqrt * m2nsqrt == m2n:
        m = m2nsqrt + 2*n
        a = 2*m*n
        b = m*m - n*n
        c = m*m +n *n
        print(a,b,c)
        ans += c
        ct+=1

    if ct >= 12:
        break
    n += 1

print('ans=',ans)