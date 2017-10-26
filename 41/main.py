"""
https://en.wikipedia.org/wiki/Pollard%27s_rho_algorithm
"""

import os, sys

target = 600851475143

def gcd(a,b):
    reminder = 0
    while b != 0:
        reminder = a % b
        a = b
        b = reminder

    return a

def rho(num):

    x_fixed = 2
    cycle_size = 2
    x = 2
    facter = 1

    while facter == 1:
        count = 1
        while count <= cycle_size and facter <= 1:
            x = (pow(x,2) + 1)%num
            facter = gcd(x - x_fixed, num)
            count += 1

        cycle_size *= 2
        x_fixed = x

    return facter


def isPrime(num):
    tmp = num
    aList = []

    prime = rho(tmp)
    if prime != tmp:
        return False
    while prime != tmp:
        aList.append(prime)
        while tmp%prime == 0:
            tmp/=prime

        prime = rho(tmp)

    if tmp != 1:
        aList.append(tmp)

    return len(aList) == 1

print isPrime(2143)

#deqList = [9,8,7,6,5,4,3,2,1]

def reQu(deqList, preNum):
    if len(deqList) == 0:
        flag = isPrime(preNum)
        if flag:
            print preNum
        return flag
    else:
        for index in range(0, len(deqList)):
            tmp = preNum * 10 + deqList[index]
            y = deqList[index]
            del deqList[index]
            if reQu(deqList, tmp):
                return True
            else:
                deqList.insert(index, y)

        return False

print "1"
reQu([4,3,2,1], 0)
print "2"
reQu([7,6,5,4,3,2,1], 0)
print "3"
reQu([8,7,6,5,4,3,2,1], 0)
print "4"
reQu([9,8,7,6,5,4,3,2,1], 0)
