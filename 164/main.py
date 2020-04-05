'''
[0, 1, 1, 1, 1, 1, 1, 1]

f[n][x][y][z] = m


'''

start = [ [ [ 1 if x !=0 and x + y + z <=9 else 0 for z in range(10)] for y in range(10) ] for x in range(10)]

for i in range(3,20):
    tmp = [ [ [0 for z in range(10)]  for y in range(10)] for x in range(10)]
    for x in range(10):
        for y in range(10):
            for z in range(10):
                for nt in range(10):
                    if nt + y + z <= 9:
                        tmp[y][z][nt] += start[x][y][z]
    
    start = tmp

ans = 0
for x in range(10):
    for y in range(10):
        for z in range(10):
            ans += start[x][y][z]

print(ans)

