limit = 100
#limit=6
primeSearch = [0 for i in range(limit)]
prime = []
for i in range(2, limit):
    if primeSearch[i] == 0:
        prime.append(i)
        index = 2
        while index * i < limit:
            primeSearch[index*i] = 1
            index += 1

lt = [1]
maxV = pow(10,9)
#maxV = pow(10,8)
for i in range(len(prime)):
    end = len(lt)
    m = prime[i]
    while m <= maxV:
        for j in range(end):
            if lt[j] * m <= maxV:
                lt.append(lt[j]*m)
        
        m *= prime[i]
    
print(len(lt))