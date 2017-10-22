import os, sys

def changeCoin(num):
    orig = [1,2,5, 10, 20, 50, 100, 200]
    dict = {0:1}

    for col in range(0, len(orig)):
        for index in range(1, num+1):
            if not dict.has_key(index):
                dict[index] = 0

            if dict.has_key(index - orig[col]):
                dict[index] += dict[index-orig[col]]

    return dict[num]


print changeCoin(200)
