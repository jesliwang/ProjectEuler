import os, sys

def reverNumber(num):
    tmp = num
    reverse = 0
    while tmp > 0:
        reverse = reverse * 10 + tmp % 10
        tmp /= 10
    return reverse


def palindromic(num):
    reverse = reverNumber(num)

    if num == reverse:
        return True
    else:
        return False



def IslyNumber(num):
    tmp = num
    for index in range(0, 60):
        revert = reverNumber(tmp)
        nextNumber = tmp + revert
        #print nextNumber, tmp, revert
        if palindromic(nextNumber):
            return False

        tmp = nextNumber

    return True

resultNumber = 0
for index in range(1, 10000):
    if IslyNumber(index):
        resultNumber += 1

print resultNumber

print IslyNumber(10677)
