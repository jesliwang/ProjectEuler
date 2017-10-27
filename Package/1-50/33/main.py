# 第一次提交了空格么？？？
import os, sys

def gcd(a,b):
    if b == 0:
        return a

    while b != 0:
        reminder = a%b
        a = b
        b = reminder

    return a

denominator = 1
numerator = 1

for index in range(10, 100):
    for subIndex in range(index+1, 100):
        if index % 10 == subIndex / 10: # xm/my
            if index * (subIndex % 10) == subIndex * (index / 10) :
                print index, subIndex
                numerator *= index
                denominator *= subIndex



print "before"
print numerator, "/", denominator

print "after"

while gcd(denominator, numerator) > 1:
    dev = gcd(denominator, numerator)
    denominator /= dev
    numerator /= dev

print numerator, "/", denominator
