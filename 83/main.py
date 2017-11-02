import sys,os

file = open(os.path.dirname(__file__) + "/matrix.txt")

line = file.readline()

maxEdge = 80

lists = [[] for i in range(maxEdge)]
index = 0

while line:
    data = line.split(',')
    for col in range(0, len(data)):

        lists[index].append(int(data[col]))

    index += 1

    line = file.readline()

#cal

ans = [[sys.maxint for n in range(maxEdge)] for i in range(maxEdge)]

startList = [(0,0)]
ans[0][0] = lists[0][0]

while len(startList) > 0:
    node = startList[0]
    del startList[0]

    if node[0] >= 1 :
        if ans[node[0]][node[1]] + lists[node[0]-1][node[1]] < ans[node[0]-1][node[1]]:
            ans[node[0]-1][node[1]] = ans[node[0]][node[1]] + lists[node[0]-1][node[1]]
            if (node[0]-1, node[1]) not in startList:
                startList.append((node[0]-1, node[1]))

    if node[1] >= 1:
        if ans[node[0]][node[1]] + lists[node[0]][node[1]-1] < ans[node[0]][node[1]-1]:
            ans[node[0]][node[1]-1] = ans[node[0]][node[1]] + lists[node[0]][node[1]-1]
            if (node[0], node[1]-1) not in startList:
                startList.append((node[0], node[1]-1))

    if node[0] + 1 < maxEdge :
        if ans[node[0]][node[1]] + lists[node[0]+1][node[1]] < ans[node[0]+1][node[1]]:
            ans[node[0]+1][node[1]] = ans[node[0]][node[1]] + lists[node[0]+1][node[1]]
            if (node[0]+1, node[1]) not in startList:
                startList.append((node[0]+1, node[1]))

    if node[1] + 1 < maxEdge:
        if ans[node[0]][node[1]] + lists[node[0]][node[1]+1] < ans[node[0]][node[1]+1]:
            ans[node[0]][node[1]+1] = ans[node[0]][node[1]] + lists[node[0]][node[1]+1]
            if (node[0], node[1]+1) not in startList:
                startList.append((node[0], node[1]+1))


print ans[maxEdge-1][maxEdge-1]
