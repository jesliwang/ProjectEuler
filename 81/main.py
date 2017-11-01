import sys,os

file = open(os.path.dirname(__file__) + "/matrix.txt")

line = file.readline()

lists = [[] for i in range(80)]
index = 0

while line:
    data = line.split(',')
    for col in range(0, len(data)):
        ans = sys.maxint
        if col > 0 and index > 0:
            ans = min(ans, lists[index-1][col] + int(data[col]))
            ans = min(ans, lists[index][col-1] + int(data[col]))
        elif col > 0:
            ans = min(ans, lists[index][col-1] + int(data[col]))
        elif index > 0:
            ans = min(ans, lists[index-1][col] + int(data[col]))
        else:
            ans = int(data[col])

        lists[index].append(ans)

    index += 1
    line = file.readline()


print lists[79][79]
