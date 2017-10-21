import os, sys

dict = {}

def sumDivisor(num):
    sum = 0
    index = 1
    while index * index <= num:
        if num % index == 0:
            sum += index
            if num / index != index:
                sum += num / index
                #print index, num/index

        index += 1
    return sum - num

result = 0

#print sumDivisor(220), sumDivisor(284)

for index in range(1, 10000):
    if False == dict.has_key(index):
        sum = sumDivisor(index)
        dict[index] = sum


    if dict[index] < index and dict[index] > 0 and dict[dict[index]] == index:
        result += index + dict[index]

print result
