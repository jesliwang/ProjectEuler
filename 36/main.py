import os, sys

def palindromic(str):
    flag = True
    for index in range(0, len(str)/2 + 1):
        #print str[index], str[len(str) - 1 - index]
        if str[index] != str[len(str) - 1 - index]:
            flag = False
            break

    return flag

sum = 0

for index in range(1, 1000000):
    if palindromic(str(index)) and palindromic(bin(index)[2:]):
        print index
        sum += index

print "sum=",sum
