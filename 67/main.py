import os, sys
from copy import deepcopy

file = open(os.path.dirname(__file__) + "/triangle.txt")

dict = {}
active_dic = {}

line = file.readline()

while line:
    data = line.split(" ")
    for index in range(0, len(data)):
        if dict.has_key(index):
            active_dic[index] = int(data[index]) + dict[index]
        else:
            active_dic[index] = int(data[index])

        if dict.has_key(index - 1):
            active_dic[index] = max(active_dic[index], int(data[index]) + dict[index - 1])

    dict.clear()
    dict = deepcopy(active_dic)
    active_dic.clear()

    line = file.readline()


result = 0

for key,value in dict.items():
    result = max(result, value)

print result
