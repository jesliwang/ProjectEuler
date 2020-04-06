'''
2^10 * 10 * 40

'''
def GetPadigital(n):
    state = 1<<10
    start = [[0 for y in range(state)] for x in range(10)]

    for i in range(1, 10):
        start[i][1<<i] = 1
    
    ans = 0
    for j in range(10):
            ans += start[j][state - 1]

    for i in range(1, n):
        end = [[0 for y in range(state)] for x in range(10)]
        for x in range(10):
            if x + 1 < 10:
                num = x+1
                for j in range(state):
                    end[num][j | (1<<num)] += start[x][j]
                
            if x - 1 >= 0:
                num = x - 1
                for j in range(state):
                    end[num][j | (1<<num)] += start[x][j]
        start = end
    
        for j in range(10):
            ans += start[j][state - 1]

    return ans

print(GetPadigital(40))