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


def getLargePrime(num):
    tmp = num
    aList = []

    prime = rho(tmp)
    while prime != tmp:
        aList.append(prime)
        while tmp%prime == 0:
            tmp/=prime

        prime = rho(tmp)

    if tmp != 1:
        aList.append(tmp)
    aList.sort();
    aList.reverse();

    return aList[0]

print getLargePrime(13195)
print getLargePrime(target)
