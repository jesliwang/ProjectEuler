import os, sys


class CrossNode:
    __slots__ = ('_up', '_down', '_left', '_right', '_data')
    def __init__(self, data):
        self._up = None
        self._down = None
        self._left = None
        self._right = None
        self._data = data

    def AddLeft(self, item):
        item._left = self._left

        item._right = self
        self._left = item

    def AddRight(self, item):
        item._right = self._right

        item._left = self
        self._right = item

    def AddUp(self, item):
        item._up = self._up

        item._down = self
        self._up = item

    def AddDown(self, item):
        item._down = self._down

        item._up = self
        self._down = item


class DLX:
    __slots__ = ('rowHead','colHead', 'anchor')
    def __init__(self, row, col):
        self.rowHead = [CrossNode(n) for n in range(row)]
        self.colHead = [CrossNode(n) for n in range(col)]
        self.anchor = CrossNode(-1)
        self.anchor.AddRight(self.colHead[0])

        self.anchor.AddDown(self.rowHead[0])

        for index in range(1, row):
            self.rowHead[index-1].AddDown(self.rowHead[index])

        for index in range(1,col):
            self.colHead[index-1].AddRight(self.colHead[index])

    def removeCol(self, index):
        if self.colHead[index]._right:
            self.colHead[index]._right._left = self.colHead[index]._left
        if self.colHead[index]._left:
            self.colHead[index]._left._right = self.colHead[index]._right

    def AddLink(self, r, c):
        newItem = CrossNode(r)
        # may dumplicate r,c
        current = self.rowHead[r]
        while current._right:
            current = current._right

        current.AddRight(newItem)

        current = self.colHead[c]
        while current._down:
            current = current._down

        current.AddDown(newItem)

    def Run(self):
        RowSelected = []

        # remove none rows
        current = self.anchor._down
        while current:
            if None == current._right:
                if current._up:
                    current._up._down = current._down

                if current._down:
                    current._down._up = current._up

            current = current._down

        while self.anchor._right:
            current = self.anchor._right._down

            #print "len", len(RowSelected), self.anchor._right._data
            if current == None:

                while len(RowSelected) > 0:
                    # continue with revert back
                    ansLen = len(RowSelected)

                    callBackArray = []
                    findex = RowSelected[ansLen-1][0]
                    current = RowSelected[ansLen-1][1]
                    reverRow = self.rowHead[findex]
                    #print "werqwerq", current._data

                    current = current._down
                    del RowSelected[ansLen-1]

                    revertAdd = reverRow._right
                    while revertAdd:
                        # find head
                        clHead = revertAdd
                        while None != clHead._up:
                            clHead = clHead._up

                        revertAdd = revertAdd._right

                        #print clHead._data
                        callBackArray.append(clHead)

                    while len(callBackArray) > 0:
                        doing = callBackArray[len(callBackArray) -1]
                        del callBackArray[len(callBackArray) -1]

                        if doing._left:
                            doing._left._right = doing

                        if doing._right:
                            doing._right._left = doing

                        doNode = doing._down

                        while doNode and doNode._down:
                            doNode = doNode._down

                        if None == doNode:
                            continue
                        #print doNode._data,"eee"
                        while doNode != doing:
                            doLeft = doNode._left
                            while doLeft:
                                if doLeft._up:
                                    doLeft._up._down = doLeft
                                if doLeft._down:
                                    doLeft._down._up = doLeft

                                doLeft = doLeft._left

                            doRight = doNode._right
                            while doRight:
                                if doRight._up:
                                    doRight._up._down = doRight
                                if doRight._down:
                                    doRight._down._up = doRight

                                doRight = doRight._right

                            doNode = doNode._up

                    if current == None:
                        continue
                    else:
                        break
                else:
                    # no ans
                    print "no ans"
                    break

            if len(RowSelected) > 0:
                last = RowSelected[len(RowSelected)-1][0]
                while current:
                    ff = True
                    for index in range(0, len(RowSelected)):
                        if RowSelected[index][0] / 9 == current._data / 9:
                            current = current._down
                            ff = False
                            break

                    if ff:
                        break

            if None == current:
                continue


            RowSelected.append([current._data, current])
            # from left to right
            # from top to dwon

            #print len(RowSelected), current._data

            removeCol = []
            leftCurrent = current
            while leftCurrent:
                llHead = leftCurrent._up
                while llHead._up:
                    llHead = llHead._up

                removeCol.append(llHead)

                leftCurrent = leftCurrent._right

            while len(removeCol) > 0:
                doing = removeCol[0]
                del removeCol[0]
                #col remove
                if doing._left:
                    doing._left._right = doing._right

                if doing._right:
                    doing._right._left = doing._left

                removeUD = doing._down

                while removeUD:
                    removeUDLeft = removeUD._left
                    while removeUDLeft:
                        if removeUDLeft._up:
                            removeUDLeft._up._down = removeUDLeft._down

                        if removeUDLeft._down:
                            removeUDLeft._down._up = removeUDLeft._up

                        removeUDLeft = removeUDLeft._left


                    removeUDRight = removeUD._right
                    while removeUDRight:
                        if removeUDRight._up:
                            removeUDRight._up._down = removeUDRight._down

                        if removeUDRight._down:
                            removeUDRight._down._up = removeUDRight._up

                        removeUDRight = removeUDRight._right

                    removeUD = removeUD._down

            #break
        #print len(RowSelected)
        sum = 0
        for index in range(0, len(RowSelected)):
            key = RowSelected[index][0]
            x = key/(9*9)
            y = key/9%9
            v = key % 9 + 1
            print "(", key/(9*9), key/9%9, ")",  key % 9 + 1
            if x == 0 and y == 0:
                sum += v * 100
            if x == 0 and y == 1:
                sum += v * 10
            if x == 0 and y == 2:
                sum += v

        return sum



