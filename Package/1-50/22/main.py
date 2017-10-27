import os, sys

def alphSum(str):
    sum = 0
    for index in range(0,len(str)):
        sum += (ord(str[index]) - ord('A') + 1)
    return sum

file = open(os.path.dirname(__file__) + "/names.txt")

line = file.readline()

names = []

while line:
    data = line.split(",")
    for index in range(0, len(data)):
        names.append(data[index].strip()[1:-1])
    line = file.readline()

names.sort()

result = 0
for index in range(0, len(names)):
    result += alphSum(names[index]) * (index + 1)

print result
