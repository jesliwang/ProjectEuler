'''
此问题方法都知道，最终结果卡在了纠结计算方式上，总想有暴力之外的方式，导致纠结了很久
'''

import time
import math

def IsPandigital(number):
    i = 0
    digital = {}
    tNum = number
    while tNum > 0 and i < 9:
        if tNum % 10 in digital:
            break
        else:
            digital[tNum%10] = True
        tNum/=10
    if len(digital) == 9 and not(0 in digital):
        return True
    else:
        return False

def FabN(k):
    sqrt5 = math.sqrt(5)
    result = round( (math.pow((1 + sqrt5)/2, k) - math.pow((1 - sqrt5)/2, k))/sqrt5 )
    return result

f1 = 1
f2 = 1

p1 = 1
p2 = 1
i = 2
base = 1000000000
print time.localtime(time.time())
while ( True):
    t = f1 + f2
    f1 = f2 % base
    f2 = t % base

    s = p1 + p2
    p1 = p2
    p2 = s
    while p1 / base > base*base*base:
        p1 /= 10
        p2 /= 10

    i += 1    

    strF = str(p2)
    headNumber = long(strF[0:9])

    if IsPandigital(f2) and IsPandigital(headNumber):
        print("head:",i)
        print(f2)
        break
    
    #if IsPandigital(f2):
    #        print(i)
    #        break
    

#print(f2)
print time.localtime(time.time())