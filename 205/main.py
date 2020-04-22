
def GetPro(n, m):
    sumMax = n*m + 1
    ansArray=[0 for i in range(sumMax)]
    state = pow(m,n)
    for i in range(0, state):
        s = n
        tmp = i
        key = 0
        while tmp > 0:
            key += tmp % m + 1
            tmp //= m
            s -= 1
        key += s
        ansArray[key] += 1


    return pow(m,n), ansArray

cubicSum, cubicArray = GetPro(6,6)
pyramSum, pyramArray = GetPro(9,4)
print(pyramSum,pyramArray)
print(cubicSum,cubicArray)

ava = 0
for i in range(37):
    minSum = 0
    for j in range(i):
        minSum += cubicArray[j]
    
    ava += minSum * pyramArray[i]

print('%.7f'%(ava/(cubicSum*pyramSum)))
