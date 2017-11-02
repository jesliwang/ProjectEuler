import sys,os
sys.path.append( os.path.dirname(__file__) + "/../Common")

import NumberUtil

def solve_71(target):
    numerator = 0
    delmon = 1


    for index in range(2, target+1):
        left = 0
        right = index

        while left < right:
            mid = (left + right)/2
            if mid * 7 >= 3 * index:
                right = mid
            else:
                left = mid + 1
        if left * 7 < 3 * index:
            if numerator * index < left * delmon:
                numerator = left
                delmon = index
        elif (left - 1) * 7 < 3 * index:
            if numerator * index < (left-1) * delmon:
                numerator = left - 1
                delmon = index


    print numerator ,"/", delmon

    gd = NumberUtil.gcd(numerator, delmon)
    while gd != 1:
        numerator /= gd
        delmon /= gd
        gd = NumberUtil.gcd(numerator, delmon)

    return numerator


solve_71(1000000)
