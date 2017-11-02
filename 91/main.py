import os, sys

def solve_91(a, b, base, mod):
    lists=[]
    tmp = b
    while tmp > 0:
        lists.append(tmp%base)
        tmp/=base


    ans = a
    start = base

    for index in range(0, len(lists)):
        if lists[index] > 0:
            ans = (ans * start)%mod

        start = (start * start)%mod

    return (ans + 1)%mod

print solve_91(28433, 7830457, 2, pow(10,10))
