import os,sys

def check(num,p):
    tmp = num
    sum = 0
    while tmp > 0:
        sum += pow(tmp%10, p)
        tmp/=10

    if num == sum:
        return True
    else:
        return False

def DigitPower(num):
    sum = 0
    for index in range(10, pow(10,num+1)):
        if check(index, num):
            sum += index
            print index

    return sum

print DigitPower(5)
