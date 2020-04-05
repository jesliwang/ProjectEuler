'''
3*3 = 9
[n][3][2]
0 没有L
1 1个L

0 不是A
1 A结尾
2 2个A借我



'''

def GetPrizeCount(n):
    start = [[1,1,0 ],[1,0,0]]
    for i in range(1, n):
        nt = [[0,0,0],[0,0,0]]
        nt[0][0]=start[0][0]+start[0][1]+start[0][2]
        nt[0][1]=start[0][0]
        nt[0][2]=start[0][1]
        nt[1][0]=start[0][0]+start[0][1]+start[0][2]+start[1][0]+start[1][1]+start[1][2]
        nt[1][1]=start[1][0]
        nt[1][2]=start[1][1]

        start = nt

    return nt[0][0] + nt[0][1] + nt[0][2] + nt[1][0] + nt[1][1] + nt[1][2]

#print(GetPrizeCount(4))
print(GetPrizeCount(30))