def checkCanUse(num, dic, x, y):
    flag = True
    for index in range(0,9):
        if num == (ord(dic[x][index]) - ord('0')):
            flag = False
        if num == (ord(dic[index][y]) - ord('0')):
            flag = False

        if not flag:
            break

    if not flag:
        return flag

    mx = x/3
    my = y / 3

    for index in range(0,3):
        for subIndex in range(0,3):
            if num == (ord(dic[3*mx + index][3*my+index]) - ord('0')):
                flag = False
                break
    return flag

def sovle_96(sudu):
    solve = DLX(9*81, 9*9+9*9+9*9)
    for x in range(0,9):
        for y in range(0,9):
            p = ord(sudu[x][y])- ord('0')
            r = (x * 9 + y)*9

            if p == 0:
                for num in range(1,10):
                    if checkCanUse(num, sudu, x, y):
                        solve.AddLink(num-1 + (x*9+y)*9, x*9+num-1)
                        solve.AddLink(num-1 + (x*9+y)*9, 9*9 + y*9 + num - 1)
                        solve.AddLink(num-1 + (x*9+y)*9, 9*9*2 + (x/3 * 3 + y/3)*9 + num-1)
            else:
                solve.AddLink(p-1 + (x*9+y)*9, x*9+p-1)
                solve.AddLink(p-1 + (x*9+y)*9, 9*9 + y*9 + p - 1)
                solve.AddLink(p-1 + (x*9+y)*9, 9*9*2 + (x/3 * 3 + y/3)*9 + p-1)

    ans = solve.Run()
    return ans


file = open(os.path.dirname(__file__) + "/sudoku.txt")
line = file.readline()

aP = 0

while line:
    if line[0] == 'G':
        print line
        sudu = []
        for index in range(9):
            line = file.readline()
            sudu.append(line)

        tmp = sovle_96(sudu)
        print tmp
        aP += tmp

    break
    line = file.readline()

print "ans=", aP
