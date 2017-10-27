import os, sys

def digitNum(num):
    result = 0
    while num > 0:
        result += 1
        num /= 10
    return result

dict = {
    0: 1,
    1: 1,
    2: 2
}

index = 3

tmp = 2
while digitNum(dict[tmp]) < 1000:
    prePre = (tmp - 1 + 3) % 3
    pre = tmp
    tmp = (tmp + 1) % 3

    dict[tmp] = dict[pre] + dict[prePre]
    index += 1

print index
