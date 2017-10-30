import os, sys
import random

def Spiral(length):

    for index in range(1, length):
        tmp = 2*index + 1   # 5
        yield pow(tmp, 2)   # 25
        yield pow(tmp, 2) - (tmp - 1) # 21
        yield pow(tmp, 2) - (tmp- 1)*2 #  17
        yield pow(tmp, 2) - (tmp - 1)*3 # 13


primeDic = {}
"""
lim = 100000000

for index in range(2, lim):
    if not primeDic.has_key(index):
        facter = 2
        while facter * index < lim:
            primeDic[facter*index] = 1
            facter += 1

"""
start = 3
startNumber = 1
primeNumber = 0

def gcd(a,b):
    reminder = 0
    while b != 0:
        reminder = a % b
        a = b
        b = reminder

    return a

def rho2(num):

    x_fixed = 2
    cycle_size = 2
    x = 2
    facter = 1

    while facter == 1:
        count = 1
        while count <= cycle_size and facter <= 1:
            x = (pow(x,2) - 1)%num
            facter = gcd(x - x_fixed, num)
            count += 1

        cycle_size *= 2
        x_fixed = x


    return facter

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

    if facter == num:
        return rho2(num)

    return facter

def newRho2(num):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = (pow(x,2)-1)%num
        tmp = (pow(y,2)-1)%num
        y = (pow(tmp, 2)-1)%num
        if x > y:
            d = gcd(x-y, num)
        else:
            d = gcd(y-x, num)

    return d

def newRho(num):
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = (pow(x,2)+1)%num
        tmp = (pow(y,2)+1)%num
        y = (pow(tmp, 2)+1)%num
        if x > y:
            d = gcd(x-y, num)
        else:
            d = gcd(y-x, num)
    if d == num:
        return newRho2(num)
    else:
        return d

#print newRho(49)


"""
def isPrime(num):
    gg = newRho(num)
    if True:#gg > 1 and gg == num:
        for index in range(0,10):
            a = random.randrange(1, num-1)
            #print a,num, pow(a,num-1)%num
            if pow(a,num-1)%num != 1:
                return False

        return True
    return False
"""

def isPrime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    s = 0
    d = num - 1
    while True:
        quatient, reminder = divmod(d, 2)
        if reminder == 1:
            break
        s += 1
        d = quatient

    def try_composite(a):
        if pow(a, d, num) == 1:
            return False
        for i in range(s):
            if pow(a, pow(2,i)*d, num) == (num-1):
                return False
        return True


    for i in range(0,5):
        a = random.randrange(2,num)
        if try_composite(a):
            return False

    return True


while True:
    a = pow(start, 2)
    b = a - (start - 1)
    c = b - (start - 1)
    d = c - (start - 1)

    startNumber += 4
    if isPrime(a):
        primeNumber += 1

    if isPrime(b):
        primeNumber += 1

    if isPrime(c):
        primeNumber += 1

    if isPrime(d):
        primeNumber += 1

    if primeNumber * 100 <  startNumber * 10:
        print "ans=",primeNumber, startNumber, start, float(primeNumber)/startNumber

        print start
        break
    start += 2
    #print primeNumber, startNumber, start, float(primeNumber)/startNumber
    if start > 100000:
        print primeNumber, startNumber
        break

print "end"
#26247
