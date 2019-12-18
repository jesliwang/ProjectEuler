
def ReverseNum(num):
    ret = 0
    tmp = num
    while tmp > 0:
        ret = ret * 10 + tmp%10
        tmp /= 10
    return ret

def IsOddDigits(num):
    tmp = num
    while tmp > 0:
        if tmp % 10 %2 != 1:
            return False
        tmp /= 10
    return True

def IsReversible(num):
    if num % 10 == 0:
        return False
    sum = num + ReverseNum(num)
    return IsOddDigits(sum)

count = 0
for num in range(1, 1000000000):
    if IsReversible(num):
        count += 1

print count
