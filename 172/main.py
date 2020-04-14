
'''
f(n,0-9,4^10)
'''

matrix = [ { } for i in range(10)]
for i in range(10):
    if i != 0:
        matrix[i][1<<(2*i)] = 1

M = 18
for i in range(1,M):
    nextMatrix = [ { } for i in range(10)]
    for x in range(10):
        for k,v in matrix[x].items():
            for n in range(10):
                check = (k >> (2*n))&3
                
                if check < 3:
                    key = (((k >> (2*n)) + 1) << (2*n)) | ((( 1 << (2*n) ) - 1)&k)
                    if key not in nextMatrix[n]:
                        nextMatrix[n][key] = 0
                    nextMatrix[n][key] = nextMatrix[n][key] + v
    
    matrix = nextMatrix


ans = 0
for i in range(10):
    for k,v in matrix[i].items():
        ans += v

print(ans)