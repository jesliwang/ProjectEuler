seq = [1]
num = set()
num.add(1)

n = 51
for i in range(1, n):
    nt = [1]
    for i in range(len(seq)-1):
        nt.append(seq[i]+seq[i+1])
    nt.append(1)

    for i in range(len(nt)):
        num.add(nt[i])
    
    seq = nt

#print('=======')
limit = 1000000
primeSearch = [0 for i in range(limit)]
prime = []
for i in range(2, limit):
    if primeSearch[i] == 0:
        prime.append(i)
        index = 2
        while index * i < limit:
            primeSearch[index*i] = 1
            index += 1

#print('-----')
ans = 0
for val in num:
    flag = True
    tmp = val
    for i in range(len(prime)):
        if tmp % (prime[i]*prime[i]) == 0:
            flag = False
            break
        
        if tmp % prime[i] == 0:
            tmp //= prime[i]
    if i == len(prime):
        print(val,tmp)

    if flag:
        ans += val
print(ans)
        