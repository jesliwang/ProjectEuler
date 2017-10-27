import os, sys

result = 0
start = 6

def isRune(num):
    if num % 100 != 0:
        return num % 4 == 0
    else:
        return num % 400 == 0
# 1, 3, 5, 7, 8, 10, 12
thirtyDays={
    1 : False,
    3 : False,
    4 : True,
    5 : False,
    6 : True,
    7 : False,
    8 : False,
    9 : True,
    10 : False,
    11 : True,
    12 : False
}

for index in range(1900, 2001):
    for month in range(1, 13):
        if (start + 1) % 7 == 6:
            print index, month
            result += 1

        if thirtyDays.has_key(month):
            if thirtyDays[month]:
                start = (start + 30) % 7
            else:
                start = (start + 31) % 7
        else:
            if isRune(index):
                start = (start + 29) % 7
            else:
                start = (start + 28) % 7

print result
