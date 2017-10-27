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

for index in range(1, 100):
    for subIndex in range(index+1, 100):
        if index % 10 == subIndex / 10: # xm/my
            if index * (subIndex % 10) == subIndex * (index / 10) :
                #if gcd(index, index/10) != min(index, index/10) :
                    print index, subIndex
        elif index / 10 == subIndex %10: # mx/ym
            if index * (subIndex / 10) == subIndex * (index % 10) :
                #if gcd(index, index%10) != min(index, index%10)  :
                    print index, subIndex
        elif index / 10 == subIndex /10: # mx/my
            if index * (subIndex % 10) == subIndex * (index % 10) :
                #if gcd(index, index%10) != min(index, index%10) :
                    print index, subIndex
        elif index % 10 == subIndex %10: #xm/ym
            if index * (subIndex / 10) == subIndex * (index / 10) :
                #if gcd(index, index/10) != min(index, index/10) :
                    print index, subIndex


print "before"
print denominator, "/", numerator

print "after"

while gcd(denominator, numerator) > 1:
    dev = gcd(denominator, numerator)
    denominator /= dev
    numerator /= dev

print denominator, "/", numerator
