import os, sys

target = 1000000

arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

dict = {}

result = 1
for index in range(0, 10):
    result = result * (index + 1)
    dict[index + 1] = result

start = 10

strResult = ""

while start > 0:
    #print target, dict[start]
    if target > dict[start]:
        print "yy"
    elif target == dict[start]:
        while len(arr):
            print arr[len(arr) - 1]
            strResult += arr[len(arr) - 1]
            del arr[len(arr) - 1]
        break
    else:
        index = 0
        while target > dict[start - 1]:
            target -= dict[start - 1]
            index += 1

        print arr[index]
        strResult += arr[index]
        del arr[index]

    start -= 1


print strResult
