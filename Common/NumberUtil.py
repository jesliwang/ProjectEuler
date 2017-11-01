
def number_Length(num):
    tmp = num
    length = 0
    while tmp > 0:
        length += 1
        tmp /=10

    return length
