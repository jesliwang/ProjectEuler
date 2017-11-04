import os, sys
import math


file = open(os.path.dirname(__file__) + "/base_exp.txt")

line = file.readline()

a = 2.0
b = 2.0

index = 0
ret = 1


while line:
    index += 1
    val = line.split(',')
    if len(val) != 2:
        print "wrong input"
        break

    ans = b * math.log10(a) - float(val[1])*math.log10(float(val[0]))
    if ans < 0:
        a = float(val[0])
        b = float(val[1])
        ret = index


    line = file.readline()

print a, b, ret
