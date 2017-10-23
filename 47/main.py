import os, sys

primeDic = {}

lim = 1000000

target = 4

for index in range(2, lim):
    if not primeDic.has_key(index):
        facter = 2
        while facter * index < lim:
            if not primeDic.has_key(facter * index):
                primeDic[facter*index] = 1
            else:
                primeDic[facter*index] = 1 + primeDic[facter*index]
            facter += 1
    else:
        if target == primeDic[index]:
            flag = True
            for subindex in range(1, target):
                if not (primeDic.has_key(index + subindex) and (target == primeDic[index + subindex]) ):
                    flag = False
                    break
            if flag:
                print index
                break
