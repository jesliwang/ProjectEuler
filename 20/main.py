import os, sys

def factor(num):
    if num == 1:
        return 1
    else:
        return num * factor(num - 1)

orig = factor(100)

resul = 0
while orig > 0:
    resul += orig % 10
    orig/=10

print resul
