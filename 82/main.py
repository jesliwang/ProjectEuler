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

ans = [[] for i in range(maxEdge)]
for col in range(0, maxEdge):
    for row in range(0, maxEdge):
        ans[row].append(0)
        if col <= 0:
            ans[row][col] = lists[row][col]
        else:
            if row <= 0:
                ans[row][col] = ans[row][col-1] + lists[row][col]
            else:
                ans[row][col] = min(ans[row][col-1], ans[row-1][col]) +lists[row][col]

    for tRow in range(0, maxEdge):
        row = maxEdge - 1 - tRow
        if col > 0:
            if row >= maxEdge - 1:
                ans[row][col] = min(ans[row][col], ans[row][col-1] + lists[row][col])
            else:
                ans[row][col] = min(ans[row][col], min(ans[row][col-1], ans[row+1][col]) +lists[row][col])



solve82 = sys.maxint
for index in range(0,maxEdge):
    solve82 = min(solve82, ans[index][maxEdge - 1])
print solve82
