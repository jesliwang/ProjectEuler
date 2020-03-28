import sys

def IsPalindromic(number):
    ns = str(number)
    begin = 0
    end = len(ns) -1
    while begin <= end:
        if ns[begin] != ns[end]:
            return False
        begin += 1
        end -= 1
    return True

#limit = 1000
limit = pow(10,8)

ansSet = set()

start = 1
ans = 0
while start * start < limit:
    now = start + 1
    nowSum = start * start + now*now
    while nowSum < limit:
        if IsPalindromic(nowSum):
            #print(nowSum, start, now)
            if nowSum not in ansSet:
                ans += nowSum
                ansSet.add(nowSum)
        now = now + 1
        nowSum += now*now
    
    start += 1
print("ans=", ans)
            