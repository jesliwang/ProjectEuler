
def generateC(n):
    ret = 1
    for index in range(1, n+1):
        ret = ret * (n + 1 - index) / index
        yield ret

lim = 1000000

resulatNum = 0
for n in range(1, 101):
    for data in generateC(n):
        if data > lim:
            resulatNum += 1


print resulatNum
