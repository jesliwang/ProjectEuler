ln = 100001
#ln = 11
primeHub = [1 for i in range(ln)]

primeHub[1] = 1
for i in range(2, ln):
    if primeHub[i] == 1:
        sr = i
        while sr < ln:
            primeHub[sr] *= i
            sr += i

    
fs = [ (index,v) for index,v in enumerate(primeHub) if index > 0]

fs.sort(key=lambda x: x[1])
print(fs[9999])