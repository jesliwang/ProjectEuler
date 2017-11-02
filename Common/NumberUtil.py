
def number_Length(num):
    tmp = num
    length = 0
    while tmp > 0:
        length += 1
        tmp /=10

    return length


def gcd(a,b):
    reminder = 0
    while b != 0:
        reminder = a % b
        a = b
        b = reminder

    return a
