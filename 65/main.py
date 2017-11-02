import sys,os
sys.path.append( os.path.dirname(__file__) + "/../Common")

import NumberUtil

def digitSum(num):
    tmp = num
    ret = 0
    while tmp > 0:
        ret += tmp%10
        tmp/=10
    return ret

def Solve_65(target):
    number = 0
    delnom = 1
    for index in range(target):
        if index + 1 == target:
            number = number + 2 * delnom
            continue

        tmp = target - index
        if tmp % 3 == 0:
            k = 2*tmp/3
            preDel = delnom
            delnom = k * preDel + number
            number = preDel
        else:
            preDel = delnom
            delnom = preDel + number
            number = preDel

    gd = NumberUtil.gcd(number, delnom)
    while gd != 1:
        number/=gd
        delnom/=gd
        gd = NumberUtil.gcd(number, delnom)

    return digitSum(number)


print Solve_65(100)
