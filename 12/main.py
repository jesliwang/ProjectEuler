import os,sys

flag = False
index = 1
sum = 0

def num_divisors(num):
    ret = 0
    tmp_index = 1
    while tmp_index * tmp_index <= num:
        if num % tmp_index == 0:
            ret += 1
            if num / tmp_index != tmp_index:
                ret += 1
        tmp_index += 1

    return ret

while False == flag:
    sum += index
    div_num = num_divisors(sum)
    print sum , div_num
    if div_num > 500:
        flag = True
    else:
        index += 1


print sum
