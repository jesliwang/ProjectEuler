import random

def get_prime_dic_and_list(maxNumber):
    primeDic = {}
    primeList = []
    for index in range(2, maxNumber):
        if not primeDic.has_key(index):
            primeList.append(index)
            facter = 2
            while facter * index < maxNumber:
                primeDic[facter*index] = 1
                facter += 1

    return primeDic, primeList



def is_mill_rabin_prime(num):
    if num < 2:
        return False

    if num == 2:
        return True

    if num % 2 == 0:
        return False

    s = 0
    d = num - 1
    while True:
        quatient, reminder = divmod(d, 2)
        if reminder == 1:
            break
        s += 1
        d = quatient

    def try_composite(a):
        if pow(a, d, num) == 1:
            return False
        for i in range(s):
            if pow(a, pow(2,i)*d, num) == (num-1):
                return False
        return True


    for i in range(0,5):
        a = random.randrange(2,num)
        if try_composite(a):
            return False

    return True
