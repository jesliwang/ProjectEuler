import os, sys

facterDic = { 0:1,
1:1}

for index in range(2,10):
    facterDic[index] = index * facterDic[index-1]

def curNumber(num):
    tmp = num
    sum = 0
    while tmp > 0 and sum < num:
        sum += facterDic[tmp%10]
        tmp/=10

    if 0 == tmp and sum == num:
        return True
    else:
        return False

lim = 1000000
ans = 0
for index in range(10, lim):
    if curNumber(index):
        ans += index
        print index

print "ans=", ans
