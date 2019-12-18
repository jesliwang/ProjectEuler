# f(0) = 2
# f(1) = 2a
# f(n) = f(n-1)*a + f(n-2)

def GetRMAX(num):
    f0 = 2
    f1 = 2 * num

    found = set(tuple((f0,f1)))


    dd = num * num

    ret = f1
    while True:
        f3 = ( f1 * num + f0 ) % dd
        if f3 > ret:
            ret = f3
        
        f0 = f1
        f1 = f3

        n = tuple((f0, f1))
        if n in found:
            break
        found.add(n)
    
    return ret

print(GetRMAX(7))
sum = 0
for num in range(3, 1001):
    sum += GetRMAX(num)

print(sum)


