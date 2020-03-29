'''
      ab
xxxxxxxx
---------------
      
1 1
3 7
7 3
9 9

基于一个猜想: 如果有n位，则必须要循环n次计算，并且不重复。所以从n开始计算就好了

'''
import sys


def gcd(a, b):
    return a if b == 0 else gcd(b, a%b)

def GetRepunit(n):
    left = 0
    
    matchSet = dict()
    matchSet[1]=1
    tmp = (1,1)
    while tmp[0] < 10000000000:
        tmp = (tmp[0]*10+1, tmp[1]+1)
        matchSet[tmp[0]] = tmp[1]
    
    len = 0
    while left not in matchSet:
        for i in range(0,10):
            if (n*i + left )%10 == 1:
                #print(len,i,left)
                left = ((n*i) + left)//10
                break
        len = len + 1
        if left == 0:
            break
    
    if left == 0:
        return len
    return len + matchSet[left]

#limit = 10
limit = 1000000

index = limit
while True:
    if gcd(index, 10) == 1:
        #print(index)
        if GetRepunit(index) >limit:
            print(index)
            break
    
    index += 1
#print(GetRepunit(41))


