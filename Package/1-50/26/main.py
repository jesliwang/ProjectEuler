import os, sys



def recyleLeng(num):
    dict = {}
    start = 1
    pos = 0

    result = 0

    while start % num != 0:
        if not dict.has_key(start):
            dict[start] = pos
            pos += 1
            start *= 10
        else:
            result = pos - dict[start]
            break

        start = start % num

    return result

length = 0
priRest = 0
for index in range(2, 1000):
    tmp = recyleLeng(index)
    if tmp > length:
        length = tmp
        priRest = index

print priRest
