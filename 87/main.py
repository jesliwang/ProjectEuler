
primeSet = set()

primeCal = set()

maxNum = 50000000

# 10000
maxPrime = 10000
for index in range(2, maxPrime):
    if index not in primeCal:
        primeSet.add(index)
        nx = 2
        while nx * index <= maxPrime:
            primeCal.add(nx * index)
            nx += 1
    

container = set()

print(len(primeSet))

forCoun = sorted(primeSet)


for first in forCoun:
    for second in forCoun:
        for third in forCoun:
            tmp = pow(first, 2) + pow(second, 3) + pow(third, 4)
            if tmp < maxNum:
                container.add(tmp)
            else:
                break
    
print(len(container))
