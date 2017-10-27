import os, sys

# 0 perfect 1 more than 9, 2 not match
def checkCondition(a, b, c):
    dict = {}
    flag = True
    num = 0
    while a > 0:
        mm = a % 10
        a = a/10

        num += 1
        if dict.has_key(mm):
            flag = False

        dict[mm] = 1

    while b > 0:
        mm = b % 10
        b = b/10

        num += 1
        if dict.has_key(mm):
            flag = False

        dict[mm] = 1

    while c > 0:
        mm = c % 10
        c = c/10

        num += 1
        if dict.has_key(mm):
            flag = False

        dict[mm] = 1

    if num > 9:
        return 1
    elif flag and ( not dict.has_key(0) ) and len(dict) == 9:
        return 0
    else:
        return 2


asnDic = {}
for row in range(2, 10000):
    for col in range(2, 10000):
        ans = checkCondition(row, col, row*col)
        if ans == 0:
            asnDic[row*col] = 1
        elif ans == 1:
            break
        else:
            continue

sum = 0
for key,value in asnDic.items():
    sum += key

print sum
