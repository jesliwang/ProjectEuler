import sys,os
sys.path.append( os.path.dirname(__file__) + "/../Common")

import NumberUtil

def Solve_63():
    ret = 0

    start = 1
    while True:
        index = 1
        while True:
            length = NumberUtil.number_Length(pow(index, start));
            if length > start:
                break
            elif length == start:
                print index, start, pow(index, start)
                ret += 1

            index += 1

        if index == 2:
            break

        if start > 1000:
            break
        start += 1

    return ret
print Solve_63()
