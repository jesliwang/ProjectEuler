import os, sys

print os.path.dirname(__file__)
file = open(os.path.dirname(__file__) + "/data.txt")


sum = 0

line = file.readline()

while line:
    sum += int(line)
    line = file.readline()

print sum
