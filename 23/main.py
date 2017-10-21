import os, sys

dict={}

def sumDivisor(num):
    sum = 0
    index = 1;
    while index * index <= num:
        if num % index == 0:
            sum += index
            if num / index != index:
                sum += num / index
        index += 1

    return sum - num


def checkAbundant(num):
    result = False
    for index in range(1, num/2 + 1):
        #print index, (num - index)
        if dict[index] == 2 and dict[num - index] == 2:
            result = True
            break
    return result



for index in range(1, 28124):
    if sumDivisor(index) == index:
        dict[index] = 0
    elif sumDivisor(index) < index:
        dict[index] = 1 # deficient
    else:
        dict[index] = 2 # abundant

result = 0

print checkAbundant(24), dict[12]

for index in range(1, 28124):
    if not checkAbundant(index):
        result += index
    #else:
    #    print index
print result
