import os, sys

def fact(num):
    result = 1
    target = 1
    while target <= num:
        result *= target
        target += 1

    return result


print fact(40)/fact(20)/fact(20)
