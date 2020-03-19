import heapq

class Item:
    def __init__(self, mul, nxt, sum, len):
        self.mul = mul
        self.nxt = nxt
        self.sum = sum
        self.len = len

    def __lt__(self, other):
        if self.CalLength() < other.CalLength():
            return True
        elif self.CalLength() == other.CalLength():
            return self.MulVal() < other.MulVal()
        else:
            return False

    def MulVal(self):
        return self.mul * self.nxt

    def SumVal(self):
        return self.sum + self.nxt

    def CalLength(self):
        length = self.mul * self.nxt - self.sum - self.nxt + self.len + 1
        return length
    
    def IsValid(self):
        return self.mul * self.nxt - self.sum - self.nxt >=0

items = []
for val in range(2, 12000):
    heapq.heappush(items, Item(val,2,val,1))

ansDic = {}
ansSum = 0
maxLength = 12000

mulDic = {}


while True:
    tmp = heapq.heappop(items)
    if tmp.CalLength() <= maxLength:
        if tmp.CalLength() not in ansDic:
            #print(tmp.CalLength(),":",tmp.MulVal())
            ansDic[tmp.CalLength()] = 1
            if tmp.MulVal() not in mulDic:
                ansSum += tmp.MulVal()
                mulDic[tmp.MulVal()] = 1
            
        left = Item(tmp.MulVal(), tmp.nxt, tmp.SumVal(), tmp.len + 1)
        down = Item(tmp.mul, tmp.nxt + 1, tmp.sum, tmp.len)
        if left.IsValid():
            heapq.heappush(items, left)
        if down.IsValid():
            heapq.heappush(items, down)
    else:
        break

print("ans=", ansSum)


