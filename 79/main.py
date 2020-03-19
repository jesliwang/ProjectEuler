
import sys,os

file = open(os.path.dirname(__file__) + "/keylog.txt")

line = file.readline()

logicSet = set()

while line:
    atom1 = tuple((int(line[0]), int(line[1])))
    atom2 = tuple((int(line[1]),int(line[2])))
    atom3 = tuple((int(line[0]), int(line[2])))

    if atom1 not in logicSet:
        logicSet.add(atom1)

    if atom2 not in logicSet:
        logicSet.add(atom2)
    if atom3 not in logicSet:
        logicSet.add(atom3)

    line = file.readline()


def GetResult(preSet, checkSet, li):
    #print("======")
    #print(preSet)
    #print(checkSet)
    #print(li)
    if len(preSet) == 0:
        #print("resul=",len(checkSet))
        if len(checkSet) + len(li) == 8:
            print(checkSet)
            print(li)
        return len(checkSet) + len(li)
    result = 100000000
    
    for i in range(0, 10):
        # remove set with i
        tmpSet = set()
        tmpCheck = set()
        for val in preSet:
            if val[0] == i:
                tmpSet.add(val)
                tmpCheck.add(val[1])
        if len(tmpSet) > 0:
            checkSet.discard(i)
            p = checkSet.union(tmpCheck)
            #print("----------")
            #print(p)
            li.append(i)
            y = GetResult(preSet.difference(tmpSet), p, li)
            #print("ans=",y)
            result = min(result, y )
            checkSet.add(i)
            li.pop()
        
    #print("resul=",result)

    return result


li = []
print(GetResult(logicSet, set(), li))
